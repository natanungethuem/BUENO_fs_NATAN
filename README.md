# Ecore Test

This project is authored by Natan Bueno.

## package.json
- `docker:build`: Builds all Docker services defined in `docker-compose.yml`.
- `docker:build:backend`: Builds the `backend` Docker service.
- `docker:build:db`: Builds the `db` Docker service.
- `docker:build:frontend`: Builds the `frontend` Docker service.
- `docker:run`: Runs all Docker services.
- `docker:run:backend`: Runs the `backend` Docker service in detached mode.
- `docker:run:db`: Runs the `db` Docker service in detached mode.
- `docker:run:frontend`: Runs the `frontend` Docker service in detached mode.

## backend/package.json
- `install:python`: Installs the Python dependencies listed in `requirements.txt`.
- `lint:python`: Runs pylint on all Python files in the project.
- `lint:python:fix`: Runs autopep8 on all Python files in the project, modifying the files in place to fix any issues.

## frontend/package.json
- `start`: Starts the development server.
- `build`: Builds the app for production.
- `test`: Runs the test watcher in an interactive mode.
- `eject`: Removes this tool and copies build dependencies, configuration files and scripts into the app directory.
- `install:node`: Deletes the `node_modules` directory and `package-lock.json` file, then runs `npm i`.

You can run these scripts with `npm run <script-name>`. For example, to build all Docker services, you would run `npm run docker:build`.

## Database

- We did not use foreign keys constraints in the database. Applications like Oracle Retail, for example, do not use this type of constraints to avoid performance loss