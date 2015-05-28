import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'cornice',
]

setup(name='reactions',
      version=0.1,
      description='reactions',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Maciej Maciaszek',
      author_email='maciej.maciaszek@gmail.com',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramid_alchemy',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = reactions:main
      [console_scripts]
      initialize_pyramid_alchemy_db = pyramid_alchemy.scripts.initializedb:main
      """,
      paster_plugins=['pyramid'])
