from .event import all_classes as events
from .message.message_segment import all_classes as message_segments
from websocket import WebSocket
import json

ws = WebSocket()
ws.connect("ws://127.0.0.1:3002")
while True:
    data = json.loads(ws.recv())
    event = events.Event.factory(data)
    isinstance(event, events.Heartbeat) or print(event)
    if isinstance(event, events.Poke) and event.is_self:
        print(f"在群 {event.group_id} 中被{event.user_id}戳")
    if isinstance(event, events.MessageEvent):
        print(event.message)
    if isinstance(event, events.PrivateMessage):
        print(f"收到来自 {event.sender.nickname}[{event.user_id}] 的消息：{event.raw_message}。其中，各个消息段为：")
        for i in event.message:
            assert i
            print(i.type.value, i)
