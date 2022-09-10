all: up migrate superuser

clean: 
	docker-compose down -v --rmi all --remove-orphans

down:
	docker-compose down

log:
	docker-compose logs -f

migrate:
	docker-compose exec web python manage.py migrate --noinput

superuser:
	docker-compose exec web python manage.py createsuperuser

up:
	docker-compose up -d 


