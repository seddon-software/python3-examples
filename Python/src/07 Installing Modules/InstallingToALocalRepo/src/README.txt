This is an example Python module (mypackage).
Use the scripts as follows:

1) build.py     - this will create a source distro and then move it to our web server
2) server.py    - start web server on localhost at port 8000
3) install.py   - use easy_install to download and install from local repo
                - server must be running
4) unistall.py  - uninstall package using easy_install
5) test.py      - verify it worked

There are also two scripts that use pip instead of easy_install
N.B. By default, setup.py sdist does not place non Python source files in 
generated tarballs, so specify them in MANIFEST.IN
