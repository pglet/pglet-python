from .control import Control

# Column
class Column(Control):
    def __init__(self, id=None, name=None, icon=None, icon_only=None, 
        field_name=None, sortable=None, sort_field=None, sorted=None, resizable=None,
        min_width=None, max_width=None, on_click=None, template_controls=None,
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

        self.__template_controls = []
        if template_controls != None:
            for control in template_controls:
                self.__template_controls.append(control)

    def _get_control_name(self):
        return "column"
    
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
        return self._get_attr("on_click")

    @on_click.setter
    def on_click(self, value):
        assert value == None or isinstance(value, bool), "resizable must be a boolean"
        self._set_attr("on_click", value)

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

        if value == None:
            return

        orig_val = self._get_attr(name)
        if orig_val != None and isinstance(orig_val, bool):
            value = str(value).lower() == "true"
        elif orig_val != None and isinstance(orig_val, float):
            value = float(str(value))

        self._set_attr_internal(name, value, dirty=False)
        setattr(self.__obj, name, value)

    def _fetch_attrs(self):
        # reflection
        for name, val in vars(self.__obj).items():
            data_type = "string"
            if isinstance(val, bool):
                data_type = "bool"
            elif isinstance(val, float):
                data_type = "float"
            orig_val = self._get_attr(name, data_type=data_type)

            if val != orig_val:
                self._set_attr_internal(name, val, dirty=True)

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
    
        self.__map = {}
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
                item = self.__map.get(obj)
                if item == None:
                    item = Item(obj)
                    self.__map[obj] = item
                item._fetch_attrs()
                items.append(item)
        
        del_objs = []
        for obj, item in self.__map.items():
            if item not in items:
                del_objs.append(obj)

        for obj in del_objs:
            del self.__map[obj]
                
        return items

class Grid(Control):
    def __init__(self, id=None, selection_mode=None, compact=None, header_visible=None, shimmer_lines=None,
            preserve_selection=None,
            columns=None, items=None, on_select=None, onitem_invoke=None,
            width=None, height=None, padding=None, margin=None, visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.selection_mode = selection_mode
        self.compact = compact
        self.header_visible = header_visible
        self.shimmer_lines = shimmer_lines
        self.preserve_selection = preserve_selection
        self._on_select_handler = None
        self.on_select = on_select
        self.onitem_invoke = onitem_invoke
        self._columns = Columns(columns=columns)
        self._items = Items(items=items)
        self._selected_items = []
        
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
    
    # on_select
    @property
    def on_select(self):
        return self._on_select_handler

    @on_select.setter
    def on_select(self, handler):
        self._on_select_handler = handler
        if handler != None:
            self._add_event_handler("select", self._on_select_internal)
        else:
            self._add_event_handler("select", None)

    # selected_items
    @property
    def selected_items(self):
        return self._selected_items

    @selected_items.setter
    def selected_items(self, value):
        self._selected_items = value
        indices = []
        for selected_item in value:
            idx = 0
            for item in self._items.items:
                if item == selected_item:
                   indices.append(str(idx))
                idx += 1
        self._set_attr("selectedindices", ' '.join(indices))  

    # onitem_invoke
    @property
    def onitem_invoke(self):
        return self._get_event_handler("itemInvoke")

    @onitem_invoke.setter
    def onitem_invoke(self, handler):
        self._add_event_handler("itemInvoke", handler)

    # selection_mode
    @property
    def selection_mode(self):
        return self._get_attr("selection")

    @selection_mode.setter
    def selection_mode(self, value):
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
        assert value == None or isinstance(value, bool), "header_visible must be a boolean"
        self._set_attr("headerVisible", value)

    # preserve_selection
    @property
    def preserve_selection(self):
        return self._get_attr("preserveSelection")

    @preserve_selection.setter
    def preserve_selection(self, value):
        assert value == None or isinstance(value, bool), "preserve_selection must be a boolean"
        self._set_attr("preserveSelection", value)

    # shimmer_lines
    @property
    def shimmer_lines(self):
        return self._get_attr("shimmerLines")

    @shimmer_lines.setter
    def shimmer_lines(self, value):
        assert value == None or isinstance(value, int), "shimmerLines must be an int"
        self._set_attr("shimmerLines", value)

    def _on_select_internal(self, e):

        self._selected_items = []
        for id in e.data.split(' '):
            if id != "":
                self._selected_items.append(self.page.get_control(id).obj)

        if self._on_select_handler != None:
            self._on_select_handler(e)

    def _get_children(self):
        result=[]
        result.append(self._columns)
        result.append(self._items)
        return result