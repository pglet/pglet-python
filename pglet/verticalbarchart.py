from .utils import encode_attr
from .control import Control

# P
class P(Control):
    def __init__(self, id=None, x=None, y=None, legend=None, color=None,
        x_tooltip=None, y_tooltip=None):
        Control.__init__(self, id=id)

        self.x = x
        self.y = y
        self.legend = legend
        self.color = color
        self.x_tooltip = x_tooltip
        self.y_tooltip = y_tooltip

    def _getControlName(self):
        return "p"

    # x
    @property
    def x(self):
        return self._get_attr("x")

    @x.setter
    def x(self, value):
        self._set_attr("x", value)

    # y
    @property
    def y(self):
        return self._get_attr("y")

    @y.setter
    def y(self, value):
        self._set_attr("y", value)

    # legend
    @property
    def legend(self):
        return self._get_attr("legend")

    @legend.setter
    def legend(self, value):
        self._set_attr("legend", value)

    # color
    @property
    def color(self):
        return self._get_attr("color")

    @color.setter
    def color(self, value):
        self._set_attr("color", value)

    # x_tooltip
    @property
    def x_tooltip(self):
        return self._get_attr("xTooltip")

    @x_tooltip.setter
    def x_tooltip(self, value):
        self._set_attr("xTooltip", value)

    # y_tooltip
    @property
    def y_tooltip(self):
        return self._get_attr("yTooltip")

    @y_tooltip.setter
    def y_tooltip(self, value):
        self._set_attr("yTooltip", value)

# Data
class Data(Control):
    def __init__(self, id=None, points=[]):
        Control.__init__(self, id=None)
    
        self._points = []
        if points and len(points) > 0:
            for point in points:
                self.add_point(point)

    # points
    @property
    def points(self):
        return self._points

    def _getControlName(self):
        return "data"

    def add_point(self, point):
        assert isinstance(point, P), ("data can hold points only")
        self._points.append(point)

    def _getChildren(self):
        return self._points


class VerticalBarChart(Control):
    def __init__(self, id=None, legend=None, tooltips=None, bar_width=None, colors=None, 
            y_min=None, y_max=None, y_ticks=None, y_format=None, x_type=None, data=[],
            width=None, height=None, padding=None, margin=None, visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self._data = Data(points=data)
        
    def _getControlName(self):
        return "verticalbarchart"

    # data
    @property
    def data(self):
        return self._data

    
    # legend
    @property
    def legend(self):
        return self._get_attr("legend")

    @legend.setter
    def legend(self, value):
        assert value == None or isinstance(value, bool), "legend must be a boolean"
        self._set_attr("legend", value)

    # tooltips
    @property
    def tooltips(self):
        return self._get_attr("tooltips")

    @tooltips.setter
    def tooltips(self, value):
        assert value == None or isinstance(value, bool), "tooltips must be a boolean"
        self._set_attr("tooltips", value)

    # colors
    @property
    def colors(self):
        return self._get_attr("colors")

    @colors.setter
    def colors(self, value):
        self._set_attr("colors", value)

    # yMin
    @property
    def y_min(self):
        return self._get_attr("yMin")

    @y_min.setter
    def y_min(self, value):
        self._set_attr("yMin", value)

    # yMax
    @property
    def y_max(self):
        return self._get_attr("yMax")

    @y_max.setter
    def y_max(self, value):
        self._set_attr("yMax", value)

    # yTicks
    @property
    def y_ticks(self):
        return self._get_attr("yTicks")

    @y_ticks.setter
    def y_ticks(self, value):
        assert value == None or isinstance(value, int), "yTicks must be an int"
        self._set_attr("yTicks", value)

    # yFormat
    @property
    def y_format(self):
        return self._get_attr("yFormat")

    @y_format.setter
    def y_format(self, value):
        self._set_attr("yFormat", value)

    # xType
    @property
    def x_type(self):
        return self._get_attr("xType")

    @x_type.setter
    def x_type(self, value):
        self._set_attr("xType", value)

    def _getChildren(self):
        return [self._data]