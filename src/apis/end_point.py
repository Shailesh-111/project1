from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from src.database import get_db
from requests import Session
from src.model.user import User
from src.schemas.users import UsersCreate, UserUpdate

user_route = FastAPI(prefix="v1")


@user_route.post("/create_user")
def create_user_(data: UsersCreate, db: Session = Depends(get_db)):
    try:
        user = User(**data.dict())
        db.add(user)
        db.commit()

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": "User created successfully",
            },
        )
    except HTTPException as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": e.detail,
            },
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Internal Server Error",
            },
        )


@user_route.post("/update_user/{user_id}")
def update_user(user_id: str, data: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        for field, value in data.dict().items():
            setattr(user, field, value)

        db.commit()

        return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True,
                    "message": "User updated successfully",
                },
            )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": e.detail,
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Internal Server Error",
            },
        )


@user_route.delete("/delete_user/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        db.delete(user)
        db.commit()

        return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True,
                    "message": "User deleted successfully",
                },
            )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": e.detail,
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Internal Server Error",
            },
        )


@user_route.get("/get_all_users")
def get_all_users(db: Session = Depends(get_db)):
    try:
        users = db.query(User).all()
        users_list = [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "status": user.status,
            }
            for user in users
        ]

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": users_list,
                "message": "User fetch successfully",
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Internal Server Error",
            },
        )
