from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN

user_data = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام خوش اومدی به لوان دیجی!\nاسم شما؟")

def handle_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    if chat_id not in user_data:
        user_data[chat_id] = {"name": text}
        update.message.reply_text("چه کمکی ازم برمیاد؟ مثلاً بفرمایید چه بودجه‌ای دارید و لپ‌تاپ رو برای چه کاری می‌خواید؟")
    elif "need" not in user_data[chat_id]:
        user_data[chat_id]["need"] = text
        update.message.reply_text("فوق‌العاده! آیا نقد می‌خواید یا اقساط؟")
    elif "payment" not in user_data[chat_id]:
        user_data[chat_id]["payment"] = text
        update.message.reply_text("لطفاً شماره تماس‌تون رو بفرستید.")
    elif "phone" not in user_data[chat_id]:
        user_data[chat_id]["phone"] = text
        update.message.reply_text("کی تشریف میارید فروشگاه؟ با یه کد تخفیف ویژه هم پذیرای شما هستیم.")
    elif "visit_date" not in user_data[chat_id]:
        user_data[chat_id]["visit_date"] = text
        update.message.reply_text("ممنون! اطلاعات شما ثبت شد. به زودی همکارمون باهاتون تماس می‌گیره.")

        # در اینجا میشه اطلاعات رو ذخیره کرد در Google Sheets یا فایل
        print(user_data[chat_id])

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
