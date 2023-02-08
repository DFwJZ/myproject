# API Programming


## Authentication API Implementation

1. to add a new user run `python3 manage.py shell`

2. add following lines<br>

> `from django.contrib.auth.models import User` ;\ <br>

> `user = User.objects.create_user(username="your_username", "email="your_email", password="your_password")`;\ <br>

> `user.save()`
