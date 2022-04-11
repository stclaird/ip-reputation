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

ADD config.py  /ip_reputation/config.py
ADD main.py  /ip_reputation/main.py
ADD v1  /ip_reputation/v1
ADD model  /ip_reputation/model
WORKDIR /ip_reputation

ENV PATH="/usr/local/bin/uvicorn:${PATH}"
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]