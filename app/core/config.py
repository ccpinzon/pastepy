from peewee import SqliteDatabase

DATABASE_PATH = "resources/pastepy.db"

database = SqliteDatabase(DATABASE_PATH)
