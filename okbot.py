import discord
from discord.ext import commands

client = commands.Bot(command_prefix='=')

TOKEN = 'ODAzMjYwMjYwNDUzOTc0MDY0.YA7MaQ.lw_3_USp4TZd7KkdWaVWtOkeTnE'

# List of filenames (does not need .py)
cogs = ['cogs.events', 'cogs.utils']

# cog loader
for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f'Could not load cog {cog}: {str(e)}')
    else:
        print(f'{cog} cog loaded')


@client.event
async def on_ready():
    print('Wingman Online')
    # Load server db? learn server seperation


@client.command()
async def loadcog(ctx, cogname=None):

    if cogname is None:
        return

    try:
        client.load_extension(cogname)
    except Exception as e:
        print(f'Could not load cog {cog}: {str(e)}')
    else:
        print(f'Loaded Cog {cog} successfully')


@client.command()
async def unloadcog(ctx, cogname=None):

    if cogname is None:
        return

    try:
        client.unload_extension(cogname)
    except Exception as e:
        print(f'Could not unload cog {cogname}: {str(e)}')
    else:
        print(f'Unloaded Cog {cogname} successfully')


@ client.command()
async def roleinfo(ctx, role: discord.User):

    await ctx.send(role.id)


@ client.command()
async def multi(ctx, role: discord.Role, user: discord.User):

    await ctx.send(role.id)
    await ctx.send(user.id)


client.run(TOKEN)
