from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Priya')
bot.set_trainer(ListTrainer)
for files in os.listdir('C:/Users/DELL/Desktop/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/Users/DELL/Desktop/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)

while True:
    message=input('Priya:')
    if message.strip!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip=='Bye' or message.strip=='bye':
        print('ChatBot:It was nice talking to you.Bye')
        break
