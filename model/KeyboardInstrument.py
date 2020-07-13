from model.MusicalInstrument import MusicalInstrument


class KeyboardInstrument(MusicalInstrument):
    def __init__(self, num_of_keys, pitch_per_key, color, dimensions, name, manufacturer, model):
        super(KeyboardInstrument, self).__init__(color, dimensions, name, manufacturer, model)
        self._num_of_keys = num_of_keys
        self._pitch_per_key = pitch_per_key

    def play(self):
        print("keyboard sound")

    def __str__(self):
        return str.format("{}, KeyboardInstrument: num_of_keys={}, pitch_per_key={}", super().__str__(),
                          self._num_of_keys, self._pitch_per_key)

    def __len__(self):
        return len(self.num_of_keys)
