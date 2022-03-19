from email.headerregistry import Group
from inspect import getargs
from click import command
import discord
from typing import Optional, Set
from discord.ext import commands
from discord import Embed


class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return "{0.clean_prefix}{1.qualified_name} {1.signature}".format(
            self, command.signature
        )

    async def _help_embed(
        self,
        title: str,
        description: Optional[str] = None,
        mapping: Optional[dict] = None,
        command_set: Optional[Set[commands.Command]] = None,
    ):
        embed = Embed(title=title)
        if description:
            embed.description = description
        if command_set:
            # show help about all commands in the set
            filtered = await self.filter_commands(command_set, sort=True)
            for command in filtered:
                embed.add_field(
                    name=self.get_command_signature(command),
                    value=command.short_doc or "...",
                    inline=False,
                )
        if mapping:
            # add a short description of commands in each cog
            for cog, command_set in mapping.items():
                filtered = await self.filter_commands(command_set, sort=True)
                if not filtered:
                    continue
                name = cog.qualified_name if cog else "No Category"
                emoji = getattr(cog, "COG_EMOJI", None)
                cog_label = f"{emoji} {name}" if emoji else name
                cmd_list = "\u2002".join(
                    f"{self.clean_prefix}{cmd.name}" for cmd in filtered
                )
                value = (
                    f"{cog.description}\n```{cmd_list}```"
                    if cog and cog.description
                    else cmd_list
                )
                embed.add_field(name=cog_label, value=value, inline=False)
        return embed

    async def send_bot_help(self, mapping: dict):
        embed = await self._help_embed(
            title="Bot commands",
            description=self.context.bot.description,
            mapping=mapping,
        )
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command: commands.Command):
        emoji = getattr(command.cog, "COG_EMOJI", None)
        embed = await self._help_embed(
            title=f"{emoji} {command.qualified_name}"
            if emoji
            else command.qualified_name,
            description=command.help,
            command_set=command.commands
            if isinstance(command, commands.Group)
            else None,
        )
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog: commands.Cog):
        emoji = getattr(cog, "COG_EMOJI", None)
        embed = await self._help_embed(
            title=f"{emoji} {cog.qualified_name}" if emoji else cog.qualified_name,
            description=cog.help,
            command_set=cog.get_commands(),
        )
        await self.get_destination().send(embed=embed)

    send_cog_help = send_command_help
