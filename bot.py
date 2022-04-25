# autor Evgenii Filatov
# 21F_CST8333_350 

from dao import Dao
import telebot, business


# create bot for users of "Telegram"
TOKEN = "2135055802:AAHMVK_ab96vkf4ZzObnymYlZ_BOCmp8R6o"

bot = telebot.TeleBot(TOKEN)
crud = business.CRUD(dao=Dao())

@bot.message_handler(commands = ["start"])
def welcome(message):
    bot.reply_to(message, "Hello, please choose command and arguments")

# customers CRUD

@bot.message_handler(content_types = ["text"]) 
def main(message):
    command_args : str = message.text.split(" ")
    if command_args[0] == "delete":
        crud.deleteRecord(command_args[1])
    if command_args[0] == "print":
        if command_args[1] == "*":
            answer = crud.printVacc(int(command_args[2]),int(command_args[3]))
            bot.reply_to(message, answer)
        else :  
            answer = crud.printCustomVacc(command_args[1],int(command_args[2]),int(command_args[3]))
            bot.reply_to(message, answer)
    if command_args[0] == "update":
        values = command_args[1].split(",")
        crud.editRecord(values [0], values[1])
        bot.reply_to(message, "updated")

    if command_args[0] == "create":
        values = command_args[1].split(",")
        crud.addRecord(values [0], values[1])
        bot.reply_to(message, "created")
bot.infinity_polling()

    
         