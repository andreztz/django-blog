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

Open the browser and go to http://localhost:8000/admin to create the first post.
