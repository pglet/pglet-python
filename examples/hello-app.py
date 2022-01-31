import pglet
from pglet import Text


def main(page):
    page.add(Text(f"Hello to session {page.session_id}!"))


pglet.app(target=main)
