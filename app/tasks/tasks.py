import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.config import settings
from app.logger import logger
from app.tasks.celery_main import celery
from app.tasks.email_templates import create_booking_confirmation_temlate
import subprocess


@celery.task
def process_pic(
    path: str,
):
    im_path = Path(path)
    # Запуск команды ls -la
    result = subprocess.run(['ls', '-la'], capture_output=True, text=True, cwd="app/static/images/")

    # Проверка кода возврата команды
    if result.returncode == 0:
        # Вывод результата команды
        print(result.stdout)
    else:
        # Вывод ошибки, если команда завершилась с ошибкой
        print(result.stderr)
    im = Image.open(im_path)
    for width, height in [
        (1000, 500),
        (200, 100)
    ]:
        resized_img = im.resize(size=(width, height))
        resized_img.save(f"app/static/images/resized_{width}_{height}_{im_path.name}")
    # Запуск команды ls -la
    result = subprocess.run(['ls', '-la'], capture_output=True, text=True, cwd="app/static/images/")

    # Проверка кода возврата команды
    if result.returncode == 0:
        # Вывод результата команды
        print(result.stdout)
    else:
        # Вывод ошибки, если команда завершилась с ошибкой
        print(result.stderr)


@celery.task
def send_booking_confirmation_email(
    booking: dict,
    email_to: EmailStr,
):
    email_to = settings.SMTP_USER_TEST
    msg_content = create_booking_confirmation_temlate(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
    logger.info(f"Successfully send email message to {email_to}")
