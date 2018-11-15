import os

from setuptools import setup, find_packages
import subprocess

# get the version
version_ns = {}
here = os.path.dirname(__file__)
with open(os.path.join(here, 'binderhub', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = [
        l.strip() for l in f.readlines()
        if not l.strip().startswith('#')
    ]

with open('README.rst', encoding="utf8") as f:
    readme = f.read()

# Build our js and css files before packaging
subprocess.check_call(['npm', 'install'], shell=True)
subprocess.check_call(['npm', 'run', 'webpack'], shell=True)

setup(
    name='binderhub',
    version=version_ns['__version__'],
    python_requires='>=3.6',
    author='Project Jupyter Contributors',
    author_email='jupyter@googlegroups.com',
    license='BSD',
    url='https://binderhub.readthedocs.io/en/latest/',
    project_urls={
        'Documentation': 'https://binderhub.readthedocs.io/en/latest/',
        'Funding': 'https://jupyter.org/about',
        'Source': 'https://github.com/jupyterhub/binderhub/',
        'Tracker': 'https://github.com/jupyterhub/binderhub/issues',
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="reproducible science environments docker kubernetes",
    description="Turn a Git repo into a collection of interactive notebooks",
    long_description=readme,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
