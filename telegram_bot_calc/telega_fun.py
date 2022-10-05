
def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Приветствую в калькуляторе")
    
def info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             """Доступны следующие команды:
                             /start - приветствие,
                             /info - информация,""")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'Привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    word = update.message.text
    print(word)
    # if 'mod' in word:
    #     context.bot.send_message(update.effective_chat.id, anecAPI.modern_joke())
    # if 'sov' in word:
    #     context.bot.send_message(update.effective_chat.id, anecAPI.soviet_joke())
    # else:
    #     context.bot.send_message(update.effective_chat.id, anecAPI.random_joke())

def give_word(update,context):
    word = update.message.text
    
    # list_num = parse(word)
    # list_result = bracket_opening(list_num)
    # result = calculate(list_result)
    #context.bot.send_message(update.effective_chat.id, result)

    # word = update.message.text
    # if "бар" in word:
    #     joke = '''Белый медведь заходит в паб и говорит бармену:
    #             - Дайте мне виски и... кока-колу.
    #             - А почему такая пауза? - спрашивает бармен.
    #             - Это всё, что вас удивляет? - с обидой говорит медведь.'''
    #     context.bot.send_message(update.effective_chat.id, joke)
    #     return joke
    # elif "пока" in word:
    #     context.bot.send_message(update.effective_chat.id, 'Покачивай шляпой из бара')
    #     return word
    # context.bot.send_message(update.effective_chat.id, 'Вы, как всегда, правы, милорд')