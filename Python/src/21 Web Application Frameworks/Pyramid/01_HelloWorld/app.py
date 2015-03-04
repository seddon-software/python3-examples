from wsgiref.simple_server import make_server
from pyramid.config import Configurator #@UnresolvedImport
from pyramid.response import Response

# This acts as the view function
def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

def main():
    # Grab the config, add a route and view, and make a WSGI app
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    # When run from command line, launch a WSGI server and app
    app = main()
    server = make_server('localhost', 8080, app)
    print '''try requesting:
        http://localhost:8080/hello/john'''
    server.serve_forever()

