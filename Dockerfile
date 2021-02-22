FROM python:3.9.2-alpine3.13

RUN pip install --upgrade pip \
    && pip install \
        flake8 \
        flake8-docstrings \
        flake8-import-order \
        flake8-todo \
        flake8-print \
        flake8-double-quotes \
        flake8-coding \
        pep8-naming \
        hacking \
        autoflake \
        autopep8 \
        docformatter \
        isort \
        radon \
        parameterized
