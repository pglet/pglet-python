import pytest
import pglet
from pglet import Slider

def test_searchbox_add():
    s = Slider(value=1, label='To what extend you agree', min=0, max=10, step=1, 
        show_value=True, value_format='current_value is {value}', vertical=True, height=200)
    assert isinstance(s, pglet.Control)
    assert isinstance(s, pglet.Slider)
    assert s.get_cmd_str() == ('slider height="200" label="To what extend you agree" max="10.0" min="0.0" showValue="true" '
    'step="1.0" value="1.0" valueFormat="current_value is {value}" vertical="true"'), "Test failed"