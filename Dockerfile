#Pull base image
From python:3.10.4

#Set enviroment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set work directory
WORKDIR /code


#Install dependencies
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /code/

ENTRYPOINT ["sh","./entrypoint.sh"]