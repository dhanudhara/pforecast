from time import sleep

import downloader


def main(coll: str, dest: str, min: int) -> None:
    while True:
        status, err = downloader.download_data(
            coll=coll,
            dest=dest,
            min=min
        )
        if status:
            with open('/app/logs/err', 'a') as err_file:
                err_file.write(f"{type(err)}: {err}\n")
            sleep(10)  # retry after 10s
            continue
        sleep(min*60)


if __name__ == "__main__":
    collection = "CYGNSS_L3_MICROPLASTIC_V3.2"
    destination = "/app/tmp"
    minute = 360
    main(collection, destination, minute)
