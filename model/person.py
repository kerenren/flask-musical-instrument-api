
class Person:
    def __init__(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return str.format("Person: first_name={}, last_name={}, email={}",
                          self._first_name, self._last_name, self._email)

    def get_email(self):
        return self._email

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name
