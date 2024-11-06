# Telegram Bot Python with Google Sheets

📌 This project demonstrates the creation of a simple Telegram bot based on the AIOGRAM 3 framework with SQLite database integration and uploading data to Google Tables.

## Enable API Access for a Project

### Creating a new Telegram Bot

Use the `/newbot` command to create a new bot. [@BotFather](https://t.me/botfather) will ask you for a name and username, then generate an authentication token for your new bot.

* **The name** of your bot is displayed in contact details and elsewhere.
* **The username** is a short name, used in search, mentions and t.me links. Usernames are 5-32 characters long and not case sensitive – but may only include Latin characters, numbers, and underscores. Your bot's username must end in 'bot’, like 'tetris_bot' or 'TetrisBot'.
* **The token** is a string, like `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`, which is required to authorize the bot and send requests to the Bot API. Keep your token secure and store it safely, it can be used by anyone to control your bot.

> Unlike the bot’s name, the username cannot be changed later – so choose it carefully.
When sending a request to api.telegram.org, remember to prefix the word ‘bot’ to your token.

### Google Sheets

1. Head to [Google Developers Console](https://console.developers.google.com/) and create a new project (or select the one you already have).
2. In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.
3. In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.
4. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
5. Fill out the form
6. Click “Create” and “Done”.
7. Press “Manage service accounts” above Service Accounts.
8. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
9. Select JSON key type and press “Create”.

You will automatically download a JSON file with credentials. It may look like this:

```json
{
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}
```

## Install

To install the necessary dependencies, run the following commands:

```bash
pip install -r requirements.txt
```

requirements.txt it contains the following dependencies:

```
aiogram==3.13.1
gspread==6.1.2
oauth2client==4.1.3
pandas==2.2.3
pydantic==2.9.2
pydantic_settings==2.5.2
python-decouple==3.8
python-dotenv==1.0.1
```

Create a file .env in the root of the project and add the following variables to it:

```
BOT_TOKEN=
TYPE=service_account
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\n\n-----END PRIVATE KEY-----\n
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
UNIVERSE_DOMAIN=
```

## Launching the bot:

```bash
python bot.py
```

## Project structure:

```
project/
│
├── googlesheets/
│   ├── __init__.py: Initializing the module
│   ├── base.csv: File for exporting the database to Google Tables
│   ├── db_users.py: Functions for interacting with SQLite
│   └── my_database.db: SQLite Database
│
├── handlers/
│   ├── __init__.py: Initializing the module
│   ├── start_questions.py: Router to start communicating with a bot
│   └── submit_application.py: Router for filling out the application
│
├── keyboards
│   ├── __init__.py: Initializing the module
│   └── kbs.py: A file with all keyboards
│
├── .env: File with environment variables for configuration
├── bot.py: Main file for launching the bot
├── gs_gen.py: Configuration file for connecting to the Google Tables API
└── requirements.txt: File with project dependencies
```