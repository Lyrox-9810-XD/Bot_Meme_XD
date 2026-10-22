import discord
from discord.ext import commands
import os
import random
# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='_', intents=intents)


@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')


@bot.command()
async def ciao(ctx, nome):
    await ctx.send(f'Ciao {nome}!')

@bot.command()
async def meme(ctx, categoria):
    if categoria == 'animali':
        lista_file = os.listdir('animali')
        random_file = random.choice(lista_file)

    if categoria == 'persone':
        lista_file = os.listdir('persone')
        random_file = random.choice(lista_file)

    if categoria == 'programmatori':
            lista_file = os.listdir('programmatori')
            random_file = random.choice(lista_file)
            
    
    with open(f'{categoria}/{random_file}', 'rb') as f:
        discord_file = discord.File(f)
        await ctx.send(file=discord_file)

bot.run("")