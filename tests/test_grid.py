import pglet
from pglet import Grid, Column

class Contact():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

def test_grid_add():
    g = Grid(selection_mode='multiple', compact=True, header_visible=True, shimmer_lines=1, columns=[
        Column(field_name="first_name", name='First name', icon='mail', icon_only=True,
        sortable='True', sort_field='sort field name', sorted='false', resizable=False, min_width=100, max_width=200),
        Column(field_name="last_name", name='Last name')
    ], items=[
        Contact(first_name='Inesa', last_name='Fitsner'),
        Contact(first_name='Fiodar', last_name='Fitsner')
    ])


    assert isinstance(g, pglet.Control)
    assert isinstance(g, pglet.Grid)
    assert g.get_cmd_str() == (
        'grid compact="true" headervisible="true" selection="multiple" shimmerlines="1"\n'
        '  columns\n'
        '    column fieldname="first_name" icon="mail" icononly="true" maxwidth="200" minwidth="100" name="First name" resizable="false" sortable="True" sorted="false" sortfield="sort field name"\n'
        '    column fieldname="last_name" name="Last name"\n'
        '  items\n'
        '    item first_name="Inesa" last_name="Fitsner"\n'
        '    item first_name="Fiodar" last_name="Fitsner"'
    ), "Test failed"