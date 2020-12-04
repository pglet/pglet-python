import pglet
from pglet import Page

def test_page():
    # create page
    p = pglet.page('test_page', noWindow=True)
    
    assert p.url != "" and p.url.startswith('http'), "Test failed"
    assert p.conn_id != "", "Test failed"
    assert p.conn_id != "", "Test failed"

    p.update(Page(title="Hello, title!", padding=0))

