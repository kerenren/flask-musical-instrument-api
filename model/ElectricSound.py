
class ElectricSound:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    def get_name(self):
        return self._name

    def get_sound(self):
        return self._sound

    def __str__(self):
        return str.format("name:{}, sound:{}", self._name, self._sound)

