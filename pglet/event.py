class Event:
    target = ""
    name = ""
    data = None

    def __init__(self, target, name, data):
        self.target = target
        self.name = name
        self.data = data