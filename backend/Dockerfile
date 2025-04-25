FROM python:3.12
RUN pip install poetry==1.7.1

WORKDIR /it_hero_map
COPY . /it_hero_map

RUN poetry install
CMD poetry run python -m it_hero_map
