from typing import Literal

import discord
import random
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

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
        answers = ["Du dreckiger Noskin",
        "Dein beschnittener Pimmel stinkt bis nach fucking Tokio", 
        "Mein geerther Skin sie schauen heute sehr gut aus!", 
        "Ohne Mütze schaust du scheiße aus", 
        "Käse ist lecker",
        "Johannes ist auch ein noskin denke daran!!!"]
        # Your code will go here
        await ctx.send(random.choice(answers))
        await ctx.send(".gifr foreskin")
