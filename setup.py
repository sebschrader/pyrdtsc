import platform

from setuptools import Extension, find_packages, setup


# PyPy does include glibc standard headers, but does not define any of the
# feature_test_macros(7)
# CPython on the other hand complains, if you define any of these macros
if platform.python_implementation() == 'PyPy':
    define_macros = [
            ('_XOPEN_SOURCE', '700'),
            ('_DEFAULT_SOURCE', '1'),
            ('_BSD_SOURCE', '1'),
    ]
else:
    define_macros = None

rdtsc = Extension('rdtsc', sources=['src/pyrdtsc.c'],
                  extra_compile_args=['-std=c99'],
                  define_macros=define_macros)


with open('README.rst') as f:
    readme = f.read()

setup(name='rdtsc',
      author='Sebastian Schrader',
      author_email='sebastian.schrader@ossmail.de',
      url='https://github.com/sebschrader/pyrdtsc',
      version='0.0.1',
      description="Read the cycle count using the rdtsc instruction",
      long_description=readme,
      package_dir={'': 'src'},
      packages=find_packages(exclude=['tests']),
      ext_modules=[rdtsc],
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: C',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: System :: Networking',
      ],
      )
