from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your bot token
application = Application.builder().token('7577675216:AAFVwwEZ6JJqT97gVOSpFiB_MfF8C3Wosuc').build()

# Function to handle the "/start" command
text = '''
List of things you can try:
/start - Start the Conversation
/introduction  - Introduction of bot
/what_i_can_do - Bot Functionalities
/end   - end the conversation
'''

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text)

# Function to handle the "/help" command
async def introduction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I am bot created by aniket, i am here to interact, when aniket is busy.")

# Function to handle the "/hi" command
async def what_i_can_do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Aniket is still building me. Hope i can talk to you one day.')
    
    
async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Bye, Meet you soon.')
    


# Add handlers for the commands
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('introduction', introduction))
application.add_handler(CommandHandler('what_i_can_do', what_i_can_do))
application.add_handler(CommandHandler('end', end))

# Start the bot
application.run_polling()
