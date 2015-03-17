def mycoroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

    
@mycoroutine
def lower():
    while True:
        message = yield
        yield message.lower()
    
@mycoroutine
def italic():
    while True:
        message = yield
        yield "<i>" + message + "</i>"

@mycoroutine
def upper():
    while True:
        message = yield
        yield message.upper()

@mycoroutine
def bold():
    while True:
        message = yield
        yield "<b>" + message + "</b>"


@mycoroutine
def format():
    while True:
        parameters = yield
        message = parameters.pop(0)
        for decorator in parameters:
            g = decorator()
            message = g.send(message)
        print message
    
g = format()
g.send(["MiXeD", upper, bold, italic])
g.send(["MiXeD", lower])
g.send(["MiXeD", italic, upper])
