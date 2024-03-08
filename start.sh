#!/bin/bash
export FLASK_APP=src.app
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000 --reload