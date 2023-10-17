import shutil

from fastapi import APIRouter, UploadFile

# from app.tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)
