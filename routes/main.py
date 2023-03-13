from vkbottle.bot import BotLabeler, Message
from sql import *
from keyboard import *
from text import *
from vkbottle.api import API
from upload_acc import *
import re


token = '3dc07eac9a76d92387b9da1fd9440998814fd51f5e056f0da586d3a6c485a5c554014d5840e4d7ff699fb'
api = API(token)
bl = BotLabeler()


@bl.private_message()
async def handler(event: Message):
    user = User(event.from_id)
    stage = user.get_stage()
    text = event.text.lower()
    payload = eval(event.payload)['button'] if event.payload is not None else ''

    if payload not in ['accept_deal', 'deny_deal', 'revoke_deal', 'finish_deal']:
        if stage == -1:
            await event.answer(
                main_text, keyboard=keyboard_main)
            user.set_stage(0)

        elif stage == 0:
            if payload == 'goods':
                await event.answer('Доступные товары 🤩\n┍━━━━╝✹╚━━━━┑\n\n-Аккаунты 2010 года без привязки\n────────────────────────\n-Роблокс код на Knife Crown\n\n┕━━━━╗✹╔━━━━┙\n────────────────────────\nЕсли вы желаете приобрести товар , нажмите на кнопку ниже !', keyboard=keyboard_goods)
                user.set_stage(1)
            elif payload == 'reviews':
                await event.answer('Отзывы можно почитать тут:\n\nhttps://vk.com/topic-216927388_49100396.')
            elif payload == 'deal':
                await event.answer('Выберите нужное действие:', keyboard=keyboard_deal_1)
                user.set_stage(6)
            elif payload == 'balance':
                await event.answer('Выберите нужное действие:', keyboard=keyboard_balance)
                user.set_stage(3)
            elif payload == 'support':
                await event.answer('Я уже позвал администратора')
                await api.messages.send(user_id=565182159, message='юзер вызвал сапорта', random_id=0)
                await api.messages.send(user_id=368091513, message='юзер вызвал сапорта', random_id=0)
            else:
                await event.answer('Выберите одно из предложенных действий.')
        
        # Аккаунты
        elif stage == 1:
            if payload == 'roblox':
                await event.answer(roblox_text, keyboard=keyboard_buy)
                user.set_stage(2)
            elif payload == 'two':
                await event.answer(knife_text, keyboard=keyboard_buy)
                user.set_stage(5)
            elif payload == 'back':
                await event.answer('Доступное меню:', keyboard=keyboard_main)
                user.set_stage(0)

        elif stage == 5:
            if payload == 'buy':
                if user.get_bal() >= 15:
                    get_acc = get_account2()
                    if get_acc is not None:
                        user.set_bal(user.get_bal() - 15)
                        await event.answer(f'Ваш аккаунт: {get_acc}')
                        await event.answer('Не забудьте сменить пароль и привязать почту. И пожалуйста, оставьте отзыв. Нам очень важно ваше мнение, и как вы оцениваете нашу работу ❤ https://vk.com/topic-216927388_49100396')
                    else:
                        await event.answer('В данный момент аккаунтов нет в наличии.')
                else:
                    await event.answer('Недостаточно средств на балансе.')

            elif payload == 'back':
                await event.answer('Доступные товары:', keyboard=keyboard_goods)
                user.set_stage(1)

        # Аккаунты роблокс
        elif stage == 2:
            if payload == 'buy':
                if user.get_bal() >= 15:
                    get_acc = get_account()
                    if get_acc is not None:
                        user.set_bal(user.get_bal() - 15)
                        await event.answer(f'Ваш аккаунт: {get_acc}')
                        await event.answer('Пожалуйста, оставьте отзыв. Нам очень важно ваше мнение, и как вы оцениваете нашу работу ❤ https://vk.com/topic-216927388_49100396')
                    else:
                        await event.answer('В данный момент ключей нет в наличии.')
                else:
                    await event.answer('Недостаточно средств на балансе.')

            elif payload == 'back':
                await event.answer('Доступные товары:', keyboard=keyboard_goods)
                user.set_stage(1)

        # Баланс
        elif stage == 3:
            if payload == 'check':
                if user.if_exist_bill():
                    paid = await check_pay_bill(user.get_bill_id())
                    if paid:
                        sum = user.get_sum_payment()
                        user.add_bal(sum)
                        user.del_bill()
                        await event.answer(f'Пополнение на {sum} р.')
                await event.answer(f'Ваш баланс: {user.get_bal()} р.') 

            elif payload == '+':
                await event.answer('Введите сумму.', keyboard=keyboard_back)
                user.set_stage(4)

            elif payload == '-':
                await event.answer('Для вывода средств обратитесь к администратору: Михаилу.')
        
            elif payload == 'back':
                await event.answer('Доступное меню:', keyboard=keyboard_main)
                user.set_stage(0)

        # Пополнение баланса
        elif stage == 4:
            if payload == '':
                if event.text.isdigit():
                    bill = await user.create_bill(int(event.text))
                    await event.answer(f'Ссылка для оплаты: {bill["pay_url"]}.\nСумма: {event.text} р.\n\nОплата должна быть строго проведена по последней созданной ссылке. После оплаты зайдите в раздел "Баланс" и нажмите на кнопку "Мой баланс".')
                else:
                    await event.answer('Сумма должна являться целым числом.')

            elif payload == 'back':
                await event.answer('Выберите нужное действие:', keyboard=keyboard_balance)
                user.set_stage(3)
        
        elif stage == 6:
            if payload == 'offer':
                await event.answer('Введите ссылку на человека и сумму через пробел, с кем хотите заключить сделку.\n\nПример: @durov 25', keyboard=keyboard_back)
                user.set_stage(7)
            elif payload == 'back':
                await event.answer('Доступное меню:', keyboard=keyboard_main)
                user.set_stage(0)
        
        elif stage == 7:
            if payload == 'back':
                await event.answer('Выберите нужное действие:', keyboard=keyboard_deal_1)
                user.set_stage(6)
            if payload == '':
                args = event.text.split()
                if len(args) > 1:
                    if args[1].isdigit():
                        if int(args[1]) > 0:
                            m = re.search(r'([a-zA-Z0-9._])+$', args[0])
                            get_user2 = await api.users.get(m[0])
                            # Если такая страница есть
                            if get_user2 != []:
                                target_id = get_user2[0].id
                                if exist_user_bd(target_id):
                                    if can_offer(target_id):
                                        if user.get_bal() >= int(args[1]):
                                            edit_offer(event.from_id, target_id, int(args[1]), 1)
                                            get_user1 = await api.users.get(event.from_id, name_case='gen')
                                            await api.messages.send(peer_id=target_id, message=f'Вам поступило предложение о заключении сделки от [id{event.from_id}|{get_user1[0].first_name} {get_user1[0].last_name}]. По итогу сделки вы получите {args[1]} р.', random_id=0, keyboard=keyboard_deal_2)
                                            await event.answer('Предложение отправлено.', keyboard=keyboard_deal_3)
                                        else:
                                            await event.answer('Недостаточно средств на балансе.')
                                else:
                                    await event.answer('Такой человек не зарегистрирован в боте.')
                            else:
                                await event.answer('Страница такого человека не найдена.')
                        else:
                            await event.answer('Сумма должна быть положительным числом.')
                    else:
                        await event.answer('Сумма должна являться целым числом.')
            else:
                await event.answer('Введите ссылку на человека, с которым хотите заключить сделку, и сумму через пробел.\n\nПример: @durov 25')

        elif stage == 10:
            if payload == '':
                if event.text != '':
                    deal_members = get_ids_del(event.from_id)
                    await api.messages.send(peer_id=deal_members[0] if deal_members[0] != event.from_id else deal_members[1], message=f'Собеседник: {event.text}', random_id=0)
                else:
                    await event.answer('Сообщение не должно быть пустым.')

    elif payload == 'accept_deal':
        if get_offer_state(event.from_id) == 1:
            deal_members = get_ids_del(event.from_id)
            user_1 = User(deal_members[0])
            user_2 = User(deal_members[1])
            sum_deal = get_sum_deal(deal_members[0])

            if user_1.get_bal() >= sum_deal:
                user_1.set_bal(user_1.get_bal() - sum_deal)
                await event.answer('Сделка принята.\n\nВсе сообщения, отправленные здесь, отправляются человеку, который ведет с вами сделку.', keyboard=keyboard_deal_4)
                
                get_user1 = await api.users.get(event.from_id)
                await api.messages.send(peer_id=deal_members[0], message=f'[id{event.from_id}|{get_user1[0].first_name} {get_user1[0].last_name}] принял/а ваше предложение о сделке.', random_id=0, keyboard=keyboard_deal_4)
                user_1.set_stage(10)
                user_2.set_stage(10)

                edit_offer(deal_members[0], deal_members[1], sum_deal, 2)
            else:
                await event.answer('На балансе человека, отправившего предложение, недостаточно средств для заключения сделки. Сделка отменена.')
                del_offer(event.from_id)
        else:
            await event.answer('В данный момент предложение не может быть отклонено.')

    elif payload == 'deny_deal':
        if get_offer_state(event.from_id) == 1:
            deal_members = get_ids_del(event.from_id)
            user_1 = User(deal_members[0])
            user_2 = User(deal_members[1])
            del_offer(event.from_id)
            await event.answer('Предложение о сделке отклонено.')

            get_user1 = await api.users.get(event.from_id)
            await api.messages.send(peer_id=deal_members[0], message=f'[id{event.from_id}|{get_user1[0].first_name} {get_user1[0].last_name}] отклонил/а ваше предложение о сделке.', random_id=0)
        else:
            await event.answer('В данный момент предложение не может быть отклонено.')

    elif payload == 'finish_deal':
        if get_offer_state(event.from_id) == 2:
            deal_members = get_ids_del(event.from_id)
            user_1 = User(deal_members[0])
            user_2 = User(deal_members[1])
            
            get_user1 = await api.users.get(event.from_id)
            await api.messages.send(peer_id=deal_members[0], message=f'Сделка прекращена. Деньги отправлены.', random_id=0, keyboard=keyboard_balance)
            await api.messages.send(peer_id=deal_members[1], message=f'Сделка прекращена. Вы получили {get_sum_deal(deal_members[1])} р.', random_id=0, keyboard=keyboard_balance)
            
            user_2.set_bal(user_2.get_bal() + get_sum_deal(deal_members[1]))
            del_offer(event.from_id)

            user_1.set_stage(3)
            user_2.set_stage(3)
        else:
            await event.answer('В данный момент сделка не может быть прекращена.')

    elif payload == 'revoke_deal':
        if get_offer_state(event.from_id) == 1:
            await event.answer('Предложение о заключении сделки отозвано.', keyboard=keyboard_deal_1)
            user.set_stage(6)
            del_offer(event.from_id)
        else:
            await event.answer('В данный момент предложение не может быть отозвано.')