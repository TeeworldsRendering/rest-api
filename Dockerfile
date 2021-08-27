FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:1234", "app"]

# docker build -t tw-api .
# docker run -it -v $PWD:/app -p 1234:1234 tw-api