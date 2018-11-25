#DjangoBlog

-   Django-bootstrap-admin, Bootstrap
-   markdown
-   RSS
-   markdown-editor (django-simplemde)

##Requirements

-   Python
-   Django
-   Bootstrap

## Install

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
    $ python manage.py runserver
```

Open the browser and go to http://localhost:8000/admin to create the first post.
