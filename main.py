import discord, random

from discord.ext import commands
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной bot и передаем все привелегии
bot = commands.Bot(command_prefix= '.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Привет! Я бот {bot.user}!")

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def subtract(ctx, left1: int, right1: int):
    await ctx.send(left1 - right1)

@bot.command()
async def multiply(ctx, left2: int, right2: int):
    await ctx.send(left2 * right2)

@bot.command()
async def divide(ctx, left3: int, right3: int):
    await ctx.send(left3 / right3)

@bot.command()
async def even_or_odd (ctx):
    result = random.randint(1, 10)
    await ctx.send(result)
@bot.command()
async def hellp(ctx):
    await ctx.send(".hello - Команда которые заставляет бота знакомится, .add - складывает число и выводит в чат результат (Пример: .add 2 3, БОТ: 5. Так работает и с subtract, multiply и divide), .subtract - вычитает число и выводит в чат результат, multiply - умножает число и выводит в чат результат, divide - делит число и выводит в чат результат, even_or_odd - выводит в чат чётное или нечётное число")
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} Привет! Чтобы мною пользоватся веди префикс . Чтобы подробнее узнать о моих командах напиши .hellp {discord.utils.format_dt(member.joined_at)}')
bot.run("TOKEN")
