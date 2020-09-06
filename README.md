# Python project boilerplate

## What's in?

Initialized with `Flask` (HTTP support) with `/heartbeat` and empty `/api` route

Comes also with dev packages
- `setuptools` to handle setup.py, 
- `pylint` linter,
- `black` && `isort` code formatter,
- `mypy` static type checker
- `coverage` code coverage

## How to test

Install dependencies
```bash
pipenv sync --dev
```

Run tests (will also check lint / mypy)
```bash
pipenv run make test
```

Test all / lint code
```bash
pipenv run make test-all
pipenv run make black
```


## Run the server
```bash
export FLASK_APP='./mywebapp/api/wsgi.py'
pipenv run flask run
```




