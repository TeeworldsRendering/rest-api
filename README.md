#  👨‍💻 REST API

#### Dependencies

```bash
sudo bash install.sh
```

#### Run

Check inside `app.py`

#### env

Copy `json/env_example.json` to `json/env.json` and replace values 

#### Docker

```bash
APP=rest-api
APP_PORT=9999
docker build -t $APP .
docker run -it -d -p $APP_PORT:1234 $APP
```

##### Running for dev

```bash
docker run -it -p $APP_PORT:1234 -d -v $PWD:/app $APP
```