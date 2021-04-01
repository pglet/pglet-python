import pglet
from pglet import LineChart
from pglet.linechart import P, Data


def test_verticalbarchart_add():
    lc = LineChart(legend=True, tooltips=True, stroke_width=4, y_min=0, y_max=100, y_ticks=2, y_format='{y}%', 
                x_type='number', lines=[
                    Data(color='yellow', legend='yellow color', points=[
                        P(x=1, y=100),
                        P(x=5, y=50)]),
                    Data(color='green', legend='green color', points=[
                        P(x=10, y=20),
                        P(x=20, y=10)])
                ])
    assert isinstance(lc, pglet.Control)
    assert isinstance(lc, pglet.LineChart)
    assert lc.get_cmd_str() == (
        'linechart legend="true" strokeWidth="4" tooltips="true" xType="number" '
        'yFormat="{y}%" yMax="100" yMin="0" yTicks="2"\n'
        '  data color="yellow" legend="yellow color"\n'
        '    p x="1" y="100"\n'
        '    p x="5" y="50"\n'
        '  data color="green" legend="green color"\n'
        '    p x="10" y="20"\n'
        '    p x="20" y="10"'
    ), "Test failed"