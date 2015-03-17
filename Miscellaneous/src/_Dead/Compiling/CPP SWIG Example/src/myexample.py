# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_myexample', [dirname(__file__)])
        except ImportError:
            import _myexample
            return _myexample
        if fp is not None:
            try:
                _mod = imp.load_module('_myexample', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _myexample = swig_import_helper()
    del swig_import_helper
else:
    import _myexample
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _myexample.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _myexample.SwigPyIterator_value(self)
    def incr(self, n = 1): return _myexample.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _myexample.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _myexample.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _myexample.SwigPyIterator_equal(self, *args)
    def copy(self): return _myexample.SwigPyIterator_copy(self)
    def next(self): return _myexample.SwigPyIterator_next(self)
    def __next__(self): return _myexample.SwigPyIterator___next__(self)
    def previous(self): return _myexample.SwigPyIterator_previous(self)
    def advance(self, *args): return _myexample.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _myexample.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _myexample.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _myexample.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _myexample.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _myexample.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _myexample.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _myexample.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _myexample.IntVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _myexample.IntVector___nonzero__(self)
    def __bool__(self): return _myexample.IntVector___bool__(self)
    def __len__(self): return _myexample.IntVector___len__(self)
    def pop(self): return _myexample.IntVector_pop(self)
    def __getslice__(self, *args): return _myexample.IntVector___getslice__(self, *args)
    def __setslice__(self, *args): return _myexample.IntVector___setslice__(self, *args)
    def __delslice__(self, *args): return _myexample.IntVector___delslice__(self, *args)
    def __delitem__(self, *args): return _myexample.IntVector___delitem__(self, *args)
    def __getitem__(self, *args): return _myexample.IntVector___getitem__(self, *args)
    def __setitem__(self, *args): return _myexample.IntVector___setitem__(self, *args)
    def append(self, *args): return _myexample.IntVector_append(self, *args)
    def empty(self): return _myexample.IntVector_empty(self)
    def size(self): return _myexample.IntVector_size(self)
    def clear(self): return _myexample.IntVector_clear(self)
    def swap(self, *args): return _myexample.IntVector_swap(self, *args)
    def get_allocator(self): return _myexample.IntVector_get_allocator(self)
    def begin(self): return _myexample.IntVector_begin(self)
    def end(self): return _myexample.IntVector_end(self)
    def rbegin(self): return _myexample.IntVector_rbegin(self)
    def rend(self): return _myexample.IntVector_rend(self)
    def pop_back(self): return _myexample.IntVector_pop_back(self)
    def erase(self, *args): return _myexample.IntVector_erase(self, *args)
    def __init__(self, *args): 
        this = _myexample.new_IntVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _myexample.IntVector_push_back(self, *args)
    def front(self): return _myexample.IntVector_front(self)
    def back(self): return _myexample.IntVector_back(self)
    def assign(self, *args): return _myexample.IntVector_assign(self, *args)
    def resize(self, *args): return _myexample.IntVector_resize(self, *args)
    def insert(self, *args): return _myexample.IntVector_insert(self, *args)
    def reserve(self, *args): return _myexample.IntVector_reserve(self, *args)
    def capacity(self): return _myexample.IntVector_capacity(self)
    __swig_destroy__ = _myexample.delete_IntVector
    __del__ = lambda self : None;
IntVector_swigregister = _myexample.IntVector_swigregister
IntVector_swigregister(IntVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _myexample.DoubleVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _myexample.DoubleVector___nonzero__(self)
    def __bool__(self): return _myexample.DoubleVector___bool__(self)
    def __len__(self): return _myexample.DoubleVector___len__(self)
    def pop(self): return _myexample.DoubleVector_pop(self)
    def __getslice__(self, *args): return _myexample.DoubleVector___getslice__(self, *args)
    def __setslice__(self, *args): return _myexample.DoubleVector___setslice__(self, *args)
    def __delslice__(self, *args): return _myexample.DoubleVector___delslice__(self, *args)
    def __delitem__(self, *args): return _myexample.DoubleVector___delitem__(self, *args)
    def __getitem__(self, *args): return _myexample.DoubleVector___getitem__(self, *args)
    def __setitem__(self, *args): return _myexample.DoubleVector___setitem__(self, *args)
    def append(self, *args): return _myexample.DoubleVector_append(self, *args)
    def empty(self): return _myexample.DoubleVector_empty(self)
    def size(self): return _myexample.DoubleVector_size(self)
    def clear(self): return _myexample.DoubleVector_clear(self)
    def swap(self, *args): return _myexample.DoubleVector_swap(self, *args)
    def get_allocator(self): return _myexample.DoubleVector_get_allocator(self)
    def begin(self): return _myexample.DoubleVector_begin(self)
    def end(self): return _myexample.DoubleVector_end(self)
    def rbegin(self): return _myexample.DoubleVector_rbegin(self)
    def rend(self): return _myexample.DoubleVector_rend(self)
    def pop_back(self): return _myexample.DoubleVector_pop_back(self)
    def erase(self, *args): return _myexample.DoubleVector_erase(self, *args)
    def __init__(self, *args): 
        this = _myexample.new_DoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _myexample.DoubleVector_push_back(self, *args)
    def front(self): return _myexample.DoubleVector_front(self)
    def back(self): return _myexample.DoubleVector_back(self)
    def assign(self, *args): return _myexample.DoubleVector_assign(self, *args)
    def resize(self, *args): return _myexample.DoubleVector_resize(self, *args)
    def insert(self, *args): return _myexample.DoubleVector_insert(self, *args)
    def reserve(self, *args): return _myexample.DoubleVector_reserve(self, *args)
    def capacity(self): return _myexample.DoubleVector_capacity(self)
    __swig_destroy__ = _myexample.delete_DoubleVector
    __del__ = lambda self : None;
DoubleVector_swigregister = _myexample.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


def average(*args):
  return _myexample.average(*args)
average = _myexample.average

def average2(*args):
  return _myexample.average2(*args)
average2 = _myexample.average2

def say_hello(*args):
  return _myexample.say_hello(*args)
say_hello = _myexample.say_hello

def say_goodbye(*args):
  return _myexample.say_goodbye(*args)
say_goodbye = _myexample.say_goodbye


