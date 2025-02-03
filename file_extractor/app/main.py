import extract
import tabulate

import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log(err):
    with open('/app/logs/err', 'a') as err_file:
        err_file.write(f"{type(err)}: {err}\n")


def write(msg: str):
    with open('/app/logs/log', 'a') as log_file:
        log_file.write(msg)


class WatchPoodacDownloads(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.nc'):
            try:
                write("Attempting to tabulate")
                df = extract.get_dataframe(path=str(event.src_path))
                tabulate.tabulate(df=df)
                write("Tabulation completed")
            except Exception as e:
                log(err=e)


if __name__ == "__main__":
    path = "/app/tmp"
    event_handler = WatchPoodacDownloads()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
