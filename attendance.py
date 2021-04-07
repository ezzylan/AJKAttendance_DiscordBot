# bot.py
import os
import datetime as dt
import discord
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


def att_link(day, hour, days_left):
    link = ""
    myID = "<@625611854777024513>"
    # lecture operating systems
    if day == 1 and hour == 11:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427762\nAttendance Lecture OS\n"+myID
    # lecture sre
    elif day == 1 and hour == 16:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427972\nAttendance Lecture SRE\n"+myID
    # lecture hci
    elif day == 2 and hour == 9:
        link = "Attendance Lecture HCI\nDr akan ambik attendance dari Teams. Jangan lupa hadir kelas!\n"+myID
    # tutorial sre
    elif day == 2 and hour == 12:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427972\nAttendance Tutorial SRE\n"+myID
    # lecture algo
    elif day == 2 and hour == 15:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427681\nAttendance Lecture Algo\nPassword Dr bagi kat chat Teams\n"+myID
    # lecture web programming
    elif day == 3 and hour == 11:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=158033\nAttendance Lecture Web Programming\nPassword Dr bagi kat chat Teams\n"+myID
    # tutorial operating systems
    elif day == 3 and hour == 14:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427762\nAttendance Tutorial OS\n"+myID
    # tutorial algo
    elif day == 4 and hour == 9:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427681\nAttendance Tutorial Algo\nPassword Dr bagi kat chat Teams\n"+myID
    # tutorial hci
    elif day == 4 and hour == 16:
        link = "Attendance Tutorial HCI\nDr akan ambik attendance dari Teams. Jangan lupa hadir kelas!\n"+myID
    # tutorial web programming
    elif day == 5 and hour == 15:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=158033\nAttendance Tutorial Web Programming\nPassword Dr bagi kat chat Teams\n"+myID
    # see you next sem
    elif hour == 0 and days_left == 0:
        link = "Tamatlah khidmat saya untuk sem ni. See you next sem! 😉"
    return link


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            channel = get(guild.text_channels, name='attendance-📝')
            now = dt.datetime.now()
            end = dt.datetime(year=2021, month=6, day=19)
            days_left = (end - now).days
            if days_left > 0:
                day = dt.datetime(now.year, now.month, now.day).isoweekday()
                hour = now.hour
                link = att_link(day, hour, days_left)
                try:
                    await channel.send(link)
                except:
                    pass
    await client.close()

client.run(TOKEN)
