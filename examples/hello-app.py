import pglet
from pglet import Text

def main(page):
    page.add(Text(f"Hello to session {page.connection.conn_id}!"))

pglet.app(target=main, web=True)