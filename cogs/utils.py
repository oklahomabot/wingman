import discord
from discord.ext import commands


class Utils(commands.Cog):

    def __init__(self, client):

        self.client = client

    @commands.command()
    async def userinfo(self, ctx, user: discord.User = None):
        temp = ''
        if user is None:
            await ctx.send('Please provide a user to get info')
            return
        temp = ((f'- User\'s ID: {user.id}\n') +
                (f'- User\'s discrim: {user.discriminator}\n') +
                ('- Is User a bot?: '))
        temp = temp + ('YES' if user.bot else 'NO')

        embed = discord.Embed(
            title='Userinfo', description=f'misc. info about {user.name}', colour=discord.Colour.blue())

        embed.add_field(name=user, value=temp)
        if user.avatar is not None:
            embed.set_thumbnail(url=user.avatar_url_as(size=64))

        await ctx.send(':mag:', embed=embed)

    @commands.command()
    # passing ctx is context and is required
    # it has such information as message ...
    async def ping(self, ctx):
        '''
        I'll play
        '''
        # await is used with async to prevent blocking simple
        # processes by allowing others to continue
        await ctx.send(f'Pong: {round(self.client.latency*1000)}ms')


def setup(client):

    client.add_cog(Utils(client))
