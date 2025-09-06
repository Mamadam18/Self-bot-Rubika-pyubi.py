from pyrubi import Client
from pyrubi.types import Message
from datetime import datetime
import time, threading

bot = Client('t2')

TYPE_SPEED = 0.08  
CLOCK_DURATION = 60  
digit_map = str.maketrans("0123456789:", "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿:")

def fancy_clock():
    ts = datetime.now().strftime("%H:%M:%S")
    return f"⏰ {ts.translate(digit_map)}"

hearts = ["🩶","🤎","💙","🩵","💚","💛","🧡","🤍"]

animations = {
    "بارون": ["💧","💧💧","🌧️","☔"],
    "آتیش": ["🔥","🔥💥","🔥💥✨","💥✨🔥"],
    "دست": ["👏","👏👏","👏👏👏","👏👏👏👏"],
    "موشک": ["🚀","🚀💨","🚀🌌","🌕"]
}

@bot.on_message()
def on_message(ms: Message):
    if not ms.text:
        return
    threading.Thread(target=handle_message, args=(ms,)).start()

def handle_message(ms: Message):
    text = ms.text.strip()
    object_guid = ms.object_guid
    message_id = ms.message_id

    if "سلام" in text:
        for h in hearts:
            try:
                bot.edit_message(object_guid=object_guid, message_id=message_id, text=f"{text} {h}")
                time.sleep(1)
            except:
                break
        return

    for key, frames in animations.items():
        if key in text:
            for f in frames:
                try:
                    bot.edit_message(object_guid=object_guid, message_id=message_id, text=f"{text} {f}")
                    time.sleep(1)
                except:
                    break
            return

    words = text.split()
    typed_text = ""
    for word in words:
        if typed_text:
            typed_text += " "
        for i in range(len(word)):
            typed_text += word[i]
            try:
                bot.edit_message(object_guid=object_guid, message_id=message_id, text=typed_text)
                time.sleep(TYPE_SPEED)
            except:
                return
        typed_text += "" 
        
    try:
        bot.edit_message(object_guid=object_guid, message_id=message_id, text=f"**{text}**\n\n{fancy_clock()}")
    except:
        return

    start = time.time()
    while time.time() - start < CLOCK_DURATION:
        try:
            bot.edit_message(object_guid=object_guid, message_id=message_id, text=f"**{text}**\n\n{fancy_clock()}")
            time.sleep(5)
        except:
            break

bot.run()