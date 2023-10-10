FROM python:3.11.0

RUN mkdir /booking

WORKDIR /booking

COPY pyproject.toml poetry.lock .

RUN pip install --upgrade pip \
  && pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

#RUN chmod a+x docker/*.sh
#COPY ./test.sh .
#RUN chmod +x /test.sh
#
#CMD ["/booking/test.sh"]
## run entrypoint.sh
#ENTRYPOINT ["/booking/entrypoint.sh"]

