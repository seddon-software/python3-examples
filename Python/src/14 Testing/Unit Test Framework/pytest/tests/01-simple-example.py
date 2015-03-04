############################################################
#
#    simple example
#
############################################################


"""
    1) if you need to install pytest, use:
        set http_proxy=wwwcache.rl.ac.uk:8080
        easy_install -U pytest
        
    2) add py.test.exe to PATH (exe will be found in Scripts directory)
    
    3) to run tests, go to a command prompt and type:
        py.test 01-simple-example.py
"""

def square(x):
    return x * x

def test_squares():
    assert square(6) == 36 # succeeds
    assert square(10) == 99 # fails

