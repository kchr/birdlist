from mongoengine import *

import datetime


class Bird(Document):

    __required = ['name', 'family', 'continents']

    __date_format = '%Y-%m-%d'

    name = StringField(required=True)
    family = StringField(required=True)
    continents = ListField(required=True)
    added = DateTimeField(default=datetime.datetime.now)
    visible = BooleanField(default=False)

    """ pre-save validation """
    def clean(self):

        # verify required fields
        missing = []
        for field in self.__required:
            if field not in self:
                missing.append(field)
            elif not self[field]:
                missing.append(field)
        if missing:
            raise ValueError("Missing required property: %s" %
                             ", ".join(missing))

        # check for dupes in continent list
        continents = []
        for c in self.continents:
            if c in continents:
                raise ValueError("Continents must be unique")
            continents.append(c)

        return True

    def get_id(self):
        return str(self.pk)

    def get_date(self):
        return self.added.strftime(self.__date_format)
