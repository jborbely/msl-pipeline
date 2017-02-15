import sys
from setuptools import setup, find_packages
from distutils.cmd import Command

from msl import pipeline


class ApiDoc(Command):
    """
    A custom command that calls sphinx-apidoc
    http://www.sphinx-doc.org/en/1.5.1/man/sphinx-apidoc.html
    """
    description = "Calls sphinx-apidoc"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from sphinx.apidoc import main
        main([
            'sphinx-apidoc',
            '--force',  # Overwrite existing files
            '--module-first',  # Put module documentation before submodule documentation
            '--separate',  # Put documentation for each module on its own page
            '-o', './docs/_autosummary',
            'msl',
        ])
        sys.exit(0)


def read(filename, split=False):
    with open(filename) as fp:
        text = fp.read()
    return text if not split else text.split()

needs_pytest = {'tests', 'pytest'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

needs_sphinx = {'docs', 'build_sphinx', 'apidoc'}.intersection(sys.argv)
sphinx = ['sphinx', 'sphinx_rtd_theme'] if needs_sphinx else []

setup(
    name='msl-pipeline',
    version=pipeline.__version__,
    author=pipeline.__author__,
    author_email='joseph.borbely@callaghaninnovation.govt.nz',
    url='https://github.com/MSLNZ',
    description='Create a sequential pipeline.',
    long_description=read('README.rst'),
    license='MIT',
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    setup_requires=sphinx + pytest_runner,
    tests_require=['pytest-cov', 'pytest'] if needs_pytest else [],
    install_requires=read('requirements.txt', True) if not needs_pytest else [],
    cmdclass={'apidoc': ApiDoc},
    namespace_packages=['msl'],
    packages=find_packages(include=('msl*',)),
    include_package_data=True,
)
