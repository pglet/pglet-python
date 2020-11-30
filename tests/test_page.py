import pglet

def test_page():
    # create page
    p = pglet.page('page1')
    
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

def test_textbox():
    tb = pglet.Textbox(id="txt1", label="Your name:")
    assert str(tb) == "textbox id=\"txt1\" label=\"Your name:\"", "Test failed"

def test_add_textbox():
    p = pglet.page('page1')
    tb_id = p.add_textbox(value="Test2")
    assert tb_id.startswith('_'), "Test failed"