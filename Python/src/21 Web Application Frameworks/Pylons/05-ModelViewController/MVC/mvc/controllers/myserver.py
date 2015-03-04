import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mvc.lib.base import BaseController, render

log = logging.getLogger(__name__)
from mvc.model.football import Football
from mvc.model.rugby import Rugby

class MyserverController(BaseController):

    def index(self):
        Football.initializeData()
        Rugby.initializeData()
        return render('/mvc.mako')
        
    def display(self):
        model = request.params['model']
        view = request.params['view']
        if model == None: model = "football"
        if view == None: view = "table"

        if model == "football": modelClass = Football
        if model == "rugby": modelClass = Rugby
        if view == "table": template = "/table.mako"
        if view == "chart": template = "/chart.mako"
        c.data = modelClass.readData()
        return render(template)
