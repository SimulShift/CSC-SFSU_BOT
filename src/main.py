from Bot import Bot
from TokenLoader import TokenLoader
from dotenv import load_dotenv
import os

def main():
    load_dotenv() # load .env file

    print('botenv: ', os.getenv('botenv'))

    #tl = TokenLoader()
    #bot = Bot(tl.getToken())

    token = os.getenv('TOKEN')
    print(token)
    bot = Bot(token)

main()
