# Bank of smart solutions

## Project setup
```
git clone
```

### Activate environment
```
source venv/bin/activate
```

### Install requirements
```
pip3 install -r requirements.txt
```

### Apply migrations 
```
python manage.py migrate --settings=config.settings.local
```

### Run on local mode
```
python manage.py runserver --settings=config.settings.local
```

### Run on production mode
```
python manage.py runserver --settings=config.settings.pro
```

