# Ecore Test

This project is authored by Natan Bueno.

## Scripts

Here are the npm scripts you can run:

- `install:node`: Deletes the `node_modules` directory and `package-lock.json` file, then runs `npm i`.
- `install:python`: Installs the Python dependencies listed in `backend/requirements.txt`.
- `lint:python`: Runs pylint on all Python files in the `backend` directory.
- `lint:python:fix`: Runs autopep8 on all Python files in the `backend` directory, modifying the files in place to fix any issues.
- `docker:build`: Builds all Docker services defined in `docker-compose.yml`.
- `docker:build:backend`: Builds the `backend` Docker service.
- `docker:build:db`: Builds the `db` Docker service.
- `docker:build:frontend`: Builds the `frontend` Docker service.
- `docker:run`: Runs all Docker services.
- `docker:run:backend`: Runs the `backend` Docker service in detached mode.
- `docker:run:db`: Runs the `db` Docker service in detached mode.
- `docker:run:frontend`: Runs the `frontend` Docker service in detached mode.

You can run these scripts with `npm run <script-name>`. For example, to build all Docker services, you would run `npm run docker:build`.