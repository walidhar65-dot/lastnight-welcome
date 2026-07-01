import discord
from discord.ext import commands
from datetime import datetime
from flask import Flask
from threading import Thread

# =============================================
#         Welcome Bot Settings
# =============================================
BOT_TOKEN          = "MTUyMTYxMDM4OTkyNDc0NTI5NQ.GbnOH8.P8LhhTkRzeV5i-c3TrCZC-EZU0739Kr-0CFh44"
WELCOME_CHANNEL_ID = 1521602464955240579  # صالون الترحيب الجديد
TICKETS_CHANNEL_ID = 1521602551454367814  # صالون التيكيت الجديد
# =============================================

intents = discord.Intents.default()
intents.members = True # ضروري تكون مفعلة فـ الـ Developer Portal

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[OK] Welcome Bot Online as {bot.user}")

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return

    # منشن للمستخدم الفوق بحال التصويرة image_fd5db0.png
    mention_msg = f"{member.mention}"
    
    # حساب تاريخ إنشاء الحساب مقاد
    created_at = member.created_at.strftime("%d/%m/%Y, %H:%M:%S")
    
    # حساب رقم العضو ف السيرفر (بلا البوتات)
    member_count = sum(not m.bot for m in member.guild.members)

    # ليمبيد كوبي بريست على image_fd5db0.png
    embed = discord.Embed(
        description=f"**{member.name}**\n\n"
                    f"┃ 🔺 Hey : {member.mention}\n\n"
                    f"┃ 🔺 Welcome To **Last Night Roleplay**\n\n"
                    f"┃ 🔺 If You Wanna Support Something <#{TICKETS_CHANNEL_ID}>\n\n"
                    f"┃ 🔺 Account Created At **{created_at}**\n\n"
                    f"┃ 🔺 You are member number : **#{member_count}**\n\n"
                    f"┃ 🔺 Enjoy <3",
        color=0xCC0000
    )
    
    embed.set_author(name=member.name, icon_url=member.display_avatar.url)
    embed.set_footer(text=f"{member.name}", icon_url=member.display_avatar.url)

    await channel.send(content=mention_msg, embed=embed)

# السيرفر ديال Flask باش الهوست الفابور يبقى شاد البوت 24/7 شاعل
app = Flask('')
@app.route('/')
def home(): return "Bot is Alive!"

def run(): app.run(host='0.0.0.0', port=8080)
Thread(target=run).start()

bot.run(BOT_TOKEN)