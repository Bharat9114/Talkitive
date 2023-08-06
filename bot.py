import os
import time
import telebot
import random
from bardapi import Bard
os.environ['_BARD_API_KEY']="XQjdWmi_NTUXEdTa4-5gxW7FSgpQb4K0D09IYttgeTQ5SdCAbX9nWDYrnWA2OYqUNWm3aQ."
TOKEN="6148950609:AAH6AgkM7M3Yo9EkngF2n3hg4N9Hal-zNlM"
bot=telebot.TeleBot("6148950609:AAH6AgkM7M3Yo9EkngF2n3hg4N9Hal-zNlM")
@bot.message_handler(['start'])
def start(message):
  bot.reply_to(message,"Heluuu !!!! I am so Talkitive that my name is Talkitive by user.I am not a Group Bot I am introvert so TUM AUR MAI!.BTW I can help you with following:\n 1.I can answer your questions in an informative way, even if they are open ended, challenging, or strange.\n 2.I can generate different creative text formats of text content, like poems, code, musical pieces, email, letters, etc. I will try my best to fulfill all your requirements.\n 3.I can tell you weather,time,date,sport score,News,etc.\n 4. I can translate for you.\n 𝐈 𝐚𝐦 𝐬𝐭𝐢𝐥𝐥 𝐮𝐧𝐝𝐞𝐫 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐦𝐞𝐧𝐭, 𝐛𝐮𝐭 𝐈 𝐚𝐦 𝐥𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐧𝐞𝐰 𝐭𝐡𝐢𝐧𝐠𝐬 𝐞𝐯𝐞𝐫𝐲 𝐝𝐚𝐲. 𝐈 𝐚𝐦 𝐚𝐥𝐰𝐚𝐲𝐬 𝐡𝐚𝐩𝐩𝐲 𝐭𝐨 𝐡𝐞𝐥𝐩 𝐢𝐧 𝐚𝐧𝐲 𝐰𝐚𝐲 𝐭𝐡𝐚𝐭 𝐈 𝐜𝐚𝐧. 𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞, 𝐟𝐞𝐞𝐥 𝐟𝐫𝐞𝐞 𝐭𝐨 𝐚𝐬𝐤 𝐦𝐞 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠!\n Hope you will spend great time with me . Go to /help for more infos. ")

@bot.message_handler(['help'])
def help(message):
  bot.reply_to(message,"""/start -----→ Greetings
  /help -----→ Get help regarding Bot
  /dev -----→ Know about Bot's developer
  /about -----→ Know Bot and it's capablities
  /shayari -----→ Suggest Random Selected Shayries
  /Contact -----→ Contact My Owner
  /tgsong -----→ Listen or Download any song from any artist INDIAN or any
  < YOUR MESSAGE > -----→ I will reply you on this, You just ask  """)

@bot.message_handler(['shayari'])
def shayari(message):
  bot.reply_to(message,"This Page is under Developement. However Use /nSD to try feature. \n Right here are some links provided by DEV That will fulfill you need :\n 1. GALIB SHAYARI: https://t.ly/lcd1 \n 2.Ada Jafri : https://www.rekhta.org/poets/ada-jafarey/all \n 3. Gulzaar Saheb: https://www.rekhta.org/poets/gulzar/all \n 4. Jhon keats : t.ly/D2ZM \n 5. Love Shayri Eng: t.ly/hyta \n 6. Love shayri Hindi: http://rb.gy/u87p6 \n These are from Devs collection")

@bot.message_handler(['nSD'])
def nSD(message):
  sh=["""Bina Tere Shehar Ka Shehar Veeraan Rehta Hai,
Bichhad Ke Tujhse Har Rasta Sunsaan Rehta Hai,
Woh Tujhe Tujh Se Jyada Pyaar Karta Hai,
Jo Tere Saamne Aksar Anjaan Rehta Hai
""","""Chup-Chap Se Rehte Hain Wo Aksar,
Zulfein Bhi Suna Hai Ki Sanwara Nahi Karte,
Din Raat Gujarte Hain Unke Bechain Se,
To Chain Se Hum Bhi Gujara Nahi Karte
""","""Armaan Tamaam Umr Ke Seene Mein Dafan Hain,
Hum Chalte Firte Log Mazaaron Se Kam Nahi
""","""Tumko Yaad Rakhne Mein Main Kya-Kya Bhool Jaata Hoon,
Jo Dil Mein Baat Hai Tumko Bataana Bhool Jaata Hoon,
Tumhare Lab Ko Chhoone Ka Iraada Roj Karta Hoon,
Najar Tumse Jo Mil Jaaye Zamana Bhool Jaata Hoon.
""","""Bewafai Karke Niklun To Wafa Kar Jaunga,
Shahar Ko Har Zayke Se Aashna Kar Jaunga,
Tu Bhi Dhoondega Mujhe Shauq-e-Saza Mein Ek Din,
Main Bhi Koi Khoobsurat Si Khata Kar Jaunga.
""","""Aaj Teri Yaaad Ko Seene Se Laga Ke Roye,
Khayalo Me Tujhe Pas Bulake Roye,
Haazar Baar Pukara Tujhko Tanhai Me,
Har Bar Tujhe Paas Na Pakar Roye.
"""]
  l=random.choice(sh)
  bot.reply_to(message,l+"\n --𝗚𝘂𝗹𝘇𝗮𝗮𝗿 𝗦𝗮𝗵𝗲𝗯 ")

@bot.message_handler(['dev'])
def dev(message):
  bot.reply_to(message,"His name is BELU or Shwet. How ever he turned 18 ... You can wish him on 9 Nov. ᴜꜱᴇ ꜱᴏɴᴀ ᴘᴀꜱᴀɴᴅ ʜᴀɪ ᴋᴀꜰɪ! ᴀʙʜɪ ʙʜɪ ꜱᴏ ʀᴀʜᴀ ʜᴏɢᴀ . ᴍᴀᴛʟᴀʙ ᴅɪɴ ᴍᴇ ꜱᴏɴᴀ ʀᴀᴀᴛ ᴍᴇ ᴊᴀɢta hai. ᴜꜱᴋᴇ ᴋᴜᴄʜ ᴅᴏꜱᴛ ᴜꜱᴇ ᴜʟʟᴜ ʙᴜʟᴀᴛᴇ ᴡᴇʟʟʟʟ ᴍᴀɪ ʙʜɪ . ᴀᴜʀ ᴊᴀɴᴏɢᴇ ᴛᴏ ᴅᴜɴɪʏᴀ ᴋᴇ ʟᴏɢᴏ ꜱᴇ ᴠɪꜱʜᴡᴀᴀꜱ ᴜᴛʜ ᴊᴀʏᴇɢᴀ .He need a partner but GOD Always gift him With Friends.भाई की जिंदगी में लड़की आएगी ek din,Uppar wala hai naa. \n Contact on TELEGRAM: https://t.me/beluga_is_mad")

@bot.message_handler(['about'])
def about(message):
  bot.reply_to(message,"""
  Version 0.1
  As earlier I told you what i can do. My Artificial is not final soon many Features will be added.
  I can comunicate in ENGLISH,FRENCH,GERMAN,SPANISH,CHINESE,RUSSIAN,JAPANESE,KOREAN and CHINESE. I can translate a message in any language.
  I am coded using Python Language by Shwet.
  This the Second AI CHAT BOT in INDIA For TELEGRAM Based on Large Language Module and SICM. My Python Module is Owned is Acheong and Modified by Shwet with full legal permit.
  Features Like assistance ,Playing Music , sending Emails, Genrating AI images,many more are part of my Task , are yet to be added.
  Note That My memory is very Short , I don't Remember anything. This can be improved my dev is working.....
  With Regards
  TALKITIVE AND BELU""")

@bot.message_handler(['contact'])
def contact(message):
  bot.reply_to(message,"""
Telegram : http://rb.gy/cp55q
Instagram : http://rb.gy/jdhho
Gmail: shwetpurwar0911@gmail.com """)

@bot.message_handler(['tgsong'])
def tgsong(message):
  bot.reply_to(message," START THE BOT > Type Your song/artist name > Enjoy or Download . VK ALL SONG : https://t.me/vkmusic_bot")

  # List of random messages and stickers
random_messages = ['AI is getting you >>>','Kuch Second Ruk Jaa Yaar...','Khoja Raha hu....','Typing....',"Finding the best answer...,","Abbe Ruk Jaa"]

random_stickers = [
    'CAACAgIAAxkBAAEJp4dkrINdOFHKRMshWXgsCtyNykJO5gACJQ8AAkuTkUjrHBy-H6OZCi8E',
    'CAACAgIAAxkBAAEJp4lkrIO3Se6UNnDsAhX2MdPOZLBuBAACBRAAAn-WSEirjcU2x7PvmS8E',
    'CAACAgIAAxkBAAEJp4tkrIQUZZc_BxwWcxn9kc4U9_RDtAACyxAAAoOIoUozbCeynN_5jy8E',
    'CAACAgQAAxkBAAEJp5FkrIWk0KuhgQIvzHUzNNclEEVxuQACKAoAAl1_SVLYBr3TuI91-y8E',
    'CAACAgIAAxkBAAEJqQxkrXgYM6GQgcwrvYVUfQfQAAFVl_4AAmcFAAI_lcwKKH7lBu6-OdQvBA',
    'CAACAgIAAxkBAAEJp5VkrIZ9_5TlyeqZjdSgOjQZinjBCgACdQADS0IiEYnt2zJ2iiz9LwQ',
    'CAACAgIAAxkBAAEJqQ5krXhK66X24xesFP-DppY8BP743AAChQADS0IiESnST_fiDtpULwQ',
    'CAACAgIAAxkBAAEJqRBkrXhNbTRV1EaYK1fxubP4xUmdYwACdAADS0IiEbBA8ru-DdxTLwQ',
    'CAACAgIAAxkBAAEJqRRkrXh_LcKLY3oNGVgPEDXGeUaH7wACBAEAAladvQreBNF6Zmb3bC8E',
    'CAACAgIAAxkBAAEJqRhkrXifFXQkq29xeBlfvkyfRFmkoQACIhMAAl1scEuuLYe9O-OAPi8E',
    'CAACAgIAAxkBAAEJqRZkrXiHR-BcDh7YPxd_PHHqTB4xWQACSQIAAladvQoqlwydCFMhDi8E',
    'CAACAgIAAxkBAAEJqRpkrXisTh2pO6z80HKZLX2y5oOlUAACfRQAAkm1IUjehEBphgJn4y8E',
    'CAACAgIAAxkBAAEJqRxkrXi1u5Vbj_Znc_3LdC53WsD68AAC4BUAAhyiGEjF4kD_M1t33C8E',
    'CAACAgEAAxkBAAEJqSBkrXlOBsbG5xMH27WBLdNIlrwWhwACCwADmQRgTtAdYVimk67CLwQ'
]
@bot.message_handler()
def answer(message):
  try:
    sent_message=bot.send_message(message.chat.id, random.choice(random_messages))
    sent_sticker = bot.send_sticker(message.chat.id, random.choice(random_stickers))
    q=message.text
    print(q)
    p=Bard().get_answer(q)['content']
    print(p)

    # Send a random sticker
    # Simulate some processing time
    # Replace this with your actual logic or API calls
    # For demonstration purposes, we'll sleep for 3 seconds
    time.sleep(3)
  except Exception as e:
    print("error")
    p="Error in Fetching Info, Dev will be informed"
  bot.delete_message(message.chat.id, sent_message.message_id)
  bot.delete_message(message.chat.id, sent_sticker.message_id)
  bot.reply_to(message,p+"\n𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 𝐁𝐄𝐋𝐔𝐆𝐀 𝐀𝐈 𝐋𝐋𝐌")
bot.polling()
