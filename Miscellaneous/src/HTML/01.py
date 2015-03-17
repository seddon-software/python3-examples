from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

def getFileAsText(filename):
    try: 
        f = open(filename, "r")
        allLines = f.readlines()
        text = "".join(allLines)
        return text
    except IOError,e:
        print e
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr
    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data
    def handle_comment(self, data):
        print "Comment  :", data
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c
    def handle_decl(self, data):
        print "Decl     :", data

parser = MyHTMLParser()
parser.feed('<style type="text/css">#python { color: green }</style>')


parser.feed(getFileAsText("files/ex1.html"))
parser.feed(getFileAsText("files/ex2.html"))
parser.feed(getFileAsText("files/ex3.html"))
parser.feed(getFileAsText("files/ex4.html"))

