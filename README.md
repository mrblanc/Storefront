# Storefront Application

This application is a simple storefront application. Customers can view items in the store, and managers can add items.

The application is implemented using Django, and is packaged with Docker.

## Prerequisites

A Linux machine running Docker >= 20.0 and docker-compose >= 2.0. Earlier versions may work as well, but they are untested. Windows may also work, but again, it is untested.

## Usage

* Clone this repo
* In a shell, navigate to the root of the repo
* Run `docker compose up -d --build`. This may need to be run with root (sudo) privileges.

### Accessing the storefront

Once the above docker compose command has been run, the storefront can be accessed in a browser from `https://localhost:8000/`.

### Adding users

A convienience script called `add_users.sh` has been added to allow bulk adding of users. Run `add_users.sh <config-file>`. A sample config file has been provided in `sample_configs/users.csv`. To use the sample config in:

`add_users.sh sample_configs/users.csv`.

### Shutting down the server

To shut down the server, run `docker compose down`.

### Running tests

To run tests, navigate to `django_project`, and run the command `python manage.py test`.

## Limitations

* Django's built-in development server is being used. The Django documentation explicitly recommends against using this server for production. This should be replaced with a production server such as Apache.
* A nosql server is being used as the database. This is fine for small-scale applications, but if it scaled up, it should be replaced with a production database such as PostGreSQL.
* Adding users through the `add_users.sh` script is an insecure method, since the passwords are stored in plaintext in a csv file prior to being added. A more secure method should be used. Even just adding users through Django's builtin admin portal is fine, but I wanted users to be able to get up and running without needing to see the backend of Django.
* Bare html is used, this could be made to look better with css.
