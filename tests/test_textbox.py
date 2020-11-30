import pglet

def test_textbox():
    tb = pglet.Textbox(id="txt1", label="Your name:")
    assert isinstance(tb, pglet.Control)
    assert isinstance(tb, pglet.Textbox)
    assert str(tb) == "textbox id=\"txt1\" label=\"Your name:\"", "Test failed"

def test_add_textbox():
    p = pglet.page('page1', noWindow=True)
    tb_id = p.add_textbox(value="Test3")
    assert tb_id.startswith('_'), "Test failed"