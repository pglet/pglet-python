from .control import Control

# Point
class Point(Control):
    def __init__(self, id=None, x=None, y=None, legend=None, color=None,
        x_tooltip=None, y_tooltip=None):
        Control.__init__(self, id=id)

        self.x = x
        self.y = y
        self.legend = legend
        self.color = color
        self.x_tooltip = x_tooltip
        self.y_tooltip = y_tooltip

    def _get_control_name(self):
        return "p"

    # x
    @property
    def x(self):
        return self._get_attr("x")

    @x.setter
    def x(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "x must be a float"  
        self._set_attr("x", value)

    # y
    @property
    def y(self):
        return self._get_attr("y")

    @y.setter
    def y(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "y must be a float"    
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
    def __init__(self, id=None, points=None):
        Control.__init__(self, id=id)
    
        self.__points = []
        if points != None:
            for point in points:
                self.__points.append(point)

    # points
    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value

    def _get_control_name(self):
        return "data"

    def _get_children(self):
        return self.__points


class BarChart(Control):
    def __init__(self, id=None, tooltips=None, data_mode=None, points=None,
            width=None, height=None, padding=None, margin=None, visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self.__data = Data(points=points)
        self.tooltips = tooltips
        self.data_mode = data_mode
        
    def _get_control_name(self):
        return "barchart"

    # points
    @property
    def points(self):
        return self.__data.points

    @points.setter
    def points(self, value):
        self.__data.points = value

    # tooltips
    @property
    def tooltips(self):
        return self._get_attr("tooltips")

    @tooltips.setter
    def tooltips(self, value):
        assert value == None or isinstance(value, bool), "tooltips must be a boolean"
        self._set_attr("tooltips", value)

    # data_mode
    @property
    def data_mode(self):
        return self._get_attr("dataMode")

    @data_mode.setter
    def data_mode(self, value):
        self._set_attr("dataMode", value)

    def _get_children(self):
        return [self.__data]
