from emedcard.controllers import router as emedcard
from fastapi import APIRouter
from users.controllers import router as users
from financials.controllers import router as fin

router = APIRouter(prefix="/api")
router.include_router(emedcard)
router.include_router(users)
router.include_router(fin)
