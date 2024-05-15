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
    def list_dicts(cls, query={}):
        languages = cls._collection.find(query)
        return [LanguageModel(language).to_dict() for language in languages]
