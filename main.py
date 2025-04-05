# main.py
from fastapi import FastAPI
from routers import member

app = FastAPI()

print("Registering member router")  # 디버깅 로그 추가
app.include_router(member.router)
print("Member router registered successfully")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}