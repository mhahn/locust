from copy import deepcopy


class Blueprint(object):

    def __init__(self, data):
        self._data = data

    def __getattr__(self, name):
        try:
            value = self._data[name]
        except TypeError:
            if name.startswith('_') and name[-1].isdigit():
                value = self._data[int(name[1:])]
            else:
                raise
        except Exception:
            value = super(Blueprint, self).__getattribute__(name)

        if isinstance(value, dict) or isinstance(value, list):
            value = Blueprint(value)
        return value

    def update(self, value):
        data = super(Blueprint, self).__getattribute__('_data')
        data.update(value)

    def clone(self):
        return Blueprint(deepcopy(self._data))
