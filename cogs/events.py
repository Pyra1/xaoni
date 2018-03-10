import discord
import json

from discord.ext.commands import errors

with open("config.json") as f:
    data = json.load(f)


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        _help = await ctx.bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
    else:
        _help = await ctx.bot.formatter.format_help_for(ctx, ctx.command)

    for page in _help:
        await ctx.send(page)


class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            await send_cmd_help(ctx)

        elif isinstance(err, errors.CommandInvokeError):
            await ctx.send(f"There was an error processing the command!\n```diff\n- {err.original}\n```")

        elif isinstance(err, errors.CheckFailure):
            pass

        elif isinstance(err, errors.CommandNotFound):
            pass

    async def on_ready(self):
        print(f'Ready: {self.bot.user} | Guilds: {len(self.bot.guilds)}')
        await self.bot.change_presence(activity=discord.Game(name=f"xa.help | on {len(self.bot.guilds)} servers!"))
	
    async def on_guild_join(self, guild):
        print(f'I have joined a guild! | Guilds: {len(self.bot.guilds)}')
        await self.bot.change_presence(activity=discord.Game(name=f"xa.help | on {len(self.bot.guilds)} servers!"))

    async def on_guild_remove(self, guild):
        print(f'I have been removed from a guild ;-; | Guilds: {len(self.bot.guilds)}')
        await self.bot.change_presence(activity=discord.Game(name=f"xa.help | on {len(self.bot.guilds)} servers!"))

def setup(bot):
    bot.add_cog(Events(bot))
