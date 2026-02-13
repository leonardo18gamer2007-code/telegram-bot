import telebot

TOKEN = "COLE_SEU_TOKEN_AQUI"
CANAL_ID = "COLE_SEU_CANAL_AQUI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
        "💎 Bem-vindo!\n\n"
        "Para entrar no canal VIP:\n"
        "Faça o Pix de R$19,90\n"
        "Chave Pix: SUA_CHAVE_AQUI\n\n"
        "Depois envie /paguei")

@bot.message_handler(commands=['paguei'])
def paguei(message):
    link = bot.create_chat_invite_link(
        chat_id=CANAL_ID,
        member_limit=1
    )
    bot.reply_to(message, f"✅ Pagamento recebido!\nAqui está seu acesso:\n{link.invite_link}")

bot.infinity_polling()
