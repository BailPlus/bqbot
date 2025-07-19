#bqbot:event.all_classes 所有事件类

from . import Event
from .message import MessageEvent
from .message.group import GroupMessage
from .message.private import PrivateMessage
from .meta import MetaEvent
from .meta.lifecycle import Lifecycle
from .meta.heartbeat import Heartbeat
from .notice import Notice
from .notice.friend_add import FriendAdd
from .notice.friend_recall import FriendRecall
from .notice.group_admin import GroupAdmin
from .notice.group_ban import GroupBan
from .notice.group_decrease import GroupDecrease
from .notice.group_increase import GroupIncrease
from .notice.group_recall import GroupRecall
from .notice.group_upload import GroupUpload
from .notice.notify import BaseNotify
from .notice.notify.honor import Honor
from .notice.notify.lucky_king import LuckyKing
from .notice.notify.poke import Poke
from .request import Request
from .request.friend import FriendRequest
from .request.group import GroupRequest
