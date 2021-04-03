import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="?")


# cleint based events
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_ready():
    guild = discord.utils.find(lambda x: x.name == GUILD, client.guilds)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f"{guild.name} here are the members in this guild:\n -{members}")



# bot based events
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="goated", help="tells you if you are goated(greatest of all time).")
async def on_message(ctx):
    answer = ['Most of the time', 'YESSIR!', 'yup,yup,yup,yup,yup', 'no', 'stop the cap you are dog water', 'nah cap']
    response = random.choice(answer)
    await ctx.send(response)


@bot.command(name='dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [str(random.choice(range(number_of_sides + 1))) for _ in range(number_of_dice)]
    await ctx.send(', '.join(dice))


@bot.command(name="complement", help='gives you a random complement(Duh?)')
async def complement(cyx):
    complements = [f"You are amazing", "Looking good boos", "You are a king", "You are awesome", "Next goat",
                   "You are my little pog champ"]
    await cyx.send(random.choice(complements))


@bot.command(name="rps", help="rock paper scissors game")
async def game1(ctx, input: str):
    options=["rock", "paper", "scissors"]
    player_input = input.lower()
    computer_pick = random.choice(options)
    if input not in options:
        await ctx.send("You didn't put rock paper or scissors. Please only give one input")
    elif computer_pick == player_input:
        await ctx.send(f"Tie game we both picked {computer_pick}.")
    elif player_input == "rock":
        if computer_pick == "paper":
            await ctx.send(f"You lost. I choose {computer_pick}.")
        else:
            await ctx.send(f"You won great job! I choose {computer_pick}.")
    elif player_input == "paper":
        if computer_pick == "scissors":
            await ctx.send(f"You lost. I choose {computer_pick}.")
        else:
            await ctx.send(f"You won great job! I choose {computer_pick}.")
    elif player_input == "scissors":
        if computer_pick == "rock":
            await ctx.send(f"You lost! I choose {computer_pick}.")
        else:
            await ctx.send(f"You won great job! I choose {computer_pick}.")

@bot.command(name='create_channel')
@commands.has_role('GOAT')
async def create_channel(ctx, channel_name: str):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)
client.run(TOKEN)

