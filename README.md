# twittoff-ssg
# Setup

```
pipenv install
```
Migrate  the database

```sh
$env:FLASK_APP = "web_app"
flask db init

$env:FLASK_APP = "web_app"
flask db migrate

$env:FLASK_APP = "web_app"
flask db upgrade

#Usage
```sh
$env:FLASK_APP = "web_app"
flask run
```