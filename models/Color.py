from models.JsonModel import JsonModel


class Color(JsonModel):

    required_attributes = ['name', 'red', 'green', 'blue']

    def __init__(self, params=None):
        super().__init__(params)


c = Color({"name": "Olive", "red": 128, "green": 128, "blue": 0})
c.save()
