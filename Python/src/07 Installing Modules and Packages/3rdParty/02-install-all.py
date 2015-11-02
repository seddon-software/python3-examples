# Use this script to setup packages
#
# N.B. if you are installing behind a proxy you will have to set 
#    HTTP_PROXY=http://user:password@yourproxy.com:port
# Alternatively use a local repository:
#    install -f http://localhost/repo foo


import pip, os

# modify this if your installation is behind a proxy
def setProxy(url):
    """example call:
          setProxy("http://wwwcache.rl.ac.uk:8080")
    """
    os.environ["HTTP_PROXY"] = url
    
def install(cmd):
    cmd = mode + " " + cmd
    print "**** pip {0}".format(cmd)
    pip.main(cmd.split())
    
# mode = "uninstall"
mode = "install --upgrade"
# mode = "install"
install("beautifulSoup")
install("bottle")
install("chameleon")
install("cherrypy")
install("cx_oracle")
install("django")
install("html5lib")
install("flask")
install("mako")
install("markupsafe") 
install("mechanize")
install("mock")
install("multiprocessing")
install("nose")
install("numpy")
install("paramiko")
install("pip")
install("pil")
install("pisa")
install("profilestats")
install("pycurl")
install("pypdf2")
install("pypng")
install("pyprof2html")
install("pyramid")
install("pyramid_chameleon")
install("pyramid_mako")
install("pysnmp")
install("pytest")
install("pyx")
install("reportlab")
install("requests")
install("scipy")
install("scrapy")
install("scons")
install("selenium")
install("speech")
install("sqlalchemy")
install("virtualenv")
install("webob")
install("web.py")
install("xlrd")     # excel
install("xlwt")     # excel
install("yolk")

# use pip and yolk to see what is installed
pip.main(['freeze'])

1



