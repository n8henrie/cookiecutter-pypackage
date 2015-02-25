from cookiecutter.main import cookiecutter
import json
import datetime
import os.path

curdir = os.path.dirname(os.path.abspath(__file__))
# defaults = json.load('cookiecutter.json')

today = datetime.datetime.today()
date = today.date().isoformat()
year = today.year

extra_context = {
        'release_date': date,
        'year': year
        }

cookiecutter(curdir, extra_context=extra_context)

