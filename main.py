from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord, spacy, thinc, wikipedia

chatbot = ChatBot('Katlyn')
trainer = ChatterBotCorpusTrainer(chatbot)

class Client(discord.Client):
    async def on_ready(self):
        print('Connected to Discord!')
        trainer.train("chatterbot.corpus.english")
        trainer.train("chatterbot.corpus.english.greetings")
        trainer.train("chatterbot.corpus.english.conversations")
    async def on_message(self,message):
        chatbot.get_response(message.clean_content)
        if isinstance(message.channel, discord.channel.DMChannel):
            if(not message.author.bot):
                async with message.channel.typing():
                    chatbot.get_response(wikipedia.summary(wikipedia.search(message.clean_content)[0]))
                    await message.channel.send(chatbot.get_response(message.clean_content))
client = Client()
client.run('token')
