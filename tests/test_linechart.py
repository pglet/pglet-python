import pglet
from pglet import LineChart
from pglet.linechart import P


def test_verticalbarchart_add():
    lc = LineChart(legend=True, tooltips=True, stroke_width=4, y_min=0, y_max=100, y_ticks=2, y_format='{y}%', 
                x_type='number', data=[
                    P(x=1, y=100),
                    P(x=5, y=50)
                ])
    assert isinstance(lc, pglet.Control)
    assert isinstance(lc, pglet.LineChart)
    assert lc.get_cmd_str() == (
        'linechart legend="true" strokeWidth="4" tooltips="true" xType="number" yFormat="{y}%" '
        'yMax="100" yMin="0" yTicks="2"\n'
        '  data\n'
        '    p x="1" y="100"\n'
        '    p x="5" y="50"'
    ), "Test failed"