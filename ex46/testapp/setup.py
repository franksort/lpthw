try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'testapp description',
    'author': 'Frank S.',
    'url': '',
    'download_url': '',
    'author_email': 'franksort@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['testapp'],
    'scripts': ['bin/testing'],
    'name': 'testapp'
}

setup(**config)
