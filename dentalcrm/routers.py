from fastapi import APIRouter
from emedcard.controllers import router as emedcard


router = APIRouter(prefix="/api")
router.include_router(emedcard)
