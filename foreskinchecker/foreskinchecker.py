from typing import Literal

import discord
import random
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config
from influxdb import InfluxDBClient

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class checker(commands.Cog):
    """
    checks if you have foreskin
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=887777595825983519,
            force_registration=True,
        )

    async def red_delete_data_for_user(self, *, requester: RequestType, user_id: int) -> None:
        # TODO: Replace this with the proper end user data removal handling.
        super().red_delete_data_for_user(requester=requester, user_id=user_id)

    @commands.command()
    async def skin(self, ctx):

        texts = []
        results = client.query('SELECT "text" FROM "RedCogs"."autogen"."noskinInsult"')
        for result in results:
            for subresult in result:
                texts.append(subresult['text'])

        await ctx.send(random.choice(texts))

    @commands.command()
    async def addskintext(self, ctx, *, text: str):

        client = InfluxDBClient(host='192.168.178.78', port=8086, username='maxi', password='maxi1997',
                                database="RedCogs")
        json_body = [
            {
                "measurement": "noskinInsult",
                "tags": {
                    "type": "noskinInsult",
                },
                "fields": {
                    "text": text
                }
            }
        ]

        response = ""

        if client.write_points(json_body):
            response = f"Worked, added {text} to the database"
        else:
            response = f"ERROR couldnt add {text} to the database"

        await ctx.send(response)


    @commands.command()
    async def whatskin(self, ctx):

        client = InfluxDBClient(host='192.168.178.78', port=8086, username='maxi', password='maxi1997',
                                database="RedCogs")

        results = client.query('SELECT "text" FROM "RedCogs"."autogen"."noskinInsult"')
        for result in results:
            for subresult in result:
                await ctx.send(subresult['text'])
