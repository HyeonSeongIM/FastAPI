from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers import items
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Item Management API", version="v1")

# 라우터 등록
app.include_router(items.router, prefix="/v1")

# 중앙 집중형 에러 처리
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError) -> JSONResponse:
    return JSONResponse(status_code=400, content={"detail": str(exc)})

@app.get("/")
async def read_root() -> dict[str, str]:
    """루트 엔드포인트: API 상태 확인."""
    return {"message": "Welcome to the Item Management API"}