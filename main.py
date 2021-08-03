import os
import discord
from discord.ext import commands

# bot constructor, edit this to your needs.
bot = commands.Bot(command_prefix="!")

#basic command
@bot.command()
async def command(ctx):
    await ctx.send("Hi") # sends the message `Hi` to the invoking channel.

# loading cogs, you can skip this part if you dont use cogs
for cog in os.listdir("cogs"):
  if cog.endswith(".py"):
    bot.load_extension(f"cogs.{cog[:-3]}")

bot.run("token") # running a bot like this is not recommended but for the sake of this template, its gonna be like this
