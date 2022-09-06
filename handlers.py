from main import bot, dp
from aiogram.types import Message
from data.config import admintsId
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gAuth = GoogleAuth()
gAuth.LocalWebserverAuth()
file = GoogleDrive(gAuth).CreateFile({'title': f'menu.txt'})



async def set_content_to_file(content):
    file.SetContentString(content)
    file.Upload()


async def f(dp):
    await set_content_to_file("test")
    await send_to_admin(dp)


def create_and_upload_file(file_name='text.txt', content='text'):
    try:
        drive = GoogleDrive(gAuth)

        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentString(content)
        my_file.Upload()

        return f'File {file_name} was uploaded!Have a good day!'
    except Exception as _ex:
        return 'Got some trouble, check your code please!'


async def send_to_admin(dp):
    await bot.send_message(chat_id=admintsId, text="я бот пиши мне меню,только одним сообщением")


@dp.message_handler()
async def echo(message: Message):
    text = f"окей я всё записал,если че пиши ещё"
    await set_content_to_file(message.text)
    await message.answer(text=text)

