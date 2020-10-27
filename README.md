##### PITCH-TECH

## Author

Lekam Charity

## Description

A Pitch-Tech is an application where users can vote on them, leave comments, and also add new pitches.


## Description & User Specifications
The Pitch-Tech is web application  that enable users to:

    1. Post pitches
    2. Downvote a pitch
    3. Upvote a pitch
    4. Comment on  pitches posted by othe users


## Set-up and Installation

# Software Requirements
    - Python 3.8
    - PostgreSQL DMS

### Clone the Repo
Run the following command on the terminal:
* `git clone https://github.com/LekamCharity/Pitch-Tech`
*  cd Pitch-Tech
Install [Postgres](https://www.postgresql.org/download/)
Install [Python](https://www.python.org/downloads/)

### Create a Virtual Environment
Run the following commands in the same terminal:
```python3.8 -m venv --without-pip virtual```
```curl https://bootstrap.pypa.io/get-pip.py | python```
```source virtual/bin/activate```

### Database
Quickly create a database where your data is going to be persistent .
```
psql
you=#  CREATE DATABASE pitches;
```

```bash
SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://username:password@localhost/pitchtech'
SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3.8 manage.py server` 


## Technologies used
    - Python 3.8
    - HTML
    - Heroku
    - Postgresql

## Contact Information 

If you have any question or contributions, please email me at [lekamcharity@gmail.com]

### License
  [MIT](https://github.com/LekamCharity/Natalie-news/blob/master/License) Copyright (c) 2020 Lekam Charity

