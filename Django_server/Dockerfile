FROM python:3.8.5
LABEL author='plavrentev' version=1.1.1
WORKDIR /code_web_med_plist
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .
RUN python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir 
# CMD gunicorn --env DJANGO_SETTINGS_MODULE=set_1e9usd.settings set_1e9usd.wsgi --bind 0.0.0.0:8003
CMD gunicorn web_med_plist.wsgi:application --bind 0.0.0.0:8004
# CMD daphne -p 8004 web_med_plist.asgi:application
