from pyrogram import Client, filters
import datetime
import random
import time
import pymongo

db = pymongo.MongoClient("mongodb+srv://GT:GT@cluster0.tjoiaxo.mongodb.net/?retryWrites=true&w=majority").my_db

@Client.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def handle_message(client, message):
    try:
        if message.text.startswith("@admin"):
            # Send the loading message
            loading_message = await message.reply("Report sending ○○○○○")

            report_text = message.text[6:]
            report_time = f"{datetime.datetime.now().strftime('%I:%M:%S %p')}"
            report_date = f"{datetime.datetime.now().strftime('%d-%m-%Y')}"
            report_day = f"{datetime.datetime.now().strftime('%A')}"
            track_id = f"#MB{random.randint(1, 1000000)}"
            report_top = "✅ Rᴇᴘᴏʀᴛ sᴇɴᴅ ᴛᴏ ᴀᴅᴍɪɴ ✅"
            report = {
                "report_top": report_top,
                "reporter": message.from_user.first_name,
                "reporter_id": message.from_user.id,
                "track_id": track_id,
                "report_text": report_text,
                "report_time": report_time,
                "report_date": report_date,
                "report_day": report_day,
            }
            db.reports.insert_one(report)
            now_in_india = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
            report_time_in_india = f"{now_in_india.strftime('%I:%M:%S %p')}"

            # Update the loading message with the filled animation
            for i in range(4):
                filled = "●" * (i + 1)
                unfilled = "○" * (4 - (i + 1))
                loading_bar = f"Report sending {filled}{unfilled}"
                await loading_message.edit_text(loading_bar)
                time.sleep(0.5)

            # Delete the loading message
            await loading_message.delete()

            getting_message = await message.reply(f"{report['report_top']}\n\n👤 Rᴇᴘᴏʀᴛᴇʀ: {report['reporter']}\n🆔 Rᴇᴘᴏʀᴛᴇʀ ɪᴅ: {report['reporter_id']}\n📜 Tʀᴀᴄᴋ ɪᴅ: {report['track_id']}\n\n💬 Rᴇᴘᴏᴛʀ ᴛᴇxᴛ : {report['report_text']}\n\n⌚ Rᴇᴘᴏʀᴛ ᴛɪᴍᴇ: {report_time_in_india}\n🗓️ Rᴇᴘᴏʀᴛ ᴅᴀᴛᴇ: {report['report_date']}\n⛅ Rᴇᴘᴏʀᴛ ᴅᴀʏ: {report['report_day']}")
            channel_id = -1002016338740
            await client.send_message(channel_id, f"Reporter: {report['reporter']}\nReporter ID: {report['reporter_id']}\nTrack ID: {report['track_id']}\nReport Text: {report['report_text']}\nReport Time: {report_time_in_india}\nReport Date: {report['report_date']}\nReport Day: {report['report_day']}")

            await acyncio.sleep(15)
            await getting_message.delete()

    except:
        pass
