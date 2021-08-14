from Bot import Bot
from TokenLoader import TokenLoader

def main():

    tl = TokenLoader()
    bot = Bot(tl.getToken())

main()