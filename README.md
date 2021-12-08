# How to setup

- `$ docker-compose up -d`
  - startup the web container and the api container
- `$ docker-compose exec web bash`
  - login to the web-server container
- `$ cd kono-chat`
  - change the current working directory
- `$ yarn install --frozen-lockfile`
  - install packages listed in yarn.lock

# How to use to develop

- `$ docker-compose up -d`
- `$ docker-compose exec web bash`
- `$ cd kono-chat`
- `$ yarn serve`
- Open `http://localhost:8080` in your browser
