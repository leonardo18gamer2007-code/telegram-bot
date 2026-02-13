import telebot

TOKEN = "COLE_SEU_TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🔥 Bem-vindo ao conteúdo exclusivo da Maya Lorenz!\n\nEscolha uma opção:\n\n💎 /comprar - Acessar conteúdo\n❓ /suporte - Falar com suporte")

@bot.message_handler(commands=['comprar'])
def comprar(message):
    bot.send_message(message.chat.id, "💰 Para acessar o conteúdo, envie o pagamento via PIX:\n\nCHAVE PIX: SUA_CHAVE_AQUI\n\nApós pagar, envie o comprovante aqui.")

@bot.message_handler(commands=['suporte'])
def suporte(message):
    bot.send_message(message.chat.id, "📩 Suporte: @SEU_USUARIO")

bot.polling()
