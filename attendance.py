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
    # lecture operating systems
    if day == 1 and hour == 11:
        link = "\nAttendance Lecture OS\n<@625611854777024513>"
    # lecture sre
    elif day == 1 and hour == 16:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427972\nAttendance Lecture SRE\n<@625611854777024513>"
    # lecture hci
    elif day == 2 and hour == 9:
        link = "Attendance Lecture HCI\nDr akan ambik attendance dari Teams. Jangan lupa hadir kelas!\n<@625611854777024513>"
    # tutorial sre
    elif day == 2 and hour == 12:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427972\nAttendance Tutorial SRE\n<@625611854777024513>"
    # lecture algo
    elif day == 2 and hour == 15:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427681\nAttendance Lecture Algo\nPassword Dr bagi kat chat Teams\n<@625611854777024513>"
    # lecture web programming
    elif day == 3 and hour == 11:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=158033\nAttendance Lecture Web Programming\nPassword Dr bagi kat chat Teams\n<@625611854777024513>"
    # tutorial operating systems
    elif day == 3 and hour == 14:
        link = "\nAttendance Tutorial OS\n<@625611854777024513>"
    # tutorial algo
    elif day == 4 and hour == 9:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=427681\nAttendance Tutorial Algo\nPassword Dr bagi kat chat Teams\n<@625611854777024513>"
    # tutorial hci
    elif day == 4 and hour == 16:
        link = "Attendance Tutorial HCI\nDr akan ambik attendance dari Teams. Jangan lupa hadir kelas!\n<@625611854777024513>"
    # tutorial web programming
    elif day == 5 and hour == 15:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=158033\nAttendance Tutorial Web Programming\nPassword Dr bagi kat chat Teams\n<@625611854777024513>"
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
