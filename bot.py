from vkbottle import Bot
from routes import labelers


token = '3dc07eac9a76d92387b9da1fd9440998814fd51f5e056f0da586d3a6c485a5c554014d5840e4d7ff699fb'
bot = Bot(token)


for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)


bot.run_forever()