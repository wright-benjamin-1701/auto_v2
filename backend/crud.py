from datetime import datetime
from models import Page, PageCreate
from sqlmodel import Session


def try_create_page(*, session: Session, page_create: PageCreate) -> Page:
    try:
        create_page(session=session, page_create=page_create)
    except:
        session.rollback()
        pass
        # raise ValueError("Page already exists")


def create_page(*, session: Session, page_create: PageCreate) -> Page:

    db_obj = page_create
    db_obj.added = datetime.now()

    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def update_page(*, session: Session, db_page: Page) -> Page:

    db_page.updated = datetime.now()

    session.commit()
    session.refresh(db_page)

    return db_page
