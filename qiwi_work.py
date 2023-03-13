import asyncio
from glQiwiApi import QiwiWrapper
import time

secret_qiwi = ''


async def p2p_usage():
    async with QiwiWrapper(secret_p2p=secret_qiwi) as w:

        bill = await w.create_p2p_bill(amount=199, comment='')
        print(f'Ссылка: {bill.pay_url}\nИд: {bill.id}')

        status = (await w.check_p2p_bill_status(bill_id=bill.id)) == 'PAID'
        print(status)


async def create_bill_url_from_qiwi(sum):
    async with QiwiWrapper(secret_p2p=secret_qiwi) as w:

        bill = await w.create_p2p_bill(amount=sum, comment='')

    return bill


async def check_pay_bill(bill_id):
    async with QiwiWrapper(secret_p2p=secret_qiwi) as w:
        status = (await w.check_p2p_bill_status(bill_id=bill_id)) == 'PAID'

    return status

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(p2p_usage())
