from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import default_settings

database_url = "sqlite:///crawl.db"

engine = create_engine(database_url)

Base = declarative_base()


class Page(Base):
    __tablename__ = "pages"
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    url = Column("url", String(), index=True, unique=True)
    content = Column("content", Text())
    added = Column("added", DateTime())
    updated = Column("updated", DateTime())


class Link(Base):
    __tablename__ = "links"
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    source = Column("source", ForeignKey(Page.url))
    destination = Column("destination", ForeignKey(Page.url))


class PageCreate(Page):
    pass


class PageUpdate(Page):
    pass

class LinkCreate(Link):
    pass

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

default_page = PageCreate(
    url=default_settings.default_search_settings.starting_url,
    added=datetime.now(),
    content=default_settings.default_search_settings.starting_content,
)

try:
    db_obj = default_page
    db_obj.added = datetime.now()
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
except:
    pass


session.close()
