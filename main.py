import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

images = os.path.join(os.getcwd(), "images")

def select_random_image_path():
    return os.path.join(images, random.choice(os.listdir(images)))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot that talks about Global Warming! You can ask me some questions by using some key words! You should use "$" before every keyword. Here are the keywords: GlobalWarming ; causes ; actions ; ecoadvice ; COP ; upcomingCOP ; COP29')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def GlobalWarming(ctx):
    await ctx.send(f"Global warming is the long-term heating of Earth's surface observed since the pre-industrial period (between 1850 and 1900) due to human activities, primarily fossil fuel burning, which increases heat-trapping greenhouse gas levels in Earth's atmosphere. This term is not interchangeable with the term 'climate change.'")

@bot.command()
async def causes(ctx):
    await ctx.send(f'1) Generating power. '
                   f'\nGenerating electricity and heat by burning fossil fuels such as coal, oil and natural gas causes a large chunk of global emissions. Most electricity is still produced from fossil fuels; only about a quarter comes from wind, solar and other renewable sources.'
                   f'\n2) Manufacturing goods. '
                   f'Manufacturing and industry produce emissions, mostly from burning fossil fuels to produce energy for making things like cement, iron, steel, electronics, plastics, clothes and other goods. Mining and other industrial processes also release gases.'
                   f'\n3) Cutting down forests. '
                   f'Cutting down forests to create farms or pastures, or for other reasons, causes emissions, since trees, when they are cut, release the carbon they have been storing. Since forests absorb carbon dioxide, destroying them also limits nature’s ability to keep emissions out of the atmosphere.')

@bot.command()
async def actions(ctx):
    await ctx.send(f'1) Save energy at home.'
                   f'\nMuch of our electricity and heat is powered by coal, oil and gas. Use less energy by lowering your heating and cooling, switching to LED light bulbs and energy-efficient electric appliances, washing your laundry with cold water or hanging things to dry instead of using a dryer.'
                   f'\n2) Walk, cycle or take public transport. '
                   f'The world’s roads are clogged with vehicles, most of them burning diesel or petrol. Walking or riding a bike instead of driving will reduce greenhouse gas emissions – and help your health and fitness. For longer distances, consider taking a train or bus. And carpool whenever possible.'
                   f'\n3) Eat more vegetables. '
                   f'Eating more vegetables, fruits, whole grains, legumes, nuts and seeds, and less meat and dairy, can significantly lower your environmental impact. Producing plant-based foods generally results in fewer greenhouse gas emissions and requires less energy, land and water.')

@bot.command()
async def ecoadvice(ctx):
    await ctx.send(file=discord.File(select_random_image_path()))

@bot.command()
async def COP(ctx):
    await ctx.send(f'The Conference of the Parties (COP), is held annually, with the Presidency rotating between the five recognised UN regions. A key part of COP meetings is to review the contributions of each of the Parties, detailing how they are tackling climate change.')

@bot.command()
async def upcomingCOP(ctx):
    await ctx.send(f'This year, Azerbaijan has been selected as the Presidency of the 29th Conference of the Parties (COP29), to be hosted in Baku this November. Azerbaijan has a strong track record of hosting international events and has chosen Baku Stadium as the venue for COP29.'
                   f'\nTo deliver a process that is transparent, impartial and inclusive, the COP29 Presidency has developed a plan based on two mutually reinforcing pillars to enhance ambition and enable action.')

Images = ["https://cdn.trend.az/2024/04/15/trend_cop29_loqo_2.jpg", "https://cop29.az/storage/53/01HVP55WS7Q1MENE4ZY9PG1YPE.jpg", "https://theeuropetoday.com/wp-content/uploads/2024/03/IMG-20240318-WA0173-jpg.webp"]
@bot.command()
async def COP29(ctx):
    await ctx.send(random.choice(Images))

