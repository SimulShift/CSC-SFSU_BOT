# Imported Libraries
from dotenv import load_dotenv
import os

# Our Libraries
from Bot import Bot

def main():
    load_dotenv() # load .env file

    print('botenv: ', os.getenv('botenv'))

    token = os.getenv('TOKEN')
    bot = Bot(token)

main()
