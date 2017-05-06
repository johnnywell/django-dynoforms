import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-dynoforms',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://github.com/johnnywell/django-dynoforms',
    author='Johnny Wellington',
    author_email='johnny.w.santos@gmail.com',
    install_requires=[
        'django>=11.1',
        'psycopg2>=2.7.1'
    ],
    extra_require={
        'Templates': ['django-material>=0.13.1']
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)