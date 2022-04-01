# Build stage:
FROM python:3.8.5 as build-container

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

#Actual stage:
FROM python:3.8.5-slim-buster
COPY --from=build-container /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages
COPY --from=build-container /usr/local/bin/uvicorn/ /usr/local/bin/uvicorn/

RUN useradd apiuser
USER apiuser

ADD config.py  /publicapi/config.py
ADD main.py  /publicapi/main.py
ADD v1  /publicapi/v1
WORKDIR /publicapi

ENV PATH="/usr/local/bin/uvicorn:${PATH}"
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]