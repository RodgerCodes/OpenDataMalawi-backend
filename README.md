# OpenDataMalawi

This is a platform where individuals can upload public datasets for the country that could be accessed via an api to download csv and excel files to train models.

## Tech Stack

**Docker** (Optional)

**Server:** Django, Postgres

## Run Locally

Clone the project

```bash
  git clone https://github.com/RodgerCodes/OpenDataMalawi-backend
```

Go to the project directory

```bash
  cd OpenDataMalawi-backend
```

create a .env

```bash
  make setup
```

### Note Add the required env varibles values

Create a virtual environment

Install packages

```bash
  pip install -r requirements.txt
```

Run Migrations

```bash
  python manage.py migrate
```

Run Server

```bash
  python manage.py migrate
```

the api run on - <http://localhost:8000>

## To view the docs visit

<http://localhost:8000/api/schema/swagger-ui/>

## With Docker

Clone the project

```bash
  git clone https://github.com/RodgerCodes/OpenDataMalawi-backend
```

Go to the project directory

```bash
  cd OpenDataMalawi-backend
```

create a .env

```bash
  make setup
```

### Note Add the required env varibles values

build the image

```bash
   make docker-build
```

start container

```bash
   make dev-start
```

navigate to containter shell

```bash
   make docker-shell
```

In docker shell run migrations

```bash
   python manage.py migrate
```

the api run on - <http://localhost:8000>

## To view the docs visit

<http://localhost:8000/api/schema/swagger-ui/>

## Running Tests

TODO: add tests

<!-- To run tests, run the following command

```bash
  make docker-test
``` -->

## Contributions

As usual PRs are welcome.
