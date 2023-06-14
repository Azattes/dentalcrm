from typing import Any, Dict, Optional

from fastapi import HTTPException, status


class APIException(HTTPException):
    status_code: int
    detail: str

    def __init__(self, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(
            status_code=self.status_code, detail=self.detail, headers=headers
        )


class PermissionDeniedException(APIException):
    status_code: int = status.HTTP_403_FORBIDDEN
    detail: str = "Permission denied"


class NotFoundException(APIException):
    status_code: int = status.HTTP_404_NOT_FOUND
    detail: str = "Not Found"


class IncorrectDataForLoginException(APIException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "Incorrect authorization data"
