import time
import subprocess

from utils import repo
from discord.ext import commands


class Admin:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    @commands.command()
    @commands.check(repo.is_owner)
    async def restart(self, ctx):
        """ Restart the bot """
        await ctx.send('Rebooting now...')
        time.sleep(1)
        await self.bot.logout()

    @commands.command(aliases=['exec'])
    @commands.check(repo.is_owner)
    async def execute(self, ctx, *, text: str):
        """ Do a shell command. """
        text_parsed = list(filter(None, text.split(" ")))
        output = subprocess.check_output(text_parsed).decode()
        await ctx.send(f"```fix\n{output}\n```")


def setup(bot):
    bot.add_cog(Admin(bot))
