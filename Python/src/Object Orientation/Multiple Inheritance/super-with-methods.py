class Base(object):
    def say(self, indent = 0):
        print '%s%s' % ('\t'*indent, 'Base')
class ChildA(Base):
    def say(self, indent = 0):
        print '%s%s' % ('\t'*indent, 'ChildA')
        super(ChildA, self).say(indent+1)
class ChildB(Base):
    def say(self, indent = 0):
        print '%s%s' % ('\t'*indent, 'ChildB')
        super(ChildB, self).say(indent+1)
class ChildC(ChildA, ChildB):
    def say(self, indent = 0):
        print '%s%s' % ('\t'*indent, 'ChildC')
        super(ChildC, self).say(indent+1)
obj = ChildC()
obj.say()


1
