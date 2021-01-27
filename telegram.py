ADAFRUIT_IO_USERNAME = "ameenmanna8824"
ADAFRUIT_IO_KEY = "3d4c4a5ea05940efabe546afd681cad9"

from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
amn = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY) # Client here is objectdef on(bot,update):
  chat_id = update.message.chat_id
  amn.create_data('telegram',Data(value=1))#telegram is the feed name
  bot.send_message(chat_id=chat_id,text = "LIGHT IS TURNED ON")
  def on(bot,update):
  chat_id = update.message.chat_id
  amn.create_data('telegram',Data(value=1))#telegram is the feed name
  bot.send_message(chat_id=chat_id,text = "LIGHT IS TURNED ON")
  #updater = Updater('1565933627:AAEl4xDPOqVTwpP-dsSlgdRnKukndV1AW80')
  updater = Updater('1561181436:AAEIjnS2JfEZTeeJVoahlDkVKO-o3MLujnU')
 dp = updater.dispatcher #updater is object and .dispatcher is attribute
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling() #updater is object and .start_polling() is method
updater.idle() #updater is object and .idle() is method
