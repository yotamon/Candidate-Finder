<p align="center"><img src="https://github.com/yotamon/Candidate-Finder/blob/master/gloat/candidator/static/images/main-img.png" height="150"></p>

# Candidate Finder

Candidate Finder is a Python App for Finding the right candidator for a specific job.

## Installation

1. Clone Git Repository To Your Local Environment
2. Create Migrations -
    ```bash
    python .\manage.py makemigrations candidator
    ```
3. Migrate -
    ```bash
    python .\manage.py migrate
    ```
4. Initialize Data -
    ```bash
    python .\manage.py loaddata data.json
    ```
5. Run The Server - 
    ```bash
    python .\manage.py runserver
    ```

## Admin Panel: 
    * User: admin
    * Password: admin
