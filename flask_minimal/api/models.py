from flask.ext.restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger


@swagger.model
class DummyResult(object):
    """The result of a call to /test"""
    resource_fields = {
        'test': fields.String
    }

    def __init__(self):
        self.test = "😃"


@swagger.model
class HelloResult(object):
    """The result of a call to /hello"""
    resource_fields = {
        'greetings': fields.String
    }

    def __init__(self, name):
        self.greetings = "Hello {}".format(name)
