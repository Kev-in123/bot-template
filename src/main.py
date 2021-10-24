import os
import discord
from discord.ext import commands

# bot constructor, edit this to your needs.
bot = commands.Bot(command_prefix="!")

#basic command
@bot.command()
async def hi(ctx):
    await ctx.send("Hi") # sends the message `Hi` to the invoking channel.

# loading all the cogs, you can skip this part if you dont use cogs or manually load all the cogs
for cog in os.listdir("cogs"):
  if cog.endswith(".py"):
    bot.load_extension(f"cogs.{cog[:-3]}")

bot.run("token") # running a bot like this is not recommended (token is visible in the source) but for the sake of this template, it's gonna be like this
