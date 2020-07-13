from model.ElectricInstrument import ElectricInstrument
from model.ElectricSound import ElectricSound
from model.KeyboardInstrument import KeyboardInstrument


class ElectricPiano(KeyboardInstrument, ElectricInstrument):
    def __init__(self, num_of_keys, pitch_per_key, color, dimensions, name, manufacturer, model,
                 sounds_bank, operating_volt, earphone_plug_type, has_speakers):
        KeyboardInstrument.__init__(self, color=color, dimensions=dimensions, name=name, num_of_keys=num_of_keys,
                                    pitch_per_key=pitch_per_key, manufacturer=manufacturer, model=model)

        ElectricInstrument.__init__(self, operating_volt, earphone_plug_type, has_speakers)

        self._sounds_bank = sounds_bank
        self.__current_select_sound = 0

    def play(self):
        if self._sounds_bank[self.__current_select_sound] is not None:
            print(self._sounds_bank.get_sound())

    def __str__(self):
        sounds_str = ''
        for sound in self._sounds_bank:
            sounds_str += str(sound)
            sounds_str += ","

        # remove the last comma ","
        if len(self._sounds_bank) > 0:
            sounds_str = sounds_str[:-1]

        return str.format("ElectricPiano: {}, {}, available-sounds={}, current-sound={}", KeyboardInstrument.__str__(self),
                          ElectricInstrument.__str__(self), sounds_str, self.__current_select_sound)

    @classmethod
    def from_string(cls, name, manufacturer, model):
        if model == "Rhodes" and manufacturer == "Fender":
            electric_piano_sound = ElectricSound("Electric Piano Sound", "Weird electric sound")
            sounds = [electric_piano_sound]

            return cls(num_of_keys=80, pitch_per_key=[], color='red', dimensions=[12, 5], name=name,
                       manufacturer=manufacturer, model=model, sounds_bank=sounds, operating_volt=5,
                       earphone_plug_type="small", has_speakers=True)

        if model == "S90" and manufacturer == "Yamaha":
            orchestra_sound = ElectricSound("Orchestra Sound", "Cool Orchestra sound")
            sounds = [orchestra_sound]

            return cls(num_of_keys=88, pitch_per_key=[], color='black', dimensions=[15, 8], name=name,
                       manufacturer=manufacturer, model=model, sounds_bank=sounds, operating_volt=3,
                       earphone_plug_type="normal", has_speakers=True)
