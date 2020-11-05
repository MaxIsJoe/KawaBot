import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '>>>')


status = cycle(["with's master cock", 
"with Rune's hair", 
"captalism simulator with German", 
"edgy songs with Emmy", 
"Kaz's appearance on TV", 
"Khadel's gacha games", 
"with lemon's memes", 
"AAAAAAAAAAA",
"Jame's videos",
"with Todd Howard",
"Max's games"])

@client.event
async def on_ready():
    change_status.start()
    print('KawaBot is online!')
    print('Her discord ID is {0.user}'.format(client))
    game = discord.Game("with master's cock")
    await client.change_presence(status=discord.Status.idle, activity=game)


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    pass

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Sorry, but some arguments are missing or are incorrect')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! it took me {round(client.latency * 1000)} ms to send this! Am I fast enough?')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

def IsItMax(ctx):
    return ctx.author.id == "Max's ID"

client.run('[Super Secret Token that only the mightiest of DOTA players can obtain]')
