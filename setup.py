from distutils.core import setup
from Cython.Build import cythonize

directives = {'language_level': 3}
setup(
    ext_modules=cythonize('fib.pyx'),
    zip_safe=False,
    
)
