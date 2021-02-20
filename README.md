# Bank of smart solutions

## Project setup
```
git clone https://github.com/VasiliKavaleu/css.git
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
python3 manage.py runserver --settings=config.settings.local
```

### Run on production mode
```
python3 manage.py runserver --settings=config.settings.pro
```

