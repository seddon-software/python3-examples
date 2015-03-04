from wsgiref.simple_server import make_server

from pyramid.config import Configurator

def main():
    config = Configurator()
    config.include('pyramid_chameleon')
    config.scan("views")
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    print '''try requesting:
        http://localhost:8080'''
    server = make_server('localhost', 8080, app)
    server.serve_forever()
