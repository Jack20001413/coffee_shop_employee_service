ARG PYTHON_VERSION="3.12"
FROM python:${PYTHON_VERSION}-alpine

ENV USE_DOT_ENV=False

WORKDIR /workplace
COPY ./workplace/requirements.txt /workplace/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /workplace/requirements.txt

WORKDIR /shared/utils
COPY ./shared/utils /shared/utils

WORKDIR /workplace
COPY ./workplace/ /workplace/

EXPOSE 8000
CMD [ "fastapi", "run", "main.py" ]


