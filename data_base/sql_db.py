import sqlite3 as sq
from create_bot import dp, bot

def db_start():
    global base, cur
    base = sq.connect("boss.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY)')
    base.execute('CREATE TABLE IF NOT EXISTS master_at_work(master_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS bron(user TEXT, time TEXT, user_name TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS all_masters(id TEXT, photo TEXT, about TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS spam(text TEXT, photo TEXT)')
    base.commit()

async def user_add(message):
    try:
        cur.execute("INSERT INTO users VALUES (?)", (message.from_user.id,))
    except:
        pass
    base.commit()

async def set_master(message):
    try:
        cur.execute("INSERT INTO master_at_work VALUES (?)", (message.from_user.id,))
    except:
        pass
    base.commit()

async def master():
    nobr = cur.execute("SELECT MAX(ROWID) FROM master_at_work").fetchall()
    tobr = cur.execute(f"SELECT master_id FROM master_at_work WHERE ROWID == {nobr[0][0]}").fetchall()
    photo = cur.execute(f"SELECT photo FROM all_masters WHERE id == {tobr[0][0]}").fetchall()
    about = cur.execute(f"SELECT about FROM all_masters WHERE id == {tobr[0][0]}").fetchall()
    return (tobr[0][0], photo[0][0], about[0][0])

async def bron(message):
    cur.execute("INSERT INTO bron VALUES (?, ?, ?)", (message.from_user.id, message.text, message.from_user.username))
    base.commit()
    nobr = cur.execute("SELECT MAX(ROWID) FROM bron").fetchall()
    tobr = cur.execute(f"SELECT time FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    uobr = cur.execute(f"SELECT user FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    name = cur.execute(f"SELECT user_name FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    return (nobr, tobr, uobr, name)

async def bronselect(message):
    user = cur.execute(f"SELECT user FROM bron WHERE ROWID == {message.text} ").fetchall()
    return user

async def spam(data):
    cur.execute("INSERT INTO spam VALUES (?, ?)", (data["text"], data["photo"]))
    base.commit()
    last_spam_num = int(cur.execute("SELECT MAX(ROWID) FROM spam").fetchall()[0][0])
    sp_t = cur.execute(f"SELECT text FROM spam WHERE ROWID == {last_spam_num} ").fetchall()[0][0]
    sp_ph = cur.execute(f"SELECT photo FROM spam WHERE ROWID == {last_spam_num} ").fetchall()[0][0]
    users = cur.execute("SELECT * FROM users").fetchall()
    for i in users:
        await bot.send_message(int(i[0]), sp_t)
        await bot.send_photo(int(i[0]), sp_ph)


async def add_photo(message):
    cur.execute("INSERT INTO all_masters VALUES (?, ?, ?)",
                (message.from_user.id, message.photo[0].file_id, None))
    base.commit()


async def add_name(message):
    last_master_num = int(cur.execute("SELECT MAX(ROWID) FROM all_masters").fetchall()[0][0])
    cur.execute(f"UPDATE all_masters SET about == ? WHERE ROWID == {last_master_num}", (f"{message.text}",))
    base.commit()

