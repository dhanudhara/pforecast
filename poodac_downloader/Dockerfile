FROM python:3.13-slim

WORKDIR /app
COPY ./app /app
COPY ./requirements.txt .
COPY .netrc /root/.netrc

RUN chmod 600 /root/.netrc
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
