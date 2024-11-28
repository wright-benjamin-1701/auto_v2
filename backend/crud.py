from datetime import datetime
from models import Page, PageCreate, Link, LinkCreate
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


def create_link(*,session:Session,link_create:LinkCreate)-> Link:

    session.add(link_create)
    session.commit()
    session.refresh(link_create)

    return link_create

def read_pages(*,session:Session):

    url_response = session.query(Page.url).all()
    urls = [item for sublist in url_response for item in sublist]
    
    return urls