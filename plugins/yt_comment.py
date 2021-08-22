#~ ported from Old Friday

import urllib
import random
import requests
from telegraph import upload_file
from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text

AVATARS = [
     "https://telegra.ph//file/77c17cea26e8c24c36ea8.jpg",
     "https://telegra.ph//file/e7f88921671418be96686.jpg",
     "https://telegra.ph//file/10371646861fcfb521195.jpg",
     "https://telegra.ph//file/1ab533ec778f56c4ecc5f.jpg",
     "https://telegra.ph//file/75b0d1a20e8e9283c067b.jpg",
     "https://telegra.ph//file/7939490055915bed0585c.jpg",
     "https://telegra.ph//file/cd6dd4acae3c276c065be.jpg",
     "https://telegra.ph//file/fced18b5d48c0cc3abb46.jpg",
     "https://telegra.ph//file/79f1ccebc6aba285c6038.jpg",
     "https://telegra.ph//file/a3423cefc893a6cd6032d.jpg",
     "https://telegra.ph//file/2cc12ce620a035510b71d.jpg",
     "https://telegra.ph//file/f40ec98eb82f48e301480.jpg",
     "https://telegra.ph//file/e14a9c34b0bd6dab04333.jpg",
     "https://telegra.ph//file/d782da8113a71bbd6e64c.jpg",
     "https://telegra.ph//file/e3d4ac98f08cc3e1a5c74.jpg",
     "https://telegra.ph//file/f5fe3e20d9ff18edf2cde.jpg",
     "https://telegra.ph//file/156fb0e4fb7b16e1ad53f.jpg",
     "https://telegra.ph//file/46997187cdadd13af1a4a.jpg",
     "https://telegra.ph//file/e4484c6f3aafb531881fe.jpg",
     "https://telegra.ph//file/8706beb96352012a02225.jpg",
     "https://telegra.ph//file/42af4f48fa7684cd9709e.jpg",
     "https://telegra.ph//file/b835311fae7dfbcb5a110.jpg",
     "https://telegra.ph//file/13e782d79a69df17256ac.jpg",
     "https://telegra.ph//file/556d9f06cedd634dc6e0b.jpg",
     "https://telegra.ph//file/63b7803170528445cd2ea.jpg",
     "https://telegra.ph//file/19364431c410895b30666.jpg",
     "https://telegra.ph//file/02a9eec0c7d58a9a2d2da.jpg",
     "https://telegra.ph//file/99c47bba3528fb3513bf7.jpg",
     "https://telegra.ph//file/04b8c4fdcecc4f08a0337.jpg",
     "https://telegra.ph//file/56fc54bdb387b21508dc4.jpg",
     "https://telegra.ph//file/06f01066e22923b3fa07c.jpg",
     "https://telegra.ph//file/3be8c6038f938679b287a.jpg",
     "https://telegra.ph//file/c84d1903f515c2bd9a5a5.jpg",
     "https://telegra.ph//file/f73ab4cb251dd5a1faeb6.jpg",
     "https://telegra.ph//file/199fb4dfabb5a966e2cc5.png",
     "https://telegra.ph//file/6c154cf21a9debdeb0f10.jpg",
     "https://telegra.ph//file/199fb4dfabb5a966e2cc5.png",
     "https://telegra.ph//file/9173ece9ac42e18bca59f.jpg",
     "https://telegra.ph//file/34f4d70b52785b6c7d519.jpg",
     "https://telegra.ph//file/9d197b2720c58bd7635d6.png",
     "https://telegra.ph//file/cd793eb6485c251acb821.png",
     "https://telegra.ph//file/bdf9039fd7adcf74c64ea.png",
     "https://telegra.ph//file/b9770ec62a54fefd466b2.jpg",
 ]
@friday_on_cmd(['rytc'],
    cmd_help={
    "help": "generate a fake ytc comment with random profile pic",
    "example": "{ch}rytc <text>"
    })
async def yt_comment(client, message):
 await message.edit("`Making Comment`")
 text = get_text(message)
 text = urllib.parse.quote_plus(text)
 name = client.me.first_name
 link = random.choice(AVATARS)    
 lol = f"https://some-random-api.ml/canvas/youtube-comment?avatar={link}&username={name}&comment={text}"
 await client.send_photo(message.chat.id, lol, caption=f"__**Team  F.R.I.D.A.Y**__")
 await message.delete()
 
 
 
@friday_on_cmd(['ytc'],
    cmd_help={
    "help": "generate a fake ytc comment with ur own profile pic",
    "example": "{ch}ytc <text>"
    })
async def yt_comment(client, message):
 await message.edit("`Making Comment`")
 text = get_text(message)
 text = urllib.parse.quote_plus(text)
 name = client.me.first_name
 img = await client.get_profile_photos("me", limit = 1)
 pic = await client.download_media(img[0].file_id)
 kk = upload_file(pic)
 imglink = f"https://telegra.ph{kk[0]}"
 lol = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&username={name}&comment={text}"
 await client.send_photo(message.chat.id, lol, caption=f"__**Team  F.R.I.D.A.Y**__")
 await message.delete()