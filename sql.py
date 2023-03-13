import sqlite3
from qiwi_work import *


db = sqlite3.connect('users')
db_qiwi = sqlite3.connect('qiwi')
db_deal = sqlite3.connect('deal')
c = db.cursor()
c_qiwi = db_qiwi.cursor()
c_deal = db_deal.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS users (
    id int,
    stage int,
    bal
)""")
db.commit()
c_qiwi.execute("""CREATE TABLE IF NOT EXISTS qiwi (
    id int,
    url str,
    bill_id str,
    sum int
)""")
db_qiwi.commit()
c_deal.execute("""CREATE TABLE IF NOT EXISTS deal (
    id_1 int,
    id_2 int,
    sum int,
    state int
)""")
db_deal.commit()


class User():
    def __init__(self, id: int):
        self.id = id

        # Занесение пользователя в базу данных, если его там нет
        data_db = c.execute("SELECT id FROM users").fetchall()
        for value in data_db:
            if value[0] == self.id:
                break
        else:
            c.execute("INSERT INTO users VALUES (?, ?, ?)", (self.id, -1, 0))
            db.commit()

    def get_stage(self):
        stage = c.execute("SELECT stage FROM users WHERE id = ?", (self.id,)).fetchone()[0]
        return stage

    def set_stage(self, value: int):
        c.execute("UPDATE users SET stage = ? WHERE id = ?", (value, self.id,))
        db.commit()

    def get_bal(self):
        return int(c.execute("SELECT bal FROM users WHERE id = ?", (self.id,)).fetchone()[0])

    def set_bal(self, value: int):
        c.execute("UPDATE users SET bal = ? WHERE id = ?", (value, self.id,))
        db.commit()

    def add_bal(self, value: int):
        bal = self.get_bal()
        c.execute("UPDATE users SET bal = ? WHERE id = ?", (bal + value, self.id,))
        db.commit()

    def del_bill(self):
        c_qiwi.execute("DELETE FROM qiwi WHERE id = ?", (self.id,))
        db_qiwi.commit()

    async def create_bill(self, sum) -> dict:
        self.del_bill()

        bill = await create_bill_url_from_qiwi(sum)

        c_qiwi.execute("INSERT INTO qiwi VALUES (?, ?, ?, ?)", (self.id, bill.pay_url, bill.id, sum))
        db_qiwi.commit()

        return {'pay_url': bill.pay_url, 'bill_id': bill.id}
    
    def if_exist_bill(self):
        data = c_qiwi.execute("SELECT * FROM qiwi WHERE id = ?", (self.id,)).fetchone()
        return data != None
    
    def get_sum_payment(self):
        data = c_qiwi.execute("SELECT sum FROM qiwi WHERE id = ?", (self.id,)).fetchone()
        return data[0]
    
    def get_bill_id(self):
        data = c_qiwi.execute("SELECT bill_id FROM qiwi WHERE id = ?", (self.id,)).fetchone()
        return data[0]


def exist_user_bd(user_id):
    data_db = c.execute("SELECT id FROM users").fetchall()
    for value in data_db:
        if value[0] == user_id:
            return True
    return False


def can_offer(user_id):
    data = c_deal.execute("SELECT state FROM deal WHERE (id_1 = ? OR id_2 = ?) AND state = 2", (user_id, user_id)).fetchone()
    return data is None


def edit_offer(user_id1, user_id2, sum, state):
    '''1 - предложение
    2 - актуальная сделка'''

    data_db = c_deal.execute("SELECT id_1 FROM deal").fetchall()
    for value in data_db:
        if value[0] == user_id1 or value[0] == user_id2:
            break
    else:
        c_deal.execute("INSERT INTO deal VALUES (?, ?, ?, ?)", (user_id1, user_id2, sum, state))
        db_deal.commit()

    c_deal.execute("UPDATE deal SET state = ? WHERE id_1 = ? AND id_2 = ?", (state, user_id1, user_id2))
    db_deal.commit()


def del_offer(user_id):
    c_deal.execute("DELETE FROM deal WHERE id_1 = ? OR id_2 = ?", (user_id, user_id))
    db_deal.commit()


def can_refuse(user_id):
    data = c_deal.execute("SELECT state FROM deal WHERE id_1 = ? OR id_2 = ?", (user_id, user_id)).fetchone()
    if data is not None:
        return True if data[0] == 1 else False
    return False


def get_offer_state(user_id):
    data = c_deal.execute("SELECT state FROM deal WHERE id_1 = ? OR id_2 = ?", (user_id, user_id)).fetchone()
    if data is not None:
        return data[0]
    else:
        return 0


def get_sum_deal(user_id):
    data = c_deal.execute("SELECT sum FROM deal WHERE id_1 = ? OR id_2 = ?", (user_id, user_id)).fetchone()
    if data is not None:
        return data[0]
    

def get_ids_del(user_id):
    data = c_deal.execute("SELECT id_1, id_2 FROM deal WHERE id_1 = ? OR id_2 = ?", (user_id, user_id)).fetchone()
    if data is not None:
        return [data[0], data[1]]