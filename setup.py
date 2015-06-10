import os

from setuptools import setup, find_packages
from setuptools.command import test
from utils import setuptools_behave


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

# prepare for monkey patching test command
# to make nose work with `setup.py test`
# see: http://goo.gl/kq9CBs
test._test = test.test


# Based on example at
# https://github.com/0compute/makeenv/blob/master/setup.py
class NoseTestCommand(test._test):

    user_options = test._test.user_options + [
        ("args=", "a", "Arguments to pass to nose"),
    ]

    def initialize_options(self):
        test._test.initialize_options(self)
        self.args = None

    def finalize_options(self):
        test._test.finalize_options(self)
        self.args = self.args and self.args.strip().split() or []
        self.test_suite = True

    def run_tests(self):
        try:
            import nose
        except ImportError:
            raise Exception(
                "You've tried to run command without nose installed")
        nose.run_exit(argv=["nosetests"] + self.args)


requires = [
    'pyramid',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'cornice',
]

setup_requires = [
    'nose',
    'behave',
    'Sphinx',
    'PasteScript',
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
      test_suite='reactions',
      install_requires=requires,
      setup_requires=setup_requires,
      cmdclass={
          'test': NoseTestCommand,
          'behave_test': setuptools_behave.behave_test
      },
      entry_points="""\
      [paste.app_factory]
      main = reactions:main
      [console_scripts]
      initialize_pyramid_alchemy_db = pyramid_alchemy.scripts.initializedb:main
      """,
      paster_plugins=['pyramid'])
