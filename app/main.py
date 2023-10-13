import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.users.router import router_auth, router_users
from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels

from app.logger import logger

app = FastAPI(
    title='Бронирование отелей',
    version="0.1.1",
    # root_path="/api"
)
app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_bookings)

#origins = [
#    "http://localhost:3000",
#]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4)
    })
    return response
