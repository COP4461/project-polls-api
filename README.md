# Pollstop.com API
Backend API server code for pollstop project


## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Structure](#structure)
  - [Data Models](#data-models)
  - [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- `GET` / `POST` / `PUT` / `DELETE` endpoints using Django REST Framework.
- Modularized applications:
  - polls
  - answers
  - votes
  - tags
  - users
- PostgreSQL or SQLite3.
- Results pagination.
- Requests Throttling system.
- CMS Admin dashboard to edit database entries.
- API explorer.


## Getting Started

#### Install dependencies
This project requires Python and Django to build, if they are not installed on your device, you should install them first.

1. [Python3](https://www.python.org/downloads/)
2. [Django](https://www.djangoproject.com/)
3. [Django REST Framework](http://www.django-rest-framework.org/)
7. [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers)

#### Install Python dependencies
```bash
$ pip3 install -r requirements.txt
```

#### Initial Server Setup
1. Collect Static Files
```bash
$ ./manage.py collectstatic
$ ./manage.py migrate
```

2. Create Django Database
```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```

3. Create Admin account
```bash
$ ./manage.py createsuperuser
```

_Note:_ users info can be changed later from *AUTHENTICATION AND AUTHORIZATION* section in the admin dashboard

#### Running the server
```bash
./manage.py runserver -p 8000
```

#### Administration Dashboard
Server admin dashboard can be accessed by visiting the URL `localhost:8000/admin`.

#### API Explorer
API Explorer is available for all [endpoints](#api-endpoints) via the URL `localhost:8000/<endpoint_url>`.


## Structure

#### Data Models
- [Poll](polls/models.py)
- [Answer](answers/models.py)
- [Vote](votes/models.py)
- [Tag](tags/models.py)
- [User](users/models.py)


#### API Endpoints

- **GET Endpoints**
  - Polls:
    - `api/v1/polls/latest/`: get latest 10 polls.
    - `api/v1/polls/<poll_id>/`: get specific poll.
  - Tags:
    - `api/v1/tags/`: get all tags (paginated).
    - `api/v1/tags/<tag_id>/`: get specific tag.
    - `api/v1/tags/<tag_id>/polls/`: get all polls with a tag (paginated).
  - Users:
    - `api/v1/users/<user_id>/public/`: get public info for a user.
    - `api/v1/users/<user_id>/`: get all info for a user (requires authorization).
    - `api/v1/users/<user_id>/polls/`: get all polls owned by a user (paginated).
    - `api/v1/users/<user_id>/votes/`: get all votes for a user (requires authorization, paginated).
- **POST Endpoints**:
  - Polls:
    - `api/v1/polls/`: create new poll (requires authentication).
  - Tags:
    - `api/v1/tags/`: create new tag (requires authentication).
  - Answers:
    - `api/v1/answers/`: create new answer for a poll (requires authorization).
  - Votes:
    - `api/v1/votes/`: create new vote for an answer (requires authentication).
- **PUT Endpoints**:
  - Polls:
    - `api/v1/polls/<poll_id>/`: update poll (requires authorization).
  - Answers:
    - `api/v1/answer/<answer_id>/`: update answer (requires authorization).
  - Users:
    - `api/v1/users/<user_id>/`: update user info (requires authorization).
- **DELETE Endpoints**
  - Polls:
    - `api/v1/polls/<poll_id>/`: delete poll (requires authorization).
  - Users:
    - `api/v1/users/<user_id>/`: delete user (requires authorization).

## Contributing
This Project is still in progress. Your feedback is always appreciated and welcomed. If you find a bug in the source code or a mistake in the documentation, you can help us by submitting an issue [**here**](https://github.com/pollstop/pollstop-api/issues). Even better you can submit a Pull Request with a fix :)


## License
This repo is released under the [MIT License](LICENSE).
