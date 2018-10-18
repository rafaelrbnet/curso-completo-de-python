from pymongo import MongoClient
from random import randint
import configparser
import os
import sys


class MongoOps:
    _db = ""

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        self._client = MongoClient(config.get("mongodb", "address"))
        self._db = self._client[config.get("mongodb", "base")]

    def get_queue(self):
        queue = self._db.fila.find()
        return queue

    def get_service_to_remove(self):
        return self._db.fila.find({"status": 1})

    def get_service_to_install(self):
        return self._db.fila.find({"status": 0})


if __name__ == "__main__":
    m = MongoOps()
    print(m.get_queue().count())
