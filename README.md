# flask jwt starter
```
git clone https://github.com/imylomylo/flask_jwt_starter
cd flask_jwt_starter
docker-compose up
```
To see the jwt flow In another terminal
```
./login.curl
```

## without docker
```
git clone https://github.com/imylomylo/flask_jwt_starter
cd flask_jwt_starter
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

If there are pip errors, maybe your system doesn't have python-pip installed.
