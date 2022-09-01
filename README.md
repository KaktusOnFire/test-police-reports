# test-police-reports

Case - https://gist.github.com/tm-minty/c39f9ab2de1c70ca9d4d559505678234

- [Requirements](#requirements)
- [Setup](#setup)
    - [Docker](#docker)
    - [Database](#database)
- [Usage](#usage)

## Requirements
* asgiref==3.5.2
* asyncpg==0.26.0
* backports.zoneinfo==0.2.1
* Django==4.1
* django-rest-framework==0.1.0
* djangorestframework==3.13.1
* gunicorn==20.1.0
* psycopg2==2.9.3
* pytz==2022.2.1
* sqlparse==0.4.2
* tzdata==2022.2

## Setup

### Docker
```bash
docker-compose up --build -d
```

### Database
- Put your csv file into 'scripts' folder
- Setup venv with [requirements](#requirements)
- Run `db.py` script
- Enter variables:
    - CSV file - `"your file name".csv`
    - Database URL - `postgresql://test_user:test_pass@localhost/police`
    - Table name - `api_appeals`

## Usage

#### Get reports

`GET /api/v1/appeals/list/`

| Parameter | Type     | Description                | Example                |
| :-------- | :------- | :------------------------- |:-----------------------|
| `date_from` | `date` | Get reports after the specified date | `date_from=2016-01-02` |
| `date_to` | `date` | Get reports before the specified date | `date_to=2016-01-02` |
| `limit` | `int` | Limit reports count per page (default - 20) | `limit=100` |
| `offset` | `int` | Starting position of the query | `offset=25` |