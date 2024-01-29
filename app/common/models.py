from peewee import Model, CharField, BooleanField, DateTimeField, ForeignKeyField, SQL
from app.core.config import database


class BaseModel(Model):
    class Meta:
        database = database


class Application(BaseModel):
    app_name = CharField(unique=True)


class ClipboardEntry(BaseModel):
    content = CharField()
    timestamp = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_pinned = BooleanField(default=False)
    source_app = ForeignKeyField(Application, backref="entries", null=True)


with database:
    database.create_tables([Application, ClipboardEntry])
