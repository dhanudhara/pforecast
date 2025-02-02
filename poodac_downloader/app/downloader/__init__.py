import subprocess


def download_data(
    coll: str,
    dest: str,
    min: int
) -> tuple[int, Exception | None]:
    command = [
        'podaac-data-subscriber',
        '-c', coll,
        '-d', dest,
        '-m', str(min)
    ]
    try:
        subprocess.run(command, check=True)
        return (0, None)
    except subprocess.CalledProcessError as e:
        return (1, e)
