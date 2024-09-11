# Geoluminate Admin

[![Github Build](https://github.com/Geoluminate/geoluminate-earth-science/actions/workflows/build.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-earth-science/actions/workflows/build.yml)
[![Github Docs](https://github.com/Geoluminate/geoluminate-earth-science/actions/workflows/docs.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-earth-science/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/Geoluminate/geoluminate-earth-science/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/Geoluminate/geoluminate-earth-science)
![GitHub](https://img.shields.io/github/license/Geoluminate/geoluminate-earth-science)
![GitHub last commit](https://img.shields.io/github/last-commit/Geoluminate/geoluminate-earth-science)
![PyPI](https://img.shields.io/pypi/v/geoluminate-earth-science)
<!-- [![RTD](https://readthedocs.org/projects/geoluminate-earth-science/badge/?version=latest)](https://geoluminate-earth-science.readthedocs.io/en/latest/readme.html) -->
<!-- [![Documentation](https://github.com/Geoluminate/geoluminate-earth-science/actions/workflows/build-docs.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-earth-science/actions/workflows/build-docs.yml) -->
<!-- [![PR](https://img.shields.io/github/issues-pr/Geoluminate/geoluminate-earth-science)](https://github.com/Geoluminate/geoluminate-earth-science/pulls)
[![Issues](https://img.shields.io/github/issues-raw/Geoluminate/geoluminate-earth-science)](https://github.com/Geoluminate/geoluminate-earth-science/pulls) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/geoluminate-earth-science) -->
<!-- ![PyPI - Status](https://img.shields.io/pypi/status/geoluminate-earth-science) -->

A Django application for managing collections of scientific instruments

Documentation
-------------

The full documentation is at https://SamuelJennings.github.io/geoluminate-admin/

Quickstart
----------

Install Geoluminate Earth Science::

    pip install geoluminate-earth-science

Add it to your `INSTALLED_APPS`:


    INSTALLED_APPS = (
        ...
        'geoscience',
        ...
    )

Add Geoluminate Earth Science's URL patterns:

    urlpatterns = [
        ...
        path('', include("geoscience.urls")),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

