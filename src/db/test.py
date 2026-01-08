from sqlalchemy import text
from src.db.session import engine

with engine.begin() as conn:
    result = conn.execute(text("select 1")).scalar()

print("DB OK:", result)
