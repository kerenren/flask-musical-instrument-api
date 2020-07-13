from model.MusicalInstrument import MusicalInstrument


class StringInstrument(MusicalInstrument):
    def __init__(self, num_of_strings, range_per_string, color, dimensions, name, manufacturer, model):
        super().__init__(color, dimensions, name, manufacturer, model)
        self._num_of_strings = num_of_strings
        self._range_per_string = range_per_string

    def play(self):
        print("String sound")

    def __str__(self):
        return str.format("StringInstrument: {}, num_of_strings={}, range_per_string={}", super().__str__(),
                          self._num_of_strings, self._range_per_string)

    def __len__(self):
        return len(self.num_of_strings)

    @classmethod
    def from_string(cls, name, manufacturer, model):
        if model == "Pro" and manufacturer == "Wittner":
            return cls(num_of_strings=4, range_per_string='5 octaves', color='brown', dimensions=[4, 2], name=name,
                       manufacturer=manufacturer, model=model)

