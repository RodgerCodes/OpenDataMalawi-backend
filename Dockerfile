FROM python:3.10
ENV PYTHONBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
COPY package.json /code/

RUN pip install -r requirements.txt
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN apt-get install -y nodejs
RUN npm install

COPY . /code/