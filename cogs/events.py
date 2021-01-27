import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, client):

        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # channel id needs to be populated - using home bot test channel
        # member.name + '#' + str(member.descrim) same as just passing member
        await self.client.get_channel(790687613656367154).send(member + ' joined the server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # channel id needs to be populated - using home bot test channel
        # send info is same as just passing member (expanded for my info)
        await self.client.get_channel(790687613656367154).send(member + ' left the server :sob:')

    @commands.command()
    async def cool(self, ctx):
        await ctx.send(f':sunglasses:')

    @commands.command()
    async def say(self, ctx, *, message=None):
        '''
        Whatever you say boss
        '''
        if message == None:
            await ctx.send('Please provide a message')
            return

        temp = message + ' and he is probably right.'
        await ctx.send(f'{ctx.author.name} said {temp}')

    @commands.command()
    async def brag(self, ctx):
        '''
        Who is Number One?
        '''

        await ctx.send(f'{ctx.author.name} is king of the world!!!')


def setup(client):

    client.add_cog(Events(client))
