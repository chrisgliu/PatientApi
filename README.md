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

## Schema
<img width="587" alt="schema" src="https://user-images.githubusercontent.com/59263349/180017619-3a2c68e0-3165-418b-8270-59aa0f063011.png">

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

## Examples

<img width="729" alt="Screen Shot 2022-07-20 at 9 23 46 AM" src="https://user-images.githubusercontent.com/59263349/180018185-dc468d31-84cc-49a7-952d-f2c73997c4ec.png">

<img width="854" alt="Screen Shot 2022-07-20 at 9 25 10 AM" src="https://user-images.githubusercontent.com/59263349/180018129-41bcc1b1-1bc3-49a9-97db-bfae818750e4.png">

<img width="923" alt="Screen Shot 2022-07-20 at 9 26 03 AM" src="https://user-images.githubusercontent.com/59263349/180018072-2da369d5-4097-4c8a-b694-e057ff4bbbae.png">

<img width="916" alt="Screen Shot 2022-07-20 at 11 08 46 AM" src="https://user-images.githubusercontent.com/59263349/180017995-ab020e50-3eb8-4904-bb1e-a8e8d2d9408f.png">

<img width="916" alt="Screen Shot 2022-07-20 at 11 09 04 AM" src="https://user-images.githubusercontent.com/59263349/180017946-b772ed01-6239-4aaf-a03c-f2c4cecbea0e.png">

<img width="731" alt="Screen Shot 2022-07-20 at 9 23 10 AM" src="https://user-images.githubusercontent.com/59263349/180017850-04a35e28-528b-47d3-b895-c306630e1b41.png">

<img width="736" alt="Screen Shot 2022-07-20 at 9 23 01 AM" src="https://user-images.githubusercontent.com/59263349/180017794-fea342ec-8943-4772-9a6f-d1c0b4539a5e.png">

