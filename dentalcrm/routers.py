from emedcard.controllers import router as emedcard
from fastapi import APIRouter
from users.controllers import router as users

router = APIRouter(prefix="/api")
router.include_router(emedcard)
router.include_router(users)
