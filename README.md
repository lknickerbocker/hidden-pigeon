# HIDDEN PIGEON

A site for storing and serving assets related to film production.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# CLONE AND RUN

This project uses docker.

    $ sudo docker-compose -f local.yml up --build
    $ sudo docker-compose -f local.yml run --rm django python manage.py createsuperuser

# TESTING

    $ docker-compose -f local.yml run --rm django coverage run -m pytest
    $ docker-compose -f local.yml run --rm django coverage html
