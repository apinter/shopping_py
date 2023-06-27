import os
import telebot

BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
SHOPPING_LIST = os.path.relpath("data/list.md")
TEMP_SHOPPING_LIST = os.path.relpath("data/temp_list.md")

bot = telebot.TeleBot(BOT_TOKEN)

if not os.path.exists(SHOPPING_LIST):
    with open(SHOPPING_LIST, 'w') as f:
        f.write('')
        f.close()

def read_shopping_list():
    with open(SHOPPING_LIST, 'r') as f:
        """ return the list of strings pretty printed"""
        content = f.read().strip()
        if not content:
            return "Hey, your shopping list is empty! Use the /add command to add an item."
        else:
            return content

def add_to_shopping_list(new_item):
    with open(SHOPPING_LIST, 'a') as f:
        """read the input and append it to the list"""
        # new_item = input('What do you want to add to the list? ')
        f.write('\n'+ new_item)

def remove_from_shopping_list(item_to_remove):
    found = False
    # item_to_remove = input('What do you want to remove from the list?')
    with open(SHOPPING_LIST, "r") as read_file:
        with open(TEMP_SHOPPING_LIST, "w") as out_file:
            for line in read_file:
                if item_to_remove not in line:
                    out_file.write(line)
                else:
                    found = True
    os.replace(TEMP_SHOPPING_LIST, SHOPPING_LIST)
    if not found:
        print("Couldn't find the item you wanted to remove.")

def clear_list():
    with open(SHOPPING_LIST, 'w') as f:
        f.write('')
        f.close()

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, "You can get items with /sync, add items with /add, remove items with /rm, and clear the list with /clear.")

@bot.message_handler(commands=['sync'])
def sign_handler(message):
    shopping_message = read_shopping_list()
    bot.send_message(message.chat.id, "Here's your list!")
    bot.send_message(message.chat.id, shopping_message, parse_mode="Markdown")

@bot.message_handler(commands=['add'])
def add_handler(message):
    text = "What would you like to add to the list?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, add_list)

def add_list(message):
    tiee = message.text
    item = add_to_shopping_list(tiee)
    bot.send_message(message.chat.id, "Added!")
    # bot.send_message(message.chat.id, item, parse_mode="Markdown")

@bot.message_handler(commands=['rm'])
def rm_handler(message):
    text = "What would you like to delete from the list?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, rm_list)

def rm_list(message):
    tie = message.text
    item = remove_from_shopping_list(tie)
    bot.send_message(message.chat.id, "Removed!")
    # bot.send_message(message.chat.id, item, parse_mode="Markdown")

@bot.message_handler(commands=['clear'])
def clear_handler(message):
    clear_list_message = clear_list()
    bot.send_message(message.chat.id, "Your list has been cleared!")
    bot.send_message(message.chat.id, clear_list_message, parse_mode="Markdown")

bot.infinity_polling()