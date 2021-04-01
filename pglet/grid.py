from .utils import encode_attr
from .control import Control

# Column
class Column(Control):
    def __init__(self, id=None, name=None, icon=None, icon_only=None, 
        field_name=None, sortable=None, sort_field=None, sorted=None, resizable=None,
        min_width=None, max_width=None, on_click=None, template_controls=None, onclick=None,
        new_window=None, expanded=None):
        Control.__init__(self, id=id)

        self.name = name
        self.icon = icon
        self.icon_only = icon_only
        self.field_name = field_name
        self.sortable = sortable
        self.sort_field = sort_field
        self.sorted = sorted
        self.resizable = resizable
        self.min_width = min_width
        self.max_width = max_width
        self.on_click = on_click
        #self.onchange = onchange

        self.__template_controls = []
        if template_controls != None:
            for control in template_controls:
                self.__template_controls.append(control)

    def _get_control_name(self):
        return "column"

    # onclick
    @property
    def onclick(self):
        return self._get_event_handler("click")

    @onclick.setter
    def onclick(self, handler):
        self._add_event_handler("click", handler)
    
    # template_controls
    @property
    def template_controls(self):
        return self.__template_controls

    @template_controls.setter
    def template_controls(self, value):
        self.__template_controls = value

    # name
    @property
    def name(self):
        return self._get_attr("name")

    @name.setter
    def name(self, value):
        self._set_attr("name", value)

    # icon
    @property
    def icon(self):
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value):
        self._set_attr("icon", value)

    # icon_only
    @property
    def icon_only(self):
        return self._get_attr("iconOnly")

    @icon_only.setter
    def icon_only(self, value):
        assert value == None or isinstance(value, bool), "iconOnly must be a boolean"
        self._set_attr("iconOnly", value)

    # field_name
    @property
    def field_name(self):
        return self._get_attr("fieldName")

    @field_name.setter
    def field_name(self, value):
        self._set_attr("fieldName", value)

    # sortable
    @property
    def sortable(self):
        return self._get_attr("sortable")

    @sortable.setter
    def sortable(self, value):
        self._set_attr("sortable", value)

    # sort_field
    @property
    def sort_field(self):
        return self._get_attr("sortField")

    @sort_field.setter
    def sort_field(self, value):
        self._set_attr("sortField", value)

    # sorted
    @property
    def sorted(self):
        return self._get_attr("sorted")

    @sorted.setter
    def sorted(self, value):
        self._set_attr("sorted", value)

    # resizable
    @property
    def resizable(self):
        return self._get_attr("resizable")

    @resizable.setter
    def resizable(self, value):
        assert value == None or isinstance(value, bool), "resizable must be a boolean"
        self._set_attr("resizable", value)

    # min_width
    @property
    def min_width(self):
        return self._get_attr("minWidth")

    @min_width.setter
    def min_width(self, value):
        assert value == None or isinstance(value, int), "minWidth must be an int"
        self._set_attr("minWidth", value)
    
    
    # max_width
    @property
    def max_width(self):
        return self._get_attr("maxWidth")

    @max_width.setter
    def max_width(self, value):
        assert value == None or isinstance(value, int), "maxWidth must be an int"
        self._set_attr("maxWidth", value)

    # on_click
    @property
    def on_click(self):
        return self._get_attr("onClick")

    @on_click.setter
    def on_click(self, value):
        assert value == None or isinstance(value, bool), "resizable must be a boolean"
        self._set_attr("onClick", value)

    def _get_children(self):
        return self.__template_controls

# Item
class Item(Control):
    def __init__(self, obj):
        Control.__init__(self)
        assert obj != None, "Obj cannot be empty"
        self.__obj = obj

    @property
    def obj(self):
        return self.__obj

    def _set_attr(self, name, value, dirty=True):
        self._Control__set_attr(name, value, dirty=False)

        print("grid item set:", name, value)

    def _fetch_attrs(self):
        # reflection
        for property, val in vars(self.__obj).items():
            data_type = "string"
            if isinstance(val, bool):
                data_type = "bool"
            elif isinstance(val, float):
                data_type = "float"
            origVal = self._get_attr(property, data_type=data_type)

            if val != origVal:
                self._Control__set_attr(property, val, dirty=True)

    def _get_control_name(self):
        return "item"

# Columns
class Columns(Control):
    def __init__(self, id=None, columns=None):
        Control.__init__(self, id=id)
    
        self.__columns = []
        if columns != None:
            for column in columns:
                self.__columns.append(column)

    # columns
    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        self.__columns = value

    def _get_control_name(self):
        return "columns"

    def _get_children(self):
        return self.__columns

# Items
class Items(Control):
    def __init__(self, id=None, items=None):
        Control.__init__(self, id=None)
    
        self.__items = []
        if items != None:
            for item in items:
                self.__items.append(item)

    # items
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    def _get_control_name(self):
        return "items"

    def _get_children(self):
        items = []
        if self.__items and len(self.__items) > 0:
            for obj in self.__items:
                item = Item(obj)
                item._fetch_attrs()
                items.append(item)
                
        return items

class Grid(Control):
    def __init__(self, id=None, selection=None, compact=None, header_visible=None, shimmer_lines=None,
            columns=None, items=None, onselect=None, onitem_invoke=None,
            width=None, height=None, padding=None, margin=None, visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.selection = selection
        self.compact = compact
        self.header_visible = header_visible
        self.shimmer_lines = shimmer_lines
        self.onselect = onselect
        self.onitem_invoke = onitem_invoke
        self._columns = Columns(columns=columns)
        self._items = Items(items=items)
        
    def _get_control_name(self):
        return "grid"

    # columns
    @property
    def columns(self):
        return self._columns.columns

    @columns.setter
    def columns(self, value):
        self._columns.columns = value

    # items
    @property
    def items(self):
        return self._items.items

    @items.setter
    def items(self, value):
        self._items.items = value
    
    # onselect
    @property
    def onselect(self):
        return self._get_event_handler("select")

    @onselect.setter
    def onselect(self, handler):
        self._add_event_handler("select", handler)

    # onitem_invoke
    @property
    def onitem_invoke(self):
        return self._get_event_handler("itemInvoke")

    @onitem_invoke.setter
    def onitem_invoke(self, handler):
        self._add_event_handler("itemInvoke", handler)

    # selection
    @property
    def selection(self):
        return self._get_attr("selection")

    @selection.setter
    def selection(self, value):
        self._set_attr("selection", value)

    # compact
    @property
    def compact(self):
        return self._get_attr("compact")

    @compact.setter
    def compact(self, value):
        assert value == None or isinstance(value, bool), "compact must be a boolean"
        self._set_attr("compact", value)

    # header_visible
    @property
    def header_visible(self):
        return self._get_attr("headerVisible")

    @header_visible.setter
    def header_visible(self, value):
        assert value == None or isinstance(value, bool), "headerVisible must be a boolean"
        self._set_attr("headerVisible", value)

    # shimmer_lines
    @property
    def shimmer_lines(self):
        return self._get_attr("shimmerLines")

    @shimmer_lines.setter
    def shimmer_lines(self, value):
        assert value == None or isinstance(value, int), "shimmerLines must be an int"
        self._set_attr("shimmerLines", value)

    def _get_children(self):
        result=[]
        result.append(self._columns)
        result.append(self._items)
        return result