import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from usingforms.lib.base import BaseController, render

log = logging.getLogger(__name__)

import formencode
from formencode import htmlfill
from usingforms.model.form import MyForm

class MyformController(BaseController):

    def index(self):
        c.title = "Simple Form"
        c.text = "Please fill in the form below"
        return render('/myform.mako')
    
    def results(self):
        schema = MyForm()
        try:
            form_result = schema.to_python(dict(request.params))
        except formencode.Invalid, error:
            response.content_type = 'text/plain'
            return 'Invalid: ' + unicode(error)

        firstName = request.params['firstName']
        lastName = request.params['lastName']
        c.title = "FORM RESULTS"
        c.text = firstName + " " + lastName
        return render('/myresults.mako')

