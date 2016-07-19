from pyramid.renderers import get_renderer
from pyramid.view import view_config

def site_layout():
    renderer = get_renderer("templates/master.pt")
    layout = renderer.implementation().macros['layout']
    return layout


@view_config(renderer="templates/index.pt")
def index_view(request):
    return {"layout": site_layout(),
            "page_title": "Home"}


@view_config(renderer="templates/teams.pt", name="teams")
def teams_view(request):
    return {"layout": site_layout(),
            "page_title": TITLE + ": Teams",
            "theTeams": TEAMS}


@view_config(renderer="templates/grounds.pt", name="grounds")
def grounds_view(request):
    return {"layout": site_layout(),
            "page_title": TITLE + ": Grounds",
            "theGrounds": GROUNDS}


@view_config(renderer="templates/both.pt", name="both")
def teams_and_grounds_view(request):
    return {"layout": site_layout(),
            "page_title": TITLE,
            "theTeams": TEAMS,
            "theGrounds": GROUNDS}

# Dummy data
TITLE = "Football Teams and Grounds"

TEAMS = [
    {'name': 'Chelsea',       'country': 'England'},
    {'name': 'Paris SG',      'country': 'France'},
    {'name': 'Juventus',      'country': 'Italy'},
    {'name': 'Ajax',          'country': 'Netherlands'},
    {'name': 'Barcelona',     'country': 'Spain'},
    {'name': 'Bayern Munich', 'country': 'Germany'},
]

GROUNDS = [
    {'ground': 'Amsterdam ArenA', 'city': 'Amsterdam'},
    {'ground': 'Wembley',         'city': 'London'},
    {'ground': 'Nou Camp',        'city': 'Barcelona'},
    {'ground': 'Hampden Park',    'city': 'Glasgow'},
]
