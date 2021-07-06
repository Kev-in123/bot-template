import discord
from discord.ext import commands

class Fun(commands.Cog): #basic cog
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command() #basic command
    async def hi(self, ctx):
        return await ctx.send("Hello")
    
    @commands.command() #a command with arguments, invoked like !say <text>
    async def say(self, ctx, text):
        return await ctx.send(text)

def setup(bot): # this part is required for every cog
    bot.add_cog(Fun(bot))
