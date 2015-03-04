To install lxml on Windows run (as administrator)

easy_install --allow-hosts=lxml.de,*.python.org lxml==2.2.2

where 2.2.2 is the latest version that includes a binary egg.  If a later version
is installed, it will need to be compiled from source.

N.B. This failed for me on Python 2.7 (even as administrator)
runas /noprofile /user:administrator "easy_install --allow-hosts=lxml.de,*.python.org lxml==2.2.2"