BASE=docker-compose.yml


setup:
	cp .env.example .env

docker-build:
	docker compose build

dev-start:
	docker compose up -d --build

dev-stop:
	docker compose stop

docker-shell:
	docker compose run web sh


# TODO add for production
