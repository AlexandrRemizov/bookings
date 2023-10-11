#!/bin/bash

uvicorn app.main:app --reload --host 0.0.0.0
#gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000