from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("gdx_getting_started_usb.pyx")
)