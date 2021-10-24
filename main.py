from pyrogram import Client, filters, idle
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import os
from pyrogram.types import Message
from urllib import request
import requests
from pyquery import PyQuery as pq

bot_token = os.environ.get('TOKEN')

api_id= os.environ.get('API_ID')

api_hash = os.environ.get('API_HASH')

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
# credit  https://github.com/kamronbek29/pinterst_downloader/blob/master/pinterest-downloader.py thanks for create this repository!
def get_download_url(link):
    # Make request to website 
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    # Get content from post request
    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = pq(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')

    return download_url


@app.on_message(filters.command(["start"]))
async def start(client, message):
  keyboard= InlineKeyboardMarkup( [
     [ 
        InlineKeyboardButton("Bot Channel", url='https://t.me/nekozu'),
     ]
	] )                                                                                                                                                                                                      
	 await message.reply_text("Hey! Im bot to download gif. video. photo from pinterest. how to use? simply. use /p command and space then pacte you url. example /phttps://pin.it/4LH0f6K. ", reply_markup=keyboard)       

@app.on_message(filters.command(["p"]))
async def p(_, message: Message):
    await message.reply_text("`Downloading The File..`")
    query = get_text(message)
    down = get_download_url(query)
    if '.mp4' in (down):
        await message.reply_video(down)
    elif '.gif' in (down):
         await message.reply_animation(down)
    else:
        await message.reply_photo(down)
app.start()
idle()
