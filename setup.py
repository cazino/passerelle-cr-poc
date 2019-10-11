#! /usr/bin/env python

import os
import subprocess

from setuptools import setup, find_packages
from distutils.command.sdist import sdist


class eo_sdist(sdist):
    def run(self):
        if os.path.exists('VERSION'):
            os.remove('VERSION')
        version = get_version()
        version_file = open('VERSION', 'w')
        version_file.write(version)
        version_file.close()
        sdist.run(self)
        if os.path.exists('VERSION'):
            os.remove('VERSION')


def get_version():
    if os.path.exists('VERSION'):
        version_file = open('VERSION', 'r')
        version = version_file.read()
        version_file.close()
        return version
    if os.path.exists('.git'):
        p = subprocess.Popen(['git', 'describe', '--dirty', '--match=v*'], stdout=subprocess.PIPE)
        result = p.communicate()[0]
        if p.returncode == 0:
            version = result.split()[0][1:]
            version = version.replace('-', '.')
            return version
    return '0'


setup(
    name='passerelle-cr-poc',
    version=get_version(),
    author='CR Reunion',
    author_email='toto@example.net',
    url='http://example.net/',
    packages=find_packages(),
    cmdclass={
        'sdist': eo_sdist,
    }
)
