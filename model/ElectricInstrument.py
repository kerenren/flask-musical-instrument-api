

class ElectricInstrument:
    def __init__(self, operating_volt, earphone_plug_type, has_speakers):
        super().__init__()
        self._operating_volt = operating_volt
        self._earphone_plug_type = earphone_plug_type
        self._has_speakers = has_speakers

    def __str__(self):
        return str.format("ElectricInstrument: earphone_plug_type={}, has_speakers={}",
                          self._earphone_plug_type, self._has_speakers)
