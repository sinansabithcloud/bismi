# Django ERP Web Application

## Features
- Inventory Management
- Sales Billing
- Thermal Printing
- Daily & Monthly Reports
- Daily Expenses
- Fund Management (Cash, Bank)

## Prerequisites
Ensure you have the following installed on your system:

- **Python 3.6** or higher (tested with Python 3.13.2)
- **pip** (tested with pip 25.0.1)

## How to Setup

#### Clone the repository to your local machine
```bash
git clone https://github.com/FINUSAM/Django-ERP-Software.git
cd Django-ERP-Software
```

#### Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### Migrate Database
```bash
python manage.py migrate
```


#### Run Application
Either run the below script in cmd or run the **billapp.vbs** script
```bash
python manage.py runserver
```