import telebot
from datetime import datetime as dt
import logging
import operations as o
from operations import read_csv, tasks
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import stickers as st
import config
from phonebook_bot import choice
bot = telebot.TeleBot(config.TOKEN)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора

START,MAIN_MENU, SUB_MENU, MENU, EDIT, ADD, DELETE, VIEW, SEARCH, SEARCH_MENU, GET_TASK, GET_DATE, DATA, TIME = range(14)

'👀☑🔍📎🎬🎮'
TIME_NOW = dt.now().strftime('%D_%H:%M')

# функция обратного вызова точки входа в разговор

def start(update, context):
    reply_keyboard = [['🎬START','🚪EXIT']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_sticker(update.message.chat.id, st.welcome)
    context.bot.send_message(update.effective_chat.id,
                     f'Добро пожаловать в список дел, {update.effective_user.first_name}!\n'
        'Для начала работы со списком нажмите кнопку 🎬START\n'
        'Для выхода нажмите кнопку 🚪EXIT', reply_markup=markup_key)

    return MAIN_MENU


def main_menu(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    choice = update.message.text
    if choice == '🎬START':
        return sub_menu(update, context)
    if choice == '🚪EXIT':        
        return cancel(update, context)

def sub_menu(update, context):
    reply_keyboard = [['👀 VIEW', '📝 ADD','🔎 SEARCH', '❌ DELETE', '✍ EDIT', '🚪 EXIT']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_sticker(update.message.chat.id, st.hello)
    update.message.reply_text('Выберете действие со списком дел 🧐', reply_markup=markup_key)
    return MENU

def menu(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    choice = update.message.text
    if choice == '👀 VIEW':
        return view(update, context)
    if choice == '📝 ADD':
        update.message.reply_text('Введите задачу сэр: ')
        return ADD
    if choice == '🔎 SEARCH':
        context.bot.send_sticker(update.message.chat.id, st.listen)
        context.bot.send_message(update.effective_chat.id,
                     f'Что бы вы хотели найти, Мастер {update.effective_user.first_name}: ')
        return SEARCH
    if choice == '❌ DELETE':
        update.message.reply_text("Найти задачу для удаления: ")
        return DELETE
    if choice == '✍ EDIT':
        update.message.reply_text("Найти задачу для редактирования: ")
        return EDIT    
    if choice == '🚪 EXIT':
        return cancel(update, context)


def view(update, context):
    user = update.message.from_user
    logger.info("Контакт %s: %s", user.first_name, update.message.text)
    context.bot.send_sticker(update.message.chat.id, st.view_sticker)
    context.bot.send_message(update.effective_chat.id,
                     f'А вот и список задач, {update.effective_user.first_name} ')
    tasks = read_csv()
    tasks_string = o.view_tasks(tasks)
    update.message.reply_text(tasks_string)
    return sub_menu(update, context)

def add(update, context):
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    name = update.message.text
    context.user_data['name'] = name
    update.message.reply_text("Сэр, Введите дату в формате ДД/ММ/ГГ: ")
    return DATA

def data(update, context):
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    data = update.message.text
    data += '_'
    context.user_data['data'] = data
    update.message.reply_text("Сэр, Введите время в формате ЧЧ:ММ ")
    return TIME

def time(update, context):
    tasks = read_csv()
    task = {}
    update.message.reply_text(f'{task}')
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    time = update.message.text
    data = context.user_data.get('data') + time
    name = context.user_data.get('name')
    task['Имя'] = user.first_name
    task['Фамилия'] = user.last_name
    task['Текущая дата'] = TIME_NOW
    task['Дата выполнения'] = data
    task['Задача'] = name
    update.message.reply_text(f'{task}')
    tasks.append(task)
    o.write_csv(tasks)
    context.bot.send_sticker(update.message.chat.id, st.complete)
    context.bot.send_message(update.effective_chat.id,
                    f'Мастер {update.effective_user.first_name}, задача успешно добавлена!:')
    return sub_menu(update, context)


def search(update, context):
    user = update.message.from_user
    logger.info("Выбор поиска: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    tasks = read_csv()
    if searchstring==[]:
            context.bot.send_message(update.effective_chat.id,
                    f' {update.effective_user.first_name}, по вашему запросу "{searchstring}" ничего не найдено:')
    else:
        tasks_filter = o.filter_task(user.first_name, tasks)
        searched_tasks = o.search_task(searchstring, tasks)
        context.bot.send_message(update.effective_chat.id,
                        f' {update.effective_user.first_name}, по вашему запросу "{searchstring}" найдено:')
        update.message.reply_text('🧐')
        tasks_string = o.view_tasks(searched_tasks)
        update.message.reply_text(tasks_string)

    return sub_menu(update, context)

    


def delete(update, context):
    tasks = read_csv()
    user = update.message.from_user
    logger.info("Выбор удаления: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    o.delete_task(searchstring, tasks)
    context.bot.send_sticker(update.message.chat.id, st.complete)
    update.message.reply_text('Задача удалена, сэр.')
    o.write_csv(tasks)
    return sub_menu(update, context)

    
def edit(update, context):
    tasks = read_csv()
    user = update.message.from_user
    logger.info("Выбор редактирования: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    o.edit_task(searchstring, tasks)
    context.bot.send_sticker(update.message.chat.id, st.complete)
    update.message.reply_text('Задача отредактирована, сэр.')
    o.write_csv(tasks)
    return sub_menu(update, context)



def cancel(update, context):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    context.bot.send_sticker(update.message.chat.id, st.goodbye)
    context.bot.send_message(update.effective_chat.id,
                     f'До новых встреч, {update.effective_user.first_name}. 👋'
        'Для вызова меню списка дел нажмите /start')
    context.bot.send_sticker(update.message.chat.id, st.relax)
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    game_conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            VIEW: [MessageHandler(Filters.text, view)],
            START: [CommandHandler('start', start)],
            SUB_MENU: [MessageHandler(Filters.text, sub_menu)],
            ADD: [MessageHandler(Filters.text, add)],
            DELETE: [MessageHandler(Filters.text, delete)],
            SEARCH: [MessageHandler(Filters.text, search)],
            MENU: [MessageHandler(Filters.text, menu)],
            MAIN_MENU: [MessageHandler(Filters.text,main_menu)],
            EDIT: [MessageHandler(Filters.text, edit)],
            DATA: [MessageHandler(Filters.text, data)],
            TIME: [MessageHandler(Filters.text, time)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(game_conversation_handler)

    # Запуск 
    print('SERVER_STARTED')
    updater.start_polling()
    updater.idle()