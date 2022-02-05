import pglet
from pglet import Text


def main(page):
    print(page.user_auth_provider, page.user_name, page.user_email)
    page.add(Text(f"Hello to session {page.session_id}!"))


pglet.app(target=main, permissions="")
