import discord

from UserProfile import UserProfile

class Bot(discord.Client):
    
    def __init__(self, token, *args, **kwargs):

        # set up stuff
        super().__init__(*args, **kwargs)   # since Bot is a subclass of discord.Client, we gotta call its parents' ctors, ignore args

        self.profiles = {} # empty dictionary

        # start execution
        self.run(token)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # the channel the message was sent in
        activeChannel = message.channel
        isNotOurMessage = message.author.id != self.user.id

        # this could all be made into a function
        pottyLanguage = [
            "swag"
        ]

        containsPotty = False

        for pottyWord in pottyLanguage:
            if pottyWord in message.content:
                containsPotty = True

        # if the incoming message wasnt sent by the bot
        if (isNotOurMessage):

            if (containsPotty):

                senderID = message.author.id

                if (senderID in self.profiles):
                    self.profiles[senderID].strikes += 1        # if we have a profile on this user, edit existing values
                else:
                    self.profiles[senderID] = UserProfile()     # else, create a profile for them

                SWAG_FACTOR = 2
                swagCounter = ":moneybag:"

                for i in range(self.profiles[senderID].strikes):
                    swagCounter *= 2

                await message.channel.send(swagCounter)