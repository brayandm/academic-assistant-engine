## Installation instructions

1 - Install pipenv:

```bash
pip install pipenv
```

2 - Initialize the virtual environment and install the dependencies:

```bash
pipenv install
```

3 - Install the pre-commit hook:

```bash
cp pre-commit .git/hooks/pre-commit
```

4 - Start the server on port 5000:

```bash
cd server && pipenv run flask run --reload
```

## Docker instructions

1- Start the server on port 5000:

```bash
docker compose up -d
```