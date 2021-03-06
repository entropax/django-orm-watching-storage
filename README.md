[#](#) Django watching-storage app
Application contains few views which purpose is to connect to remote server
and display data about visitors and their passcodes.
You can obtain database credentials only if you are user of [dvmn](https://dvmn.org).

## How to / setup instructions
#### Firstly download repo, and install requirements
```bash
git clone https://github.com/entropax/django-orm-watching-storage
cd django-orm-watching-storage
poetry install
```

#### Now you need export sercrets env vars for ./project/settings.py
```bash
export DB_URL="postgres://USER:PASSWORD@HOST:PORT/NAME"
export SECRET_KEY="sf0923jf0932fjf09j32f9j"
export DEBUG=false
```
or you can create .env with this fields:
| Field      | Example                                 |
| -----      | ------                                  |
| DB_URL     | postgres://USER:PASSWORD@HOST:PORT/NAME |
| SECRET_KEY | 2fi23vbiobf2...                         |
| DEBUG      | true                                    |

#### Run
```bash
poetry run python main.py runserver 0.0.0.0:8000
```
Then open in browser
[localhost:8000](http://localhost:8000/)

## Project goals
The code is written for educational purposes.
Training course for web-developers [dvmn](https://dvmn.org).
