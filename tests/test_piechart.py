import pglet
from pglet import PieChart
from pglet.piechart import P


def test_piechart_add():
    pc = PieChart(legend=True, tooltips=True, inner_value=40, inner_radius=42, width='100%', points=[
                    P(value=20, color='yellow', legend='Yellow color', tooltip='20%'),
                    P(value=30, color='green', legend='Green color', tooltip='30%')])

    assert isinstance(pc, pglet.Control)
    assert isinstance(pc, pglet.PieChart)
    assert pc.get_cmd_str() == (
        'piechart innerRadius="42" innerValue="40" legend="true" tooltips="true" width="100%"\n'
        '  data\n'
        '    p color="yellow" legend="Yellow color" tooltip="20%" value="20"\n'
        '    p color="green" legend="Green color" tooltip="30%" value="30"'
    ), "Test failed"