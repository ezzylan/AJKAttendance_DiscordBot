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


def att_link(day, hour, min):
    link = ""
    if day == 4 and hour == 14 and min == 28:
        link = "afiq irfan padu wild rift"
    return link


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            channel = get(guild.text_channels, name='another-one')
            now = dt.datetime.now()
            day = dt.datetime(now.year, now.month, now.day).isoweekday()
            hour = now.hour
            min = now.minute
            link = att_link(day, hour, min)
            message = await channel.send(link)
    await client.close()

client.run(TOKEN)
