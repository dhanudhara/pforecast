# Plastic monitoring and forecasting

## Prerequisites

- Docker

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
