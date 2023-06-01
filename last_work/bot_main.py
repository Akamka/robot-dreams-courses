import logging
import telebot
import requests
import os
from telebot import types

# логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

bot = telebot.TeleBot("6299259595:AAEDdiUHF9BbeqqCFtpicJpgApNiUhakcq0")

REMOVE_BG_API_KEY = "6GGfogP2U79WQrVqWxVxfvvG"

START, PHOTO = range(2)

# Ограничения для разных форматов
FORMAT_LIMITS = {
    'PNG': 10 * 4000 * 2500,  # 10 Мп
    'JPG': 25 * 6250 * 4000,  # 25 Мп
    'ZIP': 25 * 6250 * 4000  # 25 Мп
}



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Send Photo'))

    bot.send_message(message.chat.id, 'Приветик! Я бот для редактирования твоих фотографий!\nОбрати внимание, '
                                      'что перед каждым использованием нужно писать команду "start"😘\n'
                                      'PS: фото может быть отправлено только в трех форматах: PNG, JPG, ZIP\n'
                                      'PNG - до 10 Мп\nJPG - до 25 Мп\nZIP - до 25 Мп', reply_markup=markup)

    bot.register_next_step_handler(message, process_photo)


# Обработчик получения фото
def process_photo(message):
    if message.text == 'Send Photo':
        bot.send_message(message.chat.id, 'Пожалуйста, отправь мне фото для редактирования.')

        bot.register_next_step_handler(message, process_received_photo)


# Обработчик получения фото
def process_received_photo(message):
    if message.content_type == 'photo':
        # Проверяем размер фото
        photo_id = message.photo[-1].file_id
        photo_info = bot.get_file(photo_id)
        photo_path = photo_info.file_path

        photo_url = f"https://api.telegram.org/file/bot{bot.token}/{photo_path}"
        response = requests.get(photo_url)

        format_name = os.path.splitext(photo_path)[1][1:].upper()
        format_limit = FORMAT_LIMITS.get(format_name)

        if len(response.content) > format_limit:
            bot.send_message(message.chat.id, f'Превышен максимальный размер файла для формата {format_name}.')
            return

        photo_data = response.content

        # Отправка фото на удаление фона
        remove_bg_url = "https://api.remove.bg/v1.0/removebg"
        headers = {"X-Api-Key": REMOVE_BG_API_KEY}
        files = {"image_file": photo_data}
        try:
            remove_bg_response = requests.post(remove_bg_url, headers=headers, files=files)
            remove_bg_response.raise_for_status()

            if remove_bg_response.status_code == 200:
                temp_filename = "photo_without_bg.png"

                with open(temp_filename, "wb") as file:
                    file.write(remove_bg_response.content)

                with open(temp_filename, "rb") as file:
                    bot.send_photo(message.chat.id, file)

                os.remove(temp_filename)

                bot.send_message(message.chat.id, 'Фото готово, удачи!')
            else:
                bot.send_message(message.chat.id, 'Произошла ошибка при удалении фона.')

        except requests.exceptions.HTTPError as e:
            bot.send_message(message.chat.id, f'Ошибка HTTP: {e}\nОтправленое фото не подходит по требованиям.\nЯ не могу его обработать((')
            

        except requests.exceptions.RequestException as e:
            bot.send_message(message.chat.id, f'Произошла ошибка: {e}')


@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.send_message(message.chat.id, 'Извини, я не понимаю эту команду.')


bot.polling()
