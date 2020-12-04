import pglet

def test_page():
    # create page
    p = pglet.page('test_send', no_window=True)
    
    assert p.url != "" and p.url.startswith('http'), "Test failed"
    assert p.conn_id != "", "Test failed"
    assert p.conn_id != "", "Test failed"

    # clean page command
    r = p.send("clean page")
    assert r == "", "Test failed"

    # add text command
    r = p.send("add text value='Hello'")
    assert r.startswith('_'), "Test failed"

    # add button command
    r = p.send("add button id=ok text='OK'")
    assert r == "ok", "Test failed"

