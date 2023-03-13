from vkbottle.bot import BotLabeler, Message
from vkbottle.api import API
import re
from sql import *


token = '3dc07eac9a76d92387b9da1fd9440998814fd51f5e056f0da586d3a6c485a5c554014d5840e4d7ff699fb'
api = API(token)
bl = BotLabeler()
admins = [290904066]


commands = [
    '!bal set <url> <amount>', '!bal', 'bal set', 'bal set <url>',
    't <url>'
]

@bl.private_message(text=commands)
async def handler(event: Message, url=None, amount=None):
    text = event.text.lower()
    
    if text.startswith('!bal'):
        if 'set' in text:
            m = re.search(r'([a-zA-Z0-9._])+$', url)
            get_user = await api.users.get(m[0], name_case='gen')

            user_name = f'[id{get_user[0].id}|{get_user[0].first_name} {get_user[0].last_name}]'
            user = User(get_user[0].id)
            user.set_bal(amount)
            
            await event.answer(f'Баланс {user_name} установлен на: {amount} р.')