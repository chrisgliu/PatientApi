# PatientApi

This is an API to keep track of instructions for a procedure.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip3 install -r requirements.txt
```
```bash
git clone <this repository>
```
## Usage
```bash
cd PatientApi/papi
```
Set up the database *currently just sqlite
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --username admin
```
Run server
```bash
python3 manage.py runserver
```

## URL Paths

admin/ \
api/ \
[GET, POST] \
api/users/ \
[GET, POST] \
api/procedures/ \
[GET, POST] \
api/instructions/ \
[GET, PUT, DELETE] \
api/procedure/(id)/ \
[GET, PUT, DELETE] \
api/instruction/(id)/ \
[GET] \
api/procedurelist/(username)/ \
[GET] \
api/instructionlist/(username)/(procedure_id)/

