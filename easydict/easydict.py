from typing import *


class EasyDict:
    def __init__(self, default: Optional[dict] = {}, **kwargs):
        self.__dict__.update(default)
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        if 'normalize' in self.__dict__.keys():
            if self.__dict__.get('normalize') is True:
                item = item.replace('_', ' ')

        if item in self.__dict__.keys():
            return self.__dict__.get(item)

        raise AttributeError

    def __getitem__(self, item):
        if item in self.__dict__.keys():
            return self.__dict__.get(item)

        raise AttributeError

    def __setattr__(self, key, value):
        self.__dict__.update({key.replace('_', ' '): value})

    def __setitem__(self, key, value):
        self.__dict__.update({key.replace('_', ' '): value})

    def __eq__(self, other):
        print(other.__dict__, self.__dict__)
        if isinstance(other, EasyDict):
            return other.__dict__ == self.__dict__

    def get(self, key, default=None):
        if self.__dict__.get(key):
            return self.__dict__.get(key)

        if default is not None:
            return default
