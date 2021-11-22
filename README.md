# Django watching-storage app
Application contains few views which purpose is to connect to remote server
and display data about visits and passcodes.
You can obtain database credentials only if you are user of [dvmn](https://dvmn.org).

## Usage
* Setup instractions:
clone this repo, than
```bash
source pyenv/bin/activate
pip install -r requirements.txt
```

* Update ./project/settings.py file (example.env provided)
    * HOST
    * PORT
    * NAME(database name)
    * USER
    * PASSWORD
    * SECRET_KEY
    * DEBUG

* Run application
```bash
python main.py
```
Then open in browser
```bash
http://localhost:8000/
```
## Project goals
The code is written for educational purposes.
Training course for web-developers [dvmn](https://dvmn.org).
