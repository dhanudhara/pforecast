# Plastic monitoring and forecasting

## Prerequisites

- Docker

### MySQL environment variables

- Create secrets file:

```sh
mkdir .secrets && touch .secrets/db_root_password.txt
```

- add root password to this txt file

## Launch system

Run:

```sh
$ docker compose up -d
# or
$ docker compose up -d --build  # to rebuild files
```

## Modules

- data downloader (poodac)
- data converter and tabulator (ncextract)
- data forecaster (wrf?)
- api endpoint
