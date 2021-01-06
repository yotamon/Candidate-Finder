<p align="center"><img src="https://github.com/yotamon/Candidate-Finder/blob/master/gloat/candidator/static/images/main-img.png" height="150"></p>

# Candidate Finder

Candidate Finder is a Python App for Finding the right candidate for a specific job.

## Installation

1. Clone Git Repository To Your Local Environment
2. Install Python + Pipenv
    ```bash
    pip install --user pipenv
    ```
3. Open App Environment Shell & Install Packages
    ```bash
    pipenv shell
    pipenv install
    ```
4. Create Migrations -
    ```bash
    python gloat\manage.py makemigrations candidator
    ```
5. Migrate -
    ```bash
    python gloat\manage.py migrate
    ```
6. Initialize Data -
    ```bash
    python gloat\manage.py loaddata data.json
    ```
7. Run The Server - 
    ```bash
    python gloat\manage.py runserver
    ```
8. Open Site URL - localhost:port/candidator

## Admin Panel: 
    * User: admin
    * Password: admin
