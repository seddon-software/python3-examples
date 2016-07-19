import mako
from mako.template import Template

mytemplate = Template("hello world!")
print(mytemplate.render())
