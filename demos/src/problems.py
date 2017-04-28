# try throw catch
# try raise except

class TooSmall(Exception):
    def error(self, x):  print("Too small")
class TooBig(Exception):
    def error(self):  print("Too big")
class MuchTooBig(Exception):
    def error(self):  print("Too small")


def f(x):
    if x < 10:
        raise TooSmall(x)
    if x > 200:
        raise MuchTooBig(x)
    if x > 100:
        raise TooBig(x)
    print(x)

try:
    f(3)
    f(133)
    f(3)
    f(3)
    f(3)
    f(3)
except Exception as e:
    e.error(e.__str__())

