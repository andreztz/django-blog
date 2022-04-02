# DjangoBlog

- Django-bootstrap-admin, Bootstrap
- markdown
- Markdown-editor (django-simplemde)
- RSS

## Run

```bash
$ git clone https://github.com/andreztz/django-blog.git
$ cd django-blog
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ cd blog/static/
$ bower install
$ cd ../..
$ cp .env.example .env
$ python manage.py runserver
```

# Docker

```bash
$ docker build --tag django-blog . 
$ docker volume create django-blog-db
$ docker run --rm -d --name django-blog -p 8000:8000 -v django-blog-db:/app/data/ django-blog:latest
$ docker container exec -it django-blog python manage.py createsuperuser
```

Open the browser and go to http://localhost:8000/admin to create the first post.
