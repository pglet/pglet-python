import pglet

def test_page():
    p = pglet.page('page1')

    assert p.url != "" and p.url.startswith('http'), "Test failed"
    assert p.conn_id != "", "Test failed"
