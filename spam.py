import os
from telethon import TelegramClient

import asyncio

API=7382727
Hash="671902f3c9760c245232991768c758b5"
from keep_alive import keep_alive

client = TelegramClient('OWNER 💫@Deadly_kira💫', API, Hash )


print("Working!")


async def main():
  i = 1
  while True:

    group_id= write the chat id where u wanna spam


    try:
      
      msg = await client.send_message(group_id, str(i))
      i=i+1 
      await asyncio.sleep(0.8)
      await client.delete_messages(group_id, msg.id)
      await asyncio.sleep(0.8)
    except Exception as e:
      print(e)


keep_alive()
client.start()
client.loop.run_until_complete(main())
