from pprint import pprint
models = {}

class ModelMetaclass(type):
    def __new__(meta, name, bases, attrs):
        models[name] = cls = type.__new__(meta, name, bases, attrs)
        return cls

class Model(object):
    __metaclass__ = ModelMetaclass

class A(Model): pass
class B1(A): pass
class B2(A): pass
class B3(A): pass
class C(B1): pass

pprint(models)