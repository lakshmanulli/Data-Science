From python:3.9
copy . /App
workdir /App
run pip install -r requirements.txt

expose $port

cmd gunicorn --workers 4 --bind 0.0.0.0:$port App:App