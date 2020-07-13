
class Band:
    def __init__(self, musicians={}):
        self._musicians = musicians

    def add_musician(self, musician):
        if musician is None:
            raise ValueError("Missing required musician instance!")

        if musician.get_email() in self._musicians.keys():
            raise ValueError("Email already exists!")

        self._musicians[musician.get_email()] = musician
        print(self)

    def add_instrument(self, musician_email, instrument):
        if musician_email not in self._musicians.keys():
            raise ValueError("Musician does not exist!")

        self._musicians[musician_email].add_instrument(instrument)
        print(self)

    def remove_instrument(self, name, manufacturer, model, musician_email):
        if musician_email not in self._musicians.keys():
            raise ValueError("Musician does not exist!")

        musician = self._musicians[musician_email]
        for inst in musician.get_instruments():
            if inst.get_name() == name and inst.get_manufacturer() == manufacturer \
                    and inst.get_model() == model:
                musician.get_instruments().remove(inst)
            break

        print(self)

    def __str__(self):
        band = "The band's musicians & instruments:\n"
        for musician in self._musicians.values():
            band += musician.__str__()
            band += "\n"

        return band

    @property
    def musicians(self):
        return self._musicians
