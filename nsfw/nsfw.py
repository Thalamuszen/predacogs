import discord

from redbot.core import checks, commands
from redbot.core.i18n import Translator, cog_i18n

import contextlib
from typing import Union

from . import constants as sub
from .core import Core, nsfwcheck

_ = Translator("Nsfw", __file__)


@cog_i18n(_)
class Nsfw(Core):
    """
    Send random NSFW images from random subreddits
    """

    @commands.command()
    async def nsfwversion(self, ctx: commands.Context):
        """Get the version of the installed Nsfw cog."""

        await self._version_msg(ctx, self.__version__, self.__author__)

    @nsfwcheck()
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cleandm(self, ctx: commands.Context, number: int):
        """
            Delete a number specified of DM's from the bot.

            `<number>`: Number of messages from the bot you want
            to delete in your DM's.
        """
        if ctx.guild:
            return await ctx.send(_("This command works only for DM's messages !"))
        async for message in ctx.channel.history(limit=number):
            if message.author.id == ctx.bot.user.id:
                with contextlib.suppress(discord.NotFound):
                    await message.delete()
        await ctx.tick()

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(name="4k", aliases=["4K", "fourk"])
    async def four_k(self, ctx: commands.Context):
        """4k images."""

        await self._send_msg(ctx, _("4k"), sub=sub.FOUR_K)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["oface", "ofaces"])
    async def ahegao(self, ctx: commands.Context):
        """Ahegao images."""

        await self._send_msg(ctx, _("ahegao"), sub=sub.AHEGAO)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["butt", "booty"])
    async def ass(self, ctx: commands.Context):
        """Ass images."""

        await self._send_msg(ctx, _("ass"), sub=sub.ASS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["asian"])
    async def asianporn(self, ctx: commands.Context):
        """Asian porn."""

        await self._send_msg(ctx, _("asian porn"), sub=sub.ASIANPORN)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["sodomy"])
    async def anal(self, ctx: commands.Context):
        """Anal images/gifs."""

        await self._send_msg(ctx, _("anal"), sub=sub.ANAL)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["shibari"])
    async def bdsm(self, ctx: commands.Context):
        """BDSM images."""

        await self._send_msg(ctx, _("bdsm"), sub=sub.BDSM)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["blowjobs", "blowj", "bjob", "fellatio", "fellation"])
    async def blowjob(self, ctx: commands.Context):
        """Blowjob images/gifs."""

        await self._send_msg(ctx, _("blowjob"), sub=sub.BLOWJOB)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["boob", "boobies", "tits", "titties", "breasts", "breast"])
    async def boobs(self, ctx: commands.Context):
        """Boobs images."""

        await self._send_msg(ctx, _("boobs"), sub=sub.BOOBS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["boless", "b_less"])
    async def bottomless(self, ctx: commands.Context):
        """Bottomless images."""

        await self._send_msg(ctx, _("bottomless"), sub=sub.BOTTOMLESS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def cosplay(self, ctx: commands.Context):
        """NSFW cosplay images."""

        await self._send_msg(ctx, _("nsfw cosplay"), sub=sub.COSPLAY)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cunni", "pussyeating"])
    async def cunnilingus(self, ctx: commands.Context):
        """Cunnilingus images."""

        await self._send_msg(ctx, _("cunnilingus"), sub=sub.CUNNI)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cum", "cums", "cumshots"])
    async def cumshot(self, ctx: commands.Context):
        """Cumshot images/gifs."""

        await self._send_msg(ctx, _("cumshot"), sub=sub.CUMSHOTS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["deept", "deepthroating"])
    async def deepthroat(self, ctx: commands.Context):
        """Deepthroat images."""

        await self._send_msg(ctx, _("deepthroat"), sub=sub.DEEPTHROAT)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cock"])
    async def dick(self, ctx: commands.Context):
        """Dick images."""

        await self._send_msg(ctx, _("dick"), sub=sub.DICK)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["doublep", "dpenetration", "doublepene", "doublepen"])
    async def doublepenetration(self, ctx: commands.Context):
        """Double penetration images/gifs."""

        await self._send_msg(ctx, _("double penetration"), sub=sub.DOUBLE_P)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["facial"])
    async def facials(self, ctx: commands.Context):
        """Facial images."""

        await self._send_msg(ctx, _("facials"), sub=sub.FACIALS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["feets", "feetish"])
    async def feet(self, ctx: commands.Context):
        """Feet images."""

        await self._send_msg(ctx, _("feets"), sub=sub.FEET)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def femdom(self, ctx: commands.Context):
        """Femdom images."""

        await self._send_msg(ctx, _("femdom"), sub=sub.FEMDOM)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["futanari"])
    async def futa(self, ctx: commands.Context):
        """Futa images."""

        await self._send_msg(ctx, _("futa"), sub=sub.FUTA)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["gpp"])
    async def gay(self, ctx: commands.Context):
        """Gay porn."""

        await self._send_msg(ctx, _("gay porn"), sub=sub.GAY_P)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["groups", "nudegroup", "nudegroups"])
    async def group(self, ctx: commands.Context):
        """Group nudes."""

        await self._send_msg(ctx, "groups nudes", sub=sub.GROUPS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["hentaigif"])
    async def hentai(self, ctx: commands.Context):
        """Hentai images/gifs."""

        await self._send_other_msg(
            ctx,
            name=_("hentai"),
            arg="message",
            source="Nekobot API",
            url=sub.NEKOBOT_URL.format(sub.NEKOBOT_HENTAI),
        )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lesbians"])
    async def lesbian(self, ctx: commands.Context):
        """Lesbian images/gifs."""

        await self._send_msg(ctx, _("lesbian"), sub=sub.LESBIANS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["milfs"])
    async def milf(self, ctx: commands.Context):
        """Milf images."""

        await self._send_msg(ctx, _("milf"), sub=sub.MILF)

    # @nsfwcheck()
    # @commands.bot_has_permissions(embed_links=True)
    # @commands.cooldown(1, 0.5, commands.BucketType.user)
    # @commands.command(aliases=["nekogifs"])
    # async def nekogif(self, ctx: commands.Context):
    #     """Show some neko gifs from Nekobot API."""

    #     await self._send_other_msg(
    #         ctx,
    #         name=_("neko gif"),
    #         arg="message",
    #         source="Nekobot API",
    #         url=sub.NEKOBOT_URL.format("hneko"),
    #     )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["oralsex"])
    async def oral(self, ctx: commands.Context):
        """Oral images/gifs."""

        await self._send_msg(ctx, _("oral"), sub=sub.ORAL)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["pgif", "prongif"])
    async def porngif(self, ctx: commands.Context):
        """Straight up porn gifs."""

        await self._send_other_msg(
            ctx,
            name=_("porn gif"),
            arg="message",
            source="Nekobot API",
            url=sub.NEKOBOT_URL.format("pgif"),
        )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["flashinggirl"])
    async def public(self, ctx: commands.Context):
        """Public nudes."""

        await self._send_msg(ctx, _("public nude"), sub=sub.PUBLIC)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["vagina", "puss"])
    async def pussy(self, ctx: commands.Context):
        """Pussy images."""

        await self._send_msg(ctx, _("pussy"), sub=sub.PUSSY)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def realgirls(self, ctx: commands.Context):
        """Real girls."""

        await self._send_msg(ctx, _("real nudes"), sub=sub.REAL_GIRLS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["redheads", "ginger", "gingers"])
    async def redhead(self, ctx: commands.Context):
        """Red head images."""

        await self._send_msg(ctx, _("red head"), sub=sub.REDHEADS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["squirts"])
    async def squirt(self, ctx: commands.Context):
        """Squirt images."""

        await self._send_msg(ctx, _("squirt"), sub=sub.SQUIRTS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["thighs", "legs"])
    async def thigh(self, ctx: commands.Context):
        """Thighs images."""

        await self._send_msg(ctx, _("thigh"), sub=sub.THIGHS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["groupsex"])
    async def threesome(self, ctx: commands.Context):
        """Threesome images."""

        await self._send_msg(ctx, _("threesome"), sub=sub.THREESOME)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["traps", "trans", "girldick", "girldicks", "shemale", "shemales"])
    async def trap(self, ctx: commands.Context):
        """Traps images/gifs."""

        await self._send_msg(ctx, _("trap"), sub=sub.TRAPS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["wild", "gwild"])
    async def gonewild(self, ctx: commands.Context):
        """Gonewild images."""

        await self._send_msg(ctx, _("gonewild"), sub=sub.WILD)
