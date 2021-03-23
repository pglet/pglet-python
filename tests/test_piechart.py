import pglet
from pglet import PieChart
from pglet.piechart import P


def test_piechart_add():
    pc = PieChart(legend=True, tooltips=True, inner_value=40, inner_radius=42, width='100%', data=[
                    piechart.P(value=20, color='yellow', legend='Yellow color', tooltip='20%'),
                    piechart.P(value=30, color='green', legend='Green color', tooltip='30%')])

    assert isinstance(pc, pglet.Control)
    assert isinstance(pc, pglet.PieChart)
    assert pc.get_cmd_str() == (
        'verticalbarchart colors="green yellow" tooltips="false" '
        'xType="number" yFormat="format{y}" yMax="1000" yMin="0" yTicks="200"\n'
        '  data\n'
        '    p color="green" legend="legend" x="1" xTooltip="x tooltip" y="100" yTooltip="y tooltip"\n'
        '    p x="80" y="200"\n'
        '    p x="100" y="300"'
    ), "Test failed"