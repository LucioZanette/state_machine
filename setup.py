from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
#import numpy

extensions = [
    Extension(
		'run_cython', 
		sources=['run_cython.pyx'], 
		#include_dirs=[numpy.get_include()], 
		extra_compile_args=['-O3'], 
		language='c++')
]

setup(
    name="processing_module",
    ext_modules = cythonize(extensions),
)