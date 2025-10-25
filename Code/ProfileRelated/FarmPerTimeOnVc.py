from discord.ext import commands
import sqlite3

conn = sqlite3.connect('main.users.db')
cursor = conn.cursor()

data = [

]

class FarmPerTimeOnVc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot