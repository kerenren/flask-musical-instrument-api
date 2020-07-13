
class MusicalInstrument:
    def __init__(self, color, dimensions, name, manufacturer, model):
        self._color = color
        self._dimensions = dimensions
        self._name = name
        self._manufacturer = manufacturer
        self._model = model

    def play(self):
        pass

    def get_model(self):
        return self._model

    def get_manufacturer(self):
        return self._manufacturer

    def get_name(self):
        return self._name

    def set_model(self, model):
        self._model = model

    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return str.format("Musical Instrument: name={}, color={}, dimensions={}, manufacturer={}, model={}", self._name,
                          self._color, self._dimensions, self._manufacturer, self._model)

