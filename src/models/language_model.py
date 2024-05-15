from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        return {
            'name': self.data.get('name'),
            'acronym': self.data.get('acronym')
        }

    @classmethod
    def get_languages(cls, query: dict = {}):
        languages = cls._collection.find(query)
        return [cls(language) for language in languages]
