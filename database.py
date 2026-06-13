from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Sk268dip%40@127.0.0.1:5432/smartgrid"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

from models import Base

Base.metadata.create_all(bind=engine)

print("Table Created Successfully")