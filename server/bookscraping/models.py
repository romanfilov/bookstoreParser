from django.db import models
from abc import ABC, abstractmethod
# Create your models here.


class Book:
    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


class BaseStore(ABC):
    def __init__(self, url, name):
        self.url = url
        self.name = name

    @abstractmethod
    def parse(self):
        pass


class YakabooStore(BaseStore):
    def parse(self):
        return 'Yakaboo'


class BookClubStore(BaseStore):
    def parse(self):
        return 'BookClub'


class BookYeStore(BaseStore):
    def parse(self):
        return 'BookClub'
