# UPrintCloudBE

Your Cloud Printer

# Requirements

```
Python ≥ 3.6
django
pika
filetype
```

# API

```
/admin
/upload
/api/upload
/api/request?job_id=&client_id=
```

# Testing

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

## Web root

[127.0.0.1:8000](http://127.0.0.1:8000)
