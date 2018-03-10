import time
import discord
import psutil
import os

from discord.ext import commands
from utils import repo


class Info:
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        message = await ctx.send("Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong! | {int(ping)}ms")

    @commands.command()
    async def invite(self, ctx):
        """ Invite me to your server """
        await ctx.send(f"**{ctx.author.name}**, use this URL to invite me\nhttps://discordapp.com/oauth2/authorize?client_id=421726755405955073&scope=bot&permissions=8")

    @commands.command(aliases=['supportserver', 'feedbackserver'])
    async def botserver(self, ctx):
        """ Get an invite to our support server! """
        if isinstance(ctx.channel, discord.DMChannel):
            return await ctx.send(f"**Here you go {ctx.author.name} \n<{repo.invite}>**")

    @commands.command(aliases=['info', 'stats'])
    async def about(self, ctx):
        """ About the bot """
        ramUsage = self.process.memory_full_info().rss / 1024**2

        embed = discord.Embed(colour=0xC29FAF)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="Arceros", value="by Pyra_", inline=True)
        embed.add_field(name="Help & Test command", value="xa.help, xa.ping", inline=True)
        embed.add_field(name="Framework", value="discord.py 1.0.0a | Python 3.6.4", inline=True)
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"About **Xaoni** | **{repo.version}**", embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
