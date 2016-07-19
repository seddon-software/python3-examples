# doesn't work on MacOS (not yet ported)
import web

urls = (
  '/(.*)', 'index'
)
render = web.template.render('templates/')
app = web.application(urls, globals())

class index:
    def GET(self,name):
        return render.index(name)

if __name__ == "__main__": app.run()

