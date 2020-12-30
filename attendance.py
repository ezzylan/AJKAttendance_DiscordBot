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


def att_link(day, hour):
    link = ""
    # lecture probstats
    if day == 1 and hour == 9:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=335878\nAttendance Lecture ProbStats\nPassword minta kat Dehe"
    # lecture tcs
    elif day == 1 and hour == 15:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=152862\nAttendance Lecture TCS"
    # lecture softmod
    elif day == 2 and hour == 9:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=143231\nAttendance Lecture SoftMod"
    # lecture db
    elif day == 2 and hour == 13:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=332871\nAttendance Lecture Database (Dr Khalit)"
    # lecture project management
    elif day == 3 and hour == 9:
        link = "Attendance Lecture Project Management\nKetua group tutorial korang akan ambik attendance masing2. Jangan lupa hadir kelas ya!"
    # tutorial probstats
    elif day == 3 and hour == 14:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=337476\nAttendance Tutorial ProbStats\nPassword minta kat Dehe"
    # tutorial softmod
    elif day == 4 and hour == 9:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=143231\nAttendance Tutorial SoftMod"
    # tutorial db
    elif day == 4 and hour == 15:
        link = "https://spectrum.um.edu.my/mod/attendance/view.php?id=332912\nAttendance Tutorial Database (Dr Khalit)"
    # tutorial project management
    elif day == 5 and hour == 10:
        link = "Attendance Tutorial Project Management\nKetua group tutorial korang akan ambik attendance masing2. Jangan lupa hadir kelas ya!"
    return link


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            channel = get(guild.text_channels, name='acah-study📚')
            now = dt.datetime.now()
            day = dt.datetime(now.year, now.month, now.day).isoweekday()
            hour = now.hour
            link = att_link(day, hour)
            try:
                message = await channel.send(link)
            except:
                pass
    await client.close()

client.run(TOKEN)
