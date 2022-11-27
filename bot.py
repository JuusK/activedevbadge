import discord
from discord import app_commands
from discord.ext import commands
import config

token = config.TOKEN

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())
@client.event
async def on_ready():
	print("bot has started! token: " + token)
	try:
		synced = await client.tree.sync()
		print(f"Synced: {len(synced)} command(s)")
	except Exception as exc:
		print(exc)


@client.tree.command(name="badge")
async def badge(interaction: discord.Interaction):
	await interaction.response.send_message(f"Hello Mr. {interaction.user.mention}! Thanks for using the bot! If this is your bot you should get the badge soon! (24h)")

client.run(token)
