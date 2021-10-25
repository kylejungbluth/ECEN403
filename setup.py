from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Feedback_Trial1',
    ext_modules=cythonize("feedback.py"),
    zip_safe=False,
)