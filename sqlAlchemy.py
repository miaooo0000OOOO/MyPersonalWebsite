import sqlalchemy as db
from config import DB_URI

engine = db.create_engine(DB_URI)
conn = engine.connect()
metadata = db.MetaData()
table = db.Table(metadata)

print(metadata)