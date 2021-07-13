from pf_sqlalchemy.db.orm import Base, database

from application.composer.composer.data.composer_enum import CardType


class Card(Base):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column("name", database.String(150), nullable=False)
    title = database.Column("title", database.String(200), nullable=False)
    description = database.Column("description", database.Text())
    target = database.Column("target", database.String(200))
    targetType = database.Column("target_type", database.String(200))
    configuration = database.Column("configuration", database.Text())
    type = database.Column("type", database.Enum(CardType), nullable=False)

