## Installation instructions

1 - Initialize the virtual environment and install the dependencies:

```bash
pipenv shell
pipenv install
```

2 - Install the pre-commit hook:


```bash
cp pre-commit .git/hooks/pre-commit
```

3 - Start the server on port 5000:

```bash
cd server && flask run --reload
```