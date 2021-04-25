import pglet
from pglet import BarChart
from pglet.barchart import Point


def test_barchart_add():
    bc = BarChart(data_mode='default', tooltips=False, points=[
        Point(x=1, y=100, legend='legend', color='green', x_tooltip='x tooltip', y_tooltip='y tooltip'),
        Point(x=80, y=200), 
        Point(x=100, y=300),
    ])
    assert isinstance(bc, pglet.Control)
    assert isinstance(bc, pglet.BarChart)
    assert bc.get_cmd_str() == (
        'barchart dataMode="default" tooltips="false"\n'
        '  data\n'
        '    p color="green" legend="legend" x="1" xTooltip="x tooltip" y="100" yTooltip="y tooltip"\n'
        '    p x="80" y="200"\n'
        '    p x="100" y="300"'
    ), "Test failed"