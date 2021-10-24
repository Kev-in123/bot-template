import os
from discord.ext import commands

# bot constructor, edit this to your needs.
bot = commands.Bot(command_prefix="!")

#basic command
@bot.command()
async def hi(ctx):
    await ctx.send("Hi") # sends the message `Hi` to the invoking channel.

    #loagind the cog
bot.load_extension("cogs.fun")

bot.run("token") # running a bot like this is not recommended (token is visible in the source) but for the sake of this template, it's gonna be like this
