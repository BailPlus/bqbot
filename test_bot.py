from typing import override
from websocket import WebSocket
from .event.message.group import GroupMessage
from .bot import Bot as _Bot
from .onebot11.adapter.ws import WsConnection


class Bot(_Bot):
    @override
    def on_group_message(self, message: GroupMessage):
        print(f'┌{message.sender.nickname}[{message.sender.user_id}]')
        print(f'├{message.group_id}')
        print(f'└{message.raw_message}')

    @override
    def on_exit(self):
        print('exiting')
    

if __name__ == '__main__':
    ws = WebSocket()
    ws.connect('ws://127.0.0.1:3002')
    bot = Bot(WsConnection(ws))
    bot.run()
