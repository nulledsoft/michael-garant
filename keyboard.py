from vkbottle import Keyboard, KeyboardButtonColor, Text


keyboard_main = Keyboard(one_time=False, inline=False)
keyboard_main.add(Text('Товары', payload={'button': 'goods'}),
                  color=KeyboardButtonColor.SECONDARY)
keyboard_main.row()
keyboard_main.add(Text('Отзывы', payload={'button': 'reviews'}),
                  color=KeyboardButtonColor.SECONDARY)
keyboard_main.add(Text('Поддержка', payload={'button': 'support'}),
                  color=KeyboardButtonColor.SECONDARY)
keyboard_main.row()
keyboard_main.add(Text('Сделка', payload={'button': 'deal'}),
                  color=KeyboardButtonColor.NEGATIVE)
keyboard_main.row()
keyboard_main.add(Text('Баланс', payload={'button': 'balance'}),
                  color=KeyboardButtonColor.POSITIVE)
keyboard_main = keyboard_main.get_json()


keyboard_goods = Keyboard(one_time=False, inline=False)
keyboard_goods.add(Text('Аккаунты роблокс 2010г', payload={'button': 'roblox'}),
                  color=KeyboardButtonColor.PRIMARY)
keyboard_goods.add(Text('Код на Knife Crown', payload={'button': 'two'}),
                  color=KeyboardButtonColor.PRIMARY)
keyboard_goods.row()
keyboard_goods.add(Text('Назад', payload={'button': 'back'}),
                  color=KeyboardButtonColor.NEGATIVE)
keyboard_goods = keyboard_goods.get_json()


keyboard_buy = Keyboard(one_time=False, inline=False)
keyboard_buy.add(Text('Купить (проверить оплату)', payload={'button': 'buy'}),
                  color=KeyboardButtonColor.PRIMARY)
keyboard_buy.row()
keyboard_buy.add(Text('Назад', payload={'button': 'back'}),
                  color=KeyboardButtonColor.POSITIVE)
keyboard_roblox = keyboard_buy.get_json()


keyboard_balance = Keyboard(one_time=False, inline=False)
keyboard_balance.add(Text('Мой баланс', payload={'button': 'check'}),
                  color=KeyboardButtonColor.PRIMARY)
keyboard_balance.row()
keyboard_balance.add(Text('Пополнение', payload={'button': '+'}),
                  color=KeyboardButtonColor.POSITIVE)
keyboard_balance.add(Text('Вывод', payload={'button': '-'}),
                  color=KeyboardButtonColor.SECONDARY)
keyboard_balance.row()
keyboard_balance.add(Text('Назад', payload={'button': 'back'}),
                  color=KeyboardButtonColor.NEGATIVE)
keyboard_balance = keyboard_balance.get_json()


keyboard_back = Keyboard(one_time=False, inline=False)
keyboard_back.add(Text('Назад', payload={'button': 'back'}),
                  color=KeyboardButtonColor.NEGATIVE)
keyboard_back = keyboard_back.get_json()


keyboard_deal_1 = Keyboard(one_time=False, inline=False)
keyboard_deal_1.add(Text('Предложить сделку', payload={'button': 'offer'}),
                  color=KeyboardButtonColor.POSITIVE)
keyboard_deal_1.row()
keyboard_deal_1.add(Text('Назад', payload={'button': 'back'}),
                  color=KeyboardButtonColor.NEGATIVE)
keyboard_deal_1 = keyboard_deal_1.get_json()


keyboard_deal_2 = Keyboard(one_time=False, inline=True)
keyboard_deal_2.add(Text('Принять', payload={'button': 'accept_deal'}),
                  color=KeyboardButtonColor.POSITIVE)
keyboard_deal_2.add(Text('Отказаться', payload={'button': 'deny_deal'}),
                  color=KeyboardButtonColor.NEGATIVE)
keyboard_deal_2 = keyboard_deal_2.get_json()


keyboard_deal_3 = Keyboard(one_time=False, inline=True)
keyboard_deal_3.add(Text('Отозвать предложение', payload={'button': 'revoke_deal'}),
                  color=KeyboardButtonColor.SECONDARY)
keyboard_deal_3 = keyboard_deal_3.get_json()


keyboard_deal_4 = Keyboard(one_time=False, inline=False)
keyboard_deal_4.add(Text('Закончить сделку', payload={'button': 'finish_deal'}),
                  color=KeyboardButtonColor.SECONDARY)
keyboard_deal_4 = keyboard_deal_4.get_json()