import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=OPENAI_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await update.message.reply_text("📊 Screenshots received. Applying Sniper Bot V1...")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """
You are Sniper Bot V1.
Apply:
- H4 range detection
- M15 momentum filter
- M5 liquidity sweep
- RSI
- Volume spike
- ATR filter
- 5.0 SL
- 1:4 RR default

Return result in structured table format.
"""},
                {"role": "user", "content": "Analyze the screenshots and give trade decision."}
            ]
        )

        await update.message.reply_text(response.choices[0].message.content)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, handle_message))

app.run_polling()
