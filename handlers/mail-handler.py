from pyrogram import Client
from aiogram.types import Message, Document, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import tgcrypto
from config import api_hash, api_id, phone, token

rt = Router()

@rt.callback_query(F.data == 'mailing_list')
async def mail(callback: CallbackQuery):
    await callback.message.answer('Выбери, как ты хочешь отправить список для рассылки')
    keyboard = InlineKeyboardBuilder().add([
        [InlineKeyboardButton(text='Сообщением', callback_data='message_data')],
        [InlineKeyboardButton(text='.txt Файлом', callback_data='txt_data')],
        [InlineKeyboardButton(text="Вернуться в мнею", callback_data='start')]
    ])
    await callback.message.edit_reply_markup(reply_markup=keyboard.as_markup())

@rt.callback_query(F.data == 'message_data')
async def mail_message(callback: CallbackQuery):
    await rt.message.answer('Отправть мне список в выбранном формате')
    InlineKeyboardBuilder().add([InlineKeyboardButton(text='Отмена', callback_data='mail')])

    @rt.message(F.text)
    async def handle_message_data_text(message: Message):
        text = message.text
        return text

    await callback.message.answer('Отправь мне список пользователей через строку (например:\n@user1\n@user2\n123456789)')

    @rt.message(F.text)
    async def process_user_list(message: Message, text):
        user_list = message.text.strip()
        user_list = [user.replace('@', '') for user in user_list]
        try:
            userbot = Client(api_hash=api_hash, api_id=id, phone_number=phone)
            userbot.start()
            await callback.message.answer('Отправка пошла...')
            InlineKeyboardBuilder().add([InlineKeyboardButton(text='Отмена', callback_data='mail')])
            for user in user_list:
                try:
                    userbot.send_message(chat_id=user, text=text)
                except:
                    await callback.message.answer(f'Не удалось отпраить сообщение пользователю {user}')
            userbot.stop()
        except:
            await callback.message.answer('Ошибка Юзербота, обратитесь в поддержку')
            await mail(callback)

@rt.callback_query(F.data == 'txt_data')
async def mail_txt(callback: CallbackQuery):
    await rt.message.answer('Отправть мне список в выбранном формате')
    InlineKeyboardBuilder().add([InlineKeyboardButton(text='Отмена', callback_data='mail')])

    @rt.message(F.text)
    async def handle_txt_data_text(message: Message):
        text = message.text
        return text
    

    await callback.message.answer('Отправь мне файл .txt со списком пользователей')

    @rt.message(F.document)
    async def process_file(message: Message, text):
        if message.document.mime_type != 'text/plain':
            await callback.message.answer('Пожалуйста, отправь файл в формате .txt')
            return

        # Загружаем файл и обрабатываем его содержимое
        file = await message.document.download()
        with open(file, 'r', encoding='utf-8') as f:
            user_list = f.readlines()
        
        user_list = user_list.strip()
        user_list = [user.replace('@', '') for user in user_list]
        try:
            userbot = Client(api_hash=api_hash, api_id=api_id, phone_number=phone)
            userbot.start()
            await callback.message.answer('Отправка началась...')
            InlineKeyboardBuilder().add([InlineKeyboardButton(text='Отмена', callback_data='mail')])
            for user in user_list:
                try:
                    
                    userbot.send_message(chat_id=user, text=text)
                except:
                    await callback.message.answer(f'Не удалось отпраить сообщение пользователю {user}')
            userbot.stop()
        except:
            await callback.message.answer('Ошибка Юзербота, обратитесь в поддержку')
            await mail(callback)
