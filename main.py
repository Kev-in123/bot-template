import os
import discord
from discord.ext import commands


# Bot constructor, edit this to your needs.
bot = commands.Bot(command_prefix="!")


#loading cogs, you can skip this part if you dont use cogs
[bot.load_extension(f"cogs.{cog[:-3]}") for cog in os.listdir("cogs") if cog.endswith(".py")]

#basic command
@bot.command()
async def command(ctx):
    return await ctx.send("Hi") #sends the message `Hi` to the invoking channel.



bot.run("token") #running a bot like this is not recommended but for the sake of this template, its gonna be like this
