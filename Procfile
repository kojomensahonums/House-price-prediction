#web: gunicorn app:app -b :8080 --timeout 120 --workers=3 --threads=3 --worker-connections=1000
web: gunicorn app:app 
#web: gunicorn app.wsgi--log-file-app
#web: gunicorn --workers=3 app:app --timeout 200 --log-file -
#gunicorn app:app --preload
#gunicorn app.wsgi:application --log-file - --log-level debug
#web: gunicorn app:app > Procfile

