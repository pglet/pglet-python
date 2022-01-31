from pglet.control import Control

# Point
class Point(Control):
    def __init__(self, id=None, value=None, legend=None, color=None, tooltip=None):
        Control.__init__(self, id=id)

        self.value = value
        self.legend = legend
        self.color = color
        self.tooltip = tooltip

    def _get_control_name(self):
        return "p"

    # value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        assert (
            value == None or isinstance(value, float) or isinstance(value, int)
        ), "value must be a float"
        self._set_attr("value", value)

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

    # tooltip
    @property
    def tooltip(self):
        return self._get_attr("tooltip")

    @tooltip.setter
    def tooltip(self, value):
        self._set_attr("tooltip", value)


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


class PieChart(Control):
    def __init__(
        self,
        id=None,
        legend=None,
        tooltips=None,
        inner_value=None,
        inner_radius=None,
        points=None,
        width=None,
        height=None,
        padding=None,
        margin=None,
        visible=None,
        disabled=None,
    ):

        Control.__init__(
            self,
            id=id,
            width=width,
            height=height,
            padding=padding,
            margin=margin,
            visible=visible,
            disabled=disabled,
        )

        self.__data = Data(points=points)
        self.legend = legend
        self.tooltips = tooltips
        self.inner_value = inner_value
        self.inner_radius = inner_radius

    def _get_control_name(self):
        return "piechart"

    # data
    @property
    def points(self):
        return self.__data.points

    @points.setter
    def points(self, value):
        self.__data.points = value

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

    # inner_value
    @property
    def inner_value(self):
        return self._get_attr("innerValue")

    @inner_value.setter
    def inner_value(self, value):
        self._set_attr("innerValue", value)

    # inner_radius
    @property
    def inner_radius(self):
        return self._get_attr("innerRadius")

    @inner_radius.setter
    def inner_radius(self, value):
        assert (
            value == None or isinstance(value, float) or isinstance(value, int)
        ), "inner_radius must be a float"
        self._set_attr("innerRadius", value)

    def _get_children(self):
        return [self.__data]
