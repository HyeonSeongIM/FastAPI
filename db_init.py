# db_init.py
from database import Base, engine
import models.member  # 멤버 모델 임포트

# 테이블 생성
Base.metadata.create_all(bind=engine)