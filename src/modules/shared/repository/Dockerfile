ARG PYTHON_VERSION="3.12"
FROM python:${PYTHON_VERSION}-alpine

ENV USE_DOT_ENV=False

WORKDIR /repository
COPY ./requirements.txt /repository/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /repository/requirements.txt

COPY ./ /repository/

CMD [ "alembic", "upgrade", "head" ]