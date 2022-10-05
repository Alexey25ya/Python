from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import*


app = ApplicationBuilder().token("5713533191:AAFfNZoiIbREl4wdCY6lZdVE2rPG09wOj0w").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print('server start')
app.run_polling()



# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time. sleep(0.2)
#     bar.next()
# bar.finish()

