class MuchTooBig(Exception): pass
class TooBig(Exception): pass
class SomethingElse(Exception): pass

def prices(n):
    if n == 173:
        raise SomethingElse()
    if n > 200:
        raise MuchTooBig()
    if n > 100:
        raise TooBig()
    print("price {} OK".format(n))

prices(173)
try:
    prices(50)
    prices(173)
    prices(150)
except TooBig:
    print("Too Big")
except MuchTooBig:
    print("Much Too Big")
except Exception:
    print("This is always prefered")
