from fastapi import APIRouter
from starlette.responses import Response
from starlette.status import HTTP_200_OK

router = APIRouter()


@router.get("/", status_code=200)
async def get():
    return Response(status_code=HTTP_200_OK)
