from sqlalchemy import create_engine, Column, String, Float, MetaData, Table
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = f"postgresql://threatuser:threatpass@db:5432/threatdb"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

threats = Table(
    "threats", metadata,
    Column("indicator", String, primary_key=True),
    Column("source", String),
    Column("geo", String),
    Column("asn", String),
    Column("score", Float)
)

def init_db():
    metadata.create_all(engine)

def save_to_db(data):
    conn = engine.connect()
    for item in data:
        stmt = threats.insert().values(**item).on_conflict_do_nothing(index_elements=['indicator'])
        conn.execute(stmt)
    conn.close()