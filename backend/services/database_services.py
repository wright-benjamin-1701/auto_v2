from models import Page


def get_unprocessed_page_batch(session, batch_size):
    pages = (
        session.query(Page)
        .filter(Page.updated == None)
        .order_by(Page.added)
        .limit(batch_size)
        .all()
    )
    return pages
