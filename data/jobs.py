import sqlalchemy
import datetime
from sqlalchemy import orm, PrimaryKeyConstraint
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    __table_args__ = (
        PrimaryKeyConstraint('team_leader'),
    )

    id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(), nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(), nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.BOOLEAN, nullable=True)
    user = orm.relationship('User')
