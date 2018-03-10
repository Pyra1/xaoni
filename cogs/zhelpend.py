#Used to allow music cog at end of help
import discord
from discord.ext import commands

class zhelpend:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(zhelpend(bot))
