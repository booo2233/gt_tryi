import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from test_ai.ai_test import handle_response
load_dotenv()

BOT_TOKEN : str = os.getenv("BOT_TELE_KEY")
BOT_USERNAME : str = "@ai_gemini_bot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with! me! I am a cat")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("l am a cat! pls type something so l can respond")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
            file = await context.bot.get_file(update.message.photo[-1].file_id)
            os.chdir("image")
            await file.download_to_drive("image.jpg")
            os.chdir("..")
    else:
     message_type: str = update.message.chat.type
     text : str = update.message.text
     print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").split()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print("bot", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} casued error {context.error}")


if __name__ == "__main__":
    print("str")
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.ALL, handle_message))
    
    app.add_error_handler(error)
    print("poll")
    app.run_polling(poll_interval=0)