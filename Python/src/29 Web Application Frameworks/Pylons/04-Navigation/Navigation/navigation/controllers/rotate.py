import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from navigation.lib.base import BaseController, render
from navigation.model.nav import Nav

log = logging.getLogger(__name__)

class RotateController(BaseController):

    def index(self):
        if 'nav' in session: 
            nav = session['nav']
        else:
            nav = Nav()

        page = nav.next()
        c.page = page
        nextPage = "page-" + str(page) + ".mako"
        return render(nextPage)
