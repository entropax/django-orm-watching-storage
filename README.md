# Django watching-storage app
Application contains few views which purpose is to connect to remote server
and display data about visitors and their passcodes.
You can obtain database credentials only if you are user of [dvmn](https://dvmn.org).

## How to / setup instructions
#### Firstly download repo, get your virtual env and install requirements
```bash
git clone https://github.com/entropax/django-orm-watching-storage
cd django-orm-watching-storage
pyhton -m venv install .
source pyenv/bin/activate
pip install -r requirements.txt
```

#### Then you need to update ./project/settings.py file like this:
| Field               | Example         |
| -----               | ------          |
| HOST                | host.host.ort   |
| PORT                | 5434            |
| NAME(database name) | name            |
| USER                | guard           |
| PASSWORD            | beStpa6@rd      |
| SECRET_KEY          | 2fi23vbiobf2... |
| DEBUG               | True            |

#### Run
```bash
python main.py
```
Then open in browser
```bash
(http://localhost:8000/)[http://localhost:8000/]
```
## Project goals
The code is written for educational purposes.
Training course for web-developers [dvmn](https://dvmn.org).
