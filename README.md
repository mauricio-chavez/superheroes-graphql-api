# Superheroes GraphQL API

A superheroes api built with Django and GraphQL

## Requirements

* python3
* git

## Installation

In the folder where you want to put your project, type this:

```bash
$ git clone https://github.com/mauricio-chavez/superheroes-graphql-api.git
$ cd superheroes-graphql-api
```

Create a virtual environment and activate it:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

When you want to exit your virutal environment:

```bash
$ deactivate
```

Install the project requirements
```bash
$ pip install -r requirements.txt
```

Move to the project folder

```bash
$ cd superheroes_api
```

Now, run your migrations

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Load the superheroes data with:

```bash
$ python manage.py loaddata superheroes
```

And finally serve the application:

```bash
$ python manage.py runserver
```

Then, you must implement by yourself your GraphQL API 

## Usage

When you already installed the app, you can run on the project root:

```bash
$ python3 -m venv env
$ source env/bin/activate
$ python manage.py runserver
```

