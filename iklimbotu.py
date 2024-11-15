import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="nasil_baslayacagim")
async def nasil_baslayacagim(ctx):
    await ctx.send(f"Kaç tane fikir istersin? (en fazla 4)")
    ideas = [
        "hemen şu anda bir geri dönüşüm poşeti hazırlayıp ona geri dönüşümleri oraya atabilirsin.",
        "hemen şu anda etrafındakileri bilinçlendirebilirsin.",
        "hemen şu anda atık pillerini alıp marketlerdeki atık pil kutusuna atabilirsin.",
        "hemen şu anda plastik, kağıt gibi malzemeleri azaltma kararı alabilirsin."
    ]
    await ctx.send(f"Genç arkadaşım! {random.choice(ideas)}")


bot.run("MTI5OTY4NjI3NzY3ODg5NTEzNQ.GTOEnW.HHrqYdpIlSEuHEcJdM-OVSb4iWFA8OfjVEEvE8")
