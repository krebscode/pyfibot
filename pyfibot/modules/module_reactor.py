import requests
import logging
import yaml
import os
import sys
log = logging.getLogger('reactorbot')
from twisted.internet import protocol, reactor
mybot=None
onconfig=None
echoport = None
def init(bot):
    global mybot
    global onconfig
    class Echo(protocol.Protocol):
        def dataReceived(self, data):
            if mybot is None: raise Exception("Bot is not ready yet!")
            mybot.say(onconfig["channel"],data)

    class EchoFactory(protocol.Factory):
        def buildProtocol(self, addr):
            return Echo()

    configfile = os.path.join(sys.path[0], 'modules', 'module_reactor.conf')
    onconfig = yaml.load(file(configfile))

    echoport = reactor.listenTCP(1234, EchoFactory(),interface='127.0.0.1')

def finalize():
    global echoport
    echoport.stopListening()

def handle_joined(bot,channel):
    global mybot
    bot.say(channel,"This is the onbot, i will tell you when a user logged in or out")
    bot.log("I just joined %s" %channel)
    mybot=bot
