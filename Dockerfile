FROM python:3.7.4

ENV SRC=/application/src

RUN apt-get update

RUN mkdir -p ${SRC}

WORKDIR ${SRC}

COPY requirements.txt ${SRC}

# Avoid installings reqs on code changes
RUN pip3.7 install -r requirements.txt

COPY config ${SRC}/config
COPY src ${SRC}

CMD ["python", "main.py"]