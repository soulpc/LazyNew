from pyrogram import Client, filters

@Client.on_message(filters.group)
def handle_message(client, message):
    if "@admin" in message.text or "@admins" in message.text:
        sender_username = message.from_user.username
        sender_id = message.from_user.id
        group_id = message.chat.id
        track_id = f"#MB{group_id}"
        
        if client.get_chat_member(group_id, sender_id).status == "creator":
            track_id += "1"
        else:
            track_id += "2"
        
        reply_message = f"Report sent successfully\nReporter: {sender_username}\nReporter Id: {sender_id}\nTrack id: {track_id}"
        message.reply_text(reply_message)
