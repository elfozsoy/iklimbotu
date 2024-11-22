import discord
from discord.ext import commands
import random,os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)

@bot.command(name="nasil_baslayacagim")
async def nasil_baslayacagim(ctx):
    ideas = [
        "hemen şu anda bir geri dönüşüm poşeti hazırlayıp ona geri dönüşümleri oraya atabilirsin.",
        "hemen şu anda etrafındakileri bilinçlendirebilirsin.",
        "hemen şu anda atık pillerini alıp marketlerdeki atık pil kutusuna atabilirsin.",
        "hemen şu anda plastik, kağıt gibi malzemeleri azaltma kararı alabilirsin."
    ]
    await ctx.send(f"Genç arkadaşım ! {random.choice(ideas)}")

@bot.command(name="bana_aciklar_misin")
async def bana_aciklar_misin(ctx):
    aciklamalar = [
        "Sana kısaca cam atığının geri dönüşümünü anlatayım. Cam atıkları geri dönüşüm kutularından toplarlar ve fabrikaya götürülüp renklerine göre ayırırlar. Sonra da camları eriterek yeniden kalıplaras dökerler ve bitti! İşte bu kadar!",
        "Geri dönüşüm, kullanılmış bir malzemenin bir takım işlemler ile yeniden yapılmasıdır. Malzemenin hammaddesi ile başka ürünler yapılabilir ve bu geri dönüşümdür. Ayrıca geri dönüşümü sonsuza kadar yapabilirsiniz! Yapısında hiç bir sorun çıkmaz. "
    ]
    await ctx.send(f" {random.choice(aciklamalar)}")
    await ctx.send(f"Bugün su ve elektrik tasarrufu yapmayı unutma!")

@bot.command(name="quiz")
async def quiz(ctx):
    sorular = [
        "Hangi atık geri dönüştürülebilir? A)kömür B)plastik C)elma çöpü D)oyuncak (şıkkın ismini büyük harfle yaz)",
        "Doğal atıklar çevreye zarar verir mi? (küçük harfle evet yada hayır de )",
        "Etrafa çöp atan insanlara ne denir? :) (bu biraz şaşırtmalı bir soru)",
        "Hangi atık geri dönüştürülemez? A)cam B)plastik C)oyuncak "
    ]
    await ctx.send(f" {random.choice(sorular)}")

@bot.command(name="B")
async def B(ctx):
    await ctx.send("Doğru cevap! Harikasın!")

@bot.command(name="C")
async def C(ctx):
    await ctx.send("Mükemmel! Doğru cevap.")

@bot.command(name="hayır")
async def B(ctx):
    await ctx.send("Doğru cevap! Harikasın!")

@bot.command(name="kıt")
async def kıt(ctx):
    await ctx.send(":)))) Doğru!")

@bot.command(name="banane_etrafa_cop_atarim")
async def banane_etrafa_cop_atarim(ctx):
    saldiri_sozcukleri = [

        "Ne demek banane?!",
        "Sen ciddi misin? O attığımız çöpleri umursamamız gerekiyor dostum üzgünüm.",
        "Bizim gözümüzde küçük olan şeyler aslında ne kadar büyük biliyor musun? İstersen git biraz araştırma yap. Belki fikrini değiştirirsin."
        "NE?",
        "...",
        "Ben geri dönüşüm botuyum ve sizin gibi gençler için buradayım lütfen fikrini değiştir. Çevre kirliliği korkunç bir şey.",
        "Geleceğini mi kirletmek istiyorsun kanka?",
        "SEN İYİ MİSİN?",
        "Lütfen hemen karar verme! Biraz araştırma yap arkadaş çevrenden yardım iste. Bilinçlenmek çok önemli. LÜTFEN.",
        "LÜTFEN BÖYLE DÜŞÜNME, YANLIŞ YOLDASIN.",
        "SEN CİDDEN İYİ MİSİN?",
        "Lütfen saçmalama.",
        "Bak, yabancıların Türkler hakkında kötü konuştuklarında Türklerin uyguladığı tarifeyi uygulamak hiç istemiyorum.",
        "SEN NE YAPIYORSUN?",
        "LÜTFEN BUNLARI CİDDİYE AL.",
        "LÜTFEN OTOBÜSDE YER VERMEDİĞİNDE TEYZENİN DEDİKLERİNİ DEDİRTTİRME."
        "Bak, siz bu ülkenin geleceğisiniz. Her şey size bağlı. Bu yüzden hedef kitlem gençler. Şimdiden bilinçlenirseniz ileride Mars'a falan yerleşmek zorunda kalmazsın.",
        "Lütfen uyarılarımızı dikkate al dostum, ben sana yardımcı olmaya çalışıyorum."
    ]
    await ctx.send(f"{random.choice(saldiri_sozcukleri)}")

@bot.command(name="sanane_bot")
async def sanane_bot(ctx):
    saldiri = [
         "NE",
         "S-SEN CİDDİ MİSİN?",
         "SİZ GENÇLER KARAR VERMEDE ÇOK ZORLANIYORSUNUZ.",
         "NİYE BUNU YAPIYORSUN SORABİLİR MİYİM?",
         "EMPATİ KURMAYI DENE.",
         "SEN BİLİRSİN BEN ELİMDEN GELENİNİ YAPTIM.",
         ". . .",
         "N-N-NE?",
         "PEKİ.",
         "UMARIM ÇABAM BOŞA GİTMEMİŞTİR",
         "DOĞAYA OLAN SEVGİN BELLİ OLUYOR.",
         "AYYNEN BÖYLE DEVAM ET. GELECEĞİNİ ÇÖPE BOĞ. AMAN DİKKAT ET AMAAN.",
         "ŞOKTAYIM. BÖYLE BİR ŞEY YAPAMAZSIN.",
         "DEMEK SENDE KIT OLMAK İSTİYORSUN... HIMMMM ANLADIM BEN. ANLADIM"
    ]
    await ctx.send(f"{random.choice(saldiri)}")

@bot.command(name="mem")
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open('images/{gerimem1}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



bot.run("TOKEN")
