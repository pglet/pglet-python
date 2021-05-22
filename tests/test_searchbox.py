import pytest
import pglet
from pglet import SearchBox

def test_searchbox_add():
    sb = SearchBox(value='', placeholder="search for something", underlined=True, icon='icon1',
        icon_color='color1', data='data1')
    assert isinstance(sb, pglet.Control)
    assert isinstance(sb, pglet.SearchBox)
    assert sb.get_cmd_str() == ('searchbox data="data1" icon="icon1" iconcolor="color1" '
        'onchange="false" placeholder="search for something" underlined="true" value=""'), "Test failed"