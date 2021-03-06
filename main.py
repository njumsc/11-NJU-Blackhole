import itchat
from itchat.content import TEXT, PICTURE
import conversation
from user import User

conversation_map = conversation.ConversationMap()


def get_conversation(msg):
    return conversation_map.update(User(msg.user, msg.fromUserName.replace("@", "")))


@itchat.msg_register(TEXT)
def text_main(msg):
    conv = get_conversation(msg)
    conv.sender.send_text(msg.text)


@itchat.msg_register(PICTURE)
def picture_main(msg):
    conv = get_conversation(msg)
    conv.sender.send_picture(msg)


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
