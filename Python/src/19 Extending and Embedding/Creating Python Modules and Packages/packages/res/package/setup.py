from distutils.core import setup

setup(name='mypackage',
      version='1.0',
      packages=['mypackage', 'mypackage.mystuff'],
      package_dir={'mypackage': 'src/mypackage'},
      description='Example Package Distribution',
      long_description='shows how to install a module',
      license='there is no licence for this application',
      platforms='windows x86 x32',
      author='Chris Seddon',
      author_email='seddon-software@keme.co.uk',
      url='http://www.keme.net/~seddon-software',
      )
