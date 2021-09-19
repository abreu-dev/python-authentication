from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette.status import HTTP_200_OK
from src.api.auth.auth_bearer import JWTBearer

router = APIRouter()


@router.get("/", dependencies=[Depends(JWTBearer())])
async def get():
    return Response(status_code=HTTP_200_OK)
