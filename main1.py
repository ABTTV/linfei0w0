import discord
import openai
from discord.ext import commands

# ตั้งค่าของ OpenAI API
openai.api_key = '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'  # แทนที่ด้วย OpenAI API Key ของคุณ

# ตั้งค่า intents สำหรับบอท Discord
intents = discord.Intents.default()
intents.message_content = True

# สร้าง instance ของ bot
bot = commands.Bot(command_prefix="!", intents=intents)

# เมื่อบอทเชื่อมต่อกับ Discord สำเร็จ
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# ฟังก์ชันสำหรับการใช้งาน GPT-4 ผ่าน OpenAI API
async def get_gpt4_response(prompt: str):
    try:
        response = openai.Completion.create(
            model="gpt-4",  # ใช้ GPT-4 Model
            prompt=prompt,
            temperature=0.7,  # ความสุ่มในการตอบกลับ (0.0 - 1.0)
            max_tokens=150,  # จำกัดจำนวนคำตอบ (tokens)
            n=1,  # รับแค่คำตอบเดียว
            stop=None,  # ไม่มีสัญญาณหยุด
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error getting GPT-4 response: {e}")
        return "ขอโทษค่ะ, เกิดข้อผิดพลาดในการติดต่อ GPT-4."

# คำสั่งสำหรับให้บอทตอบคำถามจากผู้ใช้
@bot.command()
async def ask(ctx, *, question: str):
    # ใช้ฟังก์ชันเพื่อส่งคำถามไปยัง GPT-4 และรับคำตอบ
    response = await get_gpt4_response(question)
    await ctx.send(response)

# เริ่มบอท
bot.run('MTMxNTI1Mjk1MjUwMzQyMzA3Nw.GfgW0T.STYIUv5wA8ecTuXVc1GVpBpaiKmtbe_C7iYQWM')  # แทนที่ด้วย Token ของ Discord Bot ของคุณ
