# Github Navigator

### A web application that helps to search for repositories on the Github.

To run the application -

-   Open terminal in the project directory.

```sh
export FLASK_APP=application
export FLASK_ENV=development
export GITHUB_TOKEN=<your_github_token>
flask run
```

-   Copy and paste link in browser to view the application.

```sh
127.0.0.1:5000
```

To run test cases -

-   Open terminal in the project directory.

```sh
py.test test.py --cov
```
