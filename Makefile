BASE=docker-compose.yml


setup:
	cp .env.example .env

dev-build-start:
	docker compose up -d --build

dev-start:
	docker compose up -d

dev-stop:
	docker compose stop

docker-shell:
	docker compose run web she


# TODO add for production
