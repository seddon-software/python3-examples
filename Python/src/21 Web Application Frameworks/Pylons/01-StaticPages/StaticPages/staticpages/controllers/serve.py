import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from staticpages.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ServeController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/serve.mako')
        # or, return a string
        return 'Hello World'
    
    def view1(self):
        return render('page1.mako')
    
    def view2(self):
        return render('page2.mako')

    def view3(self):
        return render('page3.mako')
    
