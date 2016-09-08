from pyramid.view import view_config

@view_config(renderer="home.pt")
def home(request):
    return {}

@view_config(renderer="pages.pt", name="page1")
def view1(request):
    return {
             "firstName": "Chris",
             "lastName": "Seddon"
           }

@view_config(renderer="pages.pt", name="page2")
def view2(request):
    return {
            "firstName": "John", 
            "lastName": "Smith"
           }

