import discord

class Bot(discord.Client):
    def __init__(self, token, *args, **kwargs):

        # set up stuff
        super().__init__(*args, **kwargs)   # since Bot is a subclass of discord.Client, we gotta call its parents' ctors, ignore args

        # start execution
        self.run(token)

    async def onReady(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
