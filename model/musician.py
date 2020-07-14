from model.person import Person


class Musician(Person):
    def __init__(self, first_name, last_name, email, instruments=[]):
        super().__init__(first_name, last_name, email)
        self._instruments = instruments

    def __str__(self):
        instruments = ''
        for inst in self._instruments:
            instruments += inst.__str__()

        if len(instruments) == 0:
            instruments = 'None'

        return str.format("Musician: {}, instruments={}", super().__str__(),
                          instruments)

    def get_instruments(self):
        return self._instruments

    def add_instrument(self, instrument):
        self._instruments.append(instrument)

    @classmethod
    def from_string(cls, first_name, last_name, email):
        instruments = []
        return cls(first_name, last_name, email, instruments)

# musician = Musician("joe","doe","email",instruments=["guitar","piano"])
# instr = musician.get_instruments()
# # print(instr)
# # print(musician.__str__())
# print(musician._instruments.__str__())
# for inst in musician._instruments:
#     print(inst.__str__())
#     # inst.__str__()