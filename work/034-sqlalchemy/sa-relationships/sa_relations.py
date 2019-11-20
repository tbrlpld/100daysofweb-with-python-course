# -*- coding: utf-8 -*-

"""Jsut testing some of the relation ship stuff."""

import os
import shutil

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


db_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "db.sqlite",
)
engine = sa.create_engine("sqlite:///" + db_path, echo=True)
Session = orm.sessionmaker()
Session.configure(bind=engine)


parent_child_table = sa.Table(
    "parent_child_association",
    Base.metadata,
    sa.Column("parent_id", sa.Integer, sa.ForeignKey("parents.id")),
    sa.Column("child_id", sa.Integer, sa.ForeignKey("children.id")),
)


class Parent(Base):
    """Parent class."""

    __tablename__ = "parents"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(20))

    # child_id = sa.Column(sa.Integer, sa.ForeignKey("children.id"))
    children = orm.relationship(
        "Child",
        secondary=parent_child_table,
        back_populates="parents",
    )

    def __repr__(self):
        return "<Parent {0}: {1}>".format(self.id, self.name)


class Child(Base):
    """Child class."""

    __tablename__ = "children"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(20))

    parents = orm.relationship(
        "Parent",
        secondary=parent_child_table,
        back_populates="children",
    )

    def __repr__(self):
        return "<Child {0}: {1}>".format(self.id, self.name)


if __name__ == "__main__":
    if os.path.exists(db_path):
        os.remove(db_path)

    # Create the tables
    Base.metadata.create_all(engine)

    alice = Parent(name="Alice")
    bob = Parent(name="Bob")

    charlie = Child(name="Charlie")
    alice.children.append(charlie)
    bob.children.append(charlie)

    session = Session()
    session.add(alice)
    session.add(bob)
    session.add(charlie)
    session.commit()

    print(alice.children)
    print(bob.children)
    print(charlie.parents)
