import json


class JsonModel(object):

    required_attributes = []
    optional_attributes = []

    def __init__(self, params=None):
        self.initialize()
        if params is not None and not isinstance(params, dict):
            raise AttributeError("Params must be a dict to initialize starting values or "
                                 "if it's empty")
        self._set_values(params)

    def to_json(self):
        not_parsed = dict()
        for attribute in self.get_attributes():
            not_parsed[attribute] = self.__getattribute__(attribute)
        return not_parsed

    def get_attributes(self):
        return list(vars(self).keys())

    def get_static_members(self):
        static_members = []
        for member in dir(self):
            if not callable(getattr(self, member)) \
                    and not member.startswith("_") \
                    and self.get_attributes().count(member) == 0:
                static_members.append(member)
        return static_members

    def initialize(self):
        attributes = self.__class__.required_attributes + self.__class__.optional_attributes
        if len(self.__class__.required_attributes) == 0:
            raise NotImplementedError("You need at least 1 required attribute in {}.required_attributes list"
                                      .format(self.__class__.__name__))
        for attribute in attributes:
            self.__setattr__(attribute, None)

    def update(self, properties: dict):
        pass

    def save(self):
        name = self.__class__.__name__.lower() + 's'
        db_name = name + '.json'
        objects = self.__class__.all()
        objects.append(self)
        jsoned = {name:[]}
        for obj in objects:
            jsoned[name].append(obj.to_json())
        print(jsoned)
        with open('resources/{}'.format(db_name), 'w') as db:
            json.dump(jsoned, db)

    def _set_values(self, params: dict):
        attributes = self.__class__.required_attributes + self.__class__.optional_attributes
        for attribute in attributes:
            if params is None:
                self.__setattr__(attribute, None)
            else:
                self.__setattr__(attribute, params[attribute])

    @classmethod
    def all(cls):
        name = cls.__name__.lower() + 's'
        db_name = name + '.json'
        with open('resources/{}'.format(db_name)) as db:
            data = json.load(db)
            objects_list = []
            for elem in data[name]:
                o = cls()
                o._set_values(elem)
                objects_list.append(o)
            return objects_list

    @classmethod
    def new(cls, params=None):
        o = cls()
        o._set_values(params)
        return o

    @classmethod
    def create(cls, params: dict):
        o = cls()
        o._set_values(params)
        cls.all().append(o)
        return o

    @classmethod
    def find(cls, attributes: list, values: list):
        pass

    @classmethod
    def find_all(cls, attributes: list, values: list):
        pass

    @classmethod
    def delete(cls, attributes: list, values: list):
        pass

    @classmethod
    def delete_all(cls, attributes: list, values: list):
        pass

    @classmethod
    def destroy(cls, attributes: list, values: list):
        pass

    @classmethod
    def destroy_all(cls, attributes: list, values: list):
        pass






