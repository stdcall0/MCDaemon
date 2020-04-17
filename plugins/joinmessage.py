"""
MCDaemonReloaded 进服插件
用于广播进服信息。
"""
from event import TRIGGER
from textapi import CC
from plugins.daycount import getday

def onjoin(ev, server, plugin):
  server.tell(ev["sender"], CC("=======", "7"), CC(" 欢迎回到","r"),CC(" HTS","e"),CC(" =======", "7"))
  server.tell(ev["sender"], CC("今天是"), CC(" HTS ","e"),CC("开服的第","r"),CC(getday(),"e"),CC("天","r"))
  server.tell(ev["sender"], CC("-------","7"),CC(" 祝您爆肝愉快 xD ","r"),CC("-------","7"))
  server.tell(ev["sender"], CC("!!bot, !!ib, !!loc, !!here, !!self 啥的都可以用了，enjoy！"))

listener = [
  {"type": TRIGGER.PLAYER_JOIN, "func": onjoin}
]
name = "JoinMessagePlugin"
