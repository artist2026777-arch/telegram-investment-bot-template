import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# MOCK DATABASE (In-memory for demonstration)
user_portfolios = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message and initializes user portfolio."""
    user = update.effective_user
    if user.id not in user_portfolios:
        user_portfolios[user.id] = {"balance": 1000.0, "invested": 0.0}
    
    welcome_text = (
        f"Hello {user.first_name}! \n"
        "Welcome to the Investment Simulator Bot. \n"
        "You have a virtual starting balance of $1000."
    )
    
    keyboard = [
        [InlineKeyboardButton("💰 Balance", callback_data='balance')],
        [InlineKeyboardButton("📈 Invest $100", callback_data='invest_100')],
        [InlineKeyboardButton("📉 Withdraw All", callback_data='withdraw_all')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=welcome_text,
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles button clicks."""
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if user_id not in user_portfolios:
         user_portfolios[user_id] = {"balance": 1000.0, "invested": 0.0}

    portfolio = user_portfolios[user_id]

    if query.data == 'balance':
        text = (
            f"💰 Wallet Balance: ${portfolio['balance']:.2f}\n"
            f"📈 Active Investments: ${portfolio['invested']:.2f}"
        )
        await query.edit_message_text(text=text, reply_markup=query.message.reply_markup)

    elif query.data == 'invest_100':
        if portfolio['balance'] >= 100:
            portfolio['balance'] -= 100
            portfolio['invested'] += 100
            text = "✅ Successfully invested $100!"
        else:
            text = "❌ Insufficient funds."
        
        # Show temporary alert
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    elif query.data == 'withdraw_all':
        amount = portfolio['invested']
        if amount > 0:
            portfolio['balance'] += amount
            portfolio['invested'] = 0
            text = f"✅ Withdrew ${amount:.2f} to wallet."
        else:
            text = "⚠️ No active investments to withdraw."
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

if __name__ == '__main__':
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not found in .env file.")
        exit(1)

    application = ApplicationBuilder().token(token).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot is running...")
    application.run_polling()
