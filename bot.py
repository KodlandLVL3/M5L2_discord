from config import *
from logic import *
import discord
from discord.ext import commands
from config import TOKEN

# Инициализация менеджера базы данных
manager = DB_Map("database.db")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot started")

@bot.command()
async def start(ctx: commands.Context):
    await ctx.send(f"Привет, {ctx.author.name}. Чтобы узнать список команд, введи !help_me")

@bot.command()
async def help_me(ctx: commands.Context):
    await ctx.send(
        # Реализуй отрисовку города по запросу
    )

@bot.command()
async def show_city(ctx: commands.Context, *, city_name=""):
    # Реализуй отрисовку города по запросу

@bot.command()
async def show_my_cities(ctx: commands.Context):
    cities = manager.select_cities(ctx.author.id)  # Получение списка городов пользователя

    # Реализуй отрисовку всех городов

@bot.command()
async def remember_city(ctx: commands.Context, *, city_name=""):
    if manager.add_city(ctx.author.id, city_name):  # Проверка и добавление города в БД
        await ctx.send(f'Город {city_name} успешно сохранен!')
    else:
        await ctx.send("Неверный формат. Укажите название города на английском языке через пробел после команды.")

if __name__ == "__main__":
    bot.run(TOKEN)