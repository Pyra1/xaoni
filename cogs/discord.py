import discord
from io import BytesIO

from utils import default
from discord.ext import commands


class Discord:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=0xC29FAF)
        embed.description = f"Avatar to **{user.name}**\nClick [here]({user.avatar_url}) to get image"
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def server(self, ctx):
        """ Check info about current server """
        if ctx.invoked_subcommand is None:
            findbots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed()
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            embed.add_field(name="Created", value=default.date(ctx.guild.created_at), inline=True)
            await ctx.send(content=f"Information about **{ctx.guild.name}**", embed=embed)

    @commands.command()
    async def user(self, ctx, user: discord.Member = None):
        """ Get user information """
        if user is None:
            user = ctx.author

        embed = discord.Embed()
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)

        if hasattr(user, "nick"):
            embed.add_field(name="Nickname", value=user.nick, inline=True)
        else:
            embed.add_field(name="Nickname", value="None", inline=True)

        embed.add_field(name="Account created", value=default.date(user.created_at), inline=True)

        if hasattr(user, "joined_at"):
            embed.add_field(name="Joined this server", value=default.date(user.joined_at), inline=True)

        await ctx.send(content=f"ℹ About **{user.id}**", embed=embed)


def setup(bot):
    bot.add_cog(Discord(bot))
