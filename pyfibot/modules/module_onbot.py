import requests
import logging

query = "http://heidi.shack:5000/user/online"

log = logging.getLogger('onbot')


def init(bot):
    pass
def command_online(bot, user, channel, args):
    """Query User Suppository"""
    try:
        r = requests.get(query)

        if r.status_code != 200: return bot.say(channel,"server retarded...")
	
        return bot.say(channel, r.content)
    except:
	return bot.say(channel,"server retarded...")
