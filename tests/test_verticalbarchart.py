import pglet
from pglet import VerticalBarChart
from pglet.verticalbarchart import Point


def test_verticalbarchart_add():
    vbc = VerticalBarChart(legend=True, tooltips=False, bar_width=56, 
        colors='green yellow', y_min=0, y_max=1000, y_ticks=200, y_format='format{y}',
        x_type='number', points=[
        Point(x='1', y=100, legend='legend', color='green', x_tooltip='x tooltip', y_tooltip='y tooltip'),
        Point(x='80', y=200), 
        Point(x='100', y=300),
    ])
    assert isinstance(vbc, pglet.Control)
    assert isinstance(vbc, pglet.VerticalBarChart)
    assert vbc.get_cmd_str() == (
        'verticalbarchart barWidth="56" colors="green yellow" legend="true" tooltips="false" '
        'xType="number" yFormat="format{y}" yMax="1000" yMin="0" yTicks="200"\n'
        '  data\n'
        '    p color="green" legend="legend" x="1" xTooltip="x tooltip" y="100" yTooltip="y tooltip"\n'
        '    p x="80" y="200"\n'
        '    p x="100" y="300"'
    ), "Test failed"