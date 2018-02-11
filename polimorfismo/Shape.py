from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def get_area(self):
        pass
