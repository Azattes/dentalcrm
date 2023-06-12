from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dentalcrm.dependencies import get_database
from dentalcrm.routers import router

app = FastAPI()
app.state.database = get_database()
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.disconnect()
