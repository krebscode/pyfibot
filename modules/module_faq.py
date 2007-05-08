import os
import os.path
import sys
import re

# this should be faster than string.startswith
#faqregex = re.compile(r'^\?\?') # matches strings starting with ??
faqignore = re.compile(r'(^[^\.])') # everything starting with a dot

def handle_privmsg(bot, user, channel, args):
    """Usage: ?? <searchterm>"""

    if args.startswith("??"):
        bot.log("Command faq called by %s" % user)
        faqdir = os.path.join(sys.path[0], "faq", channel.replace("#", ""))

        if not os.path.exists(faqdir): return

	# skip the ?? -triggger, strip spaces from start & end, replace the rest with underscores
        args = args[2:].strip() #.replace(" ", "_")

        if not args: return

	faqs = os.listdir(faqdir)
        faqs = filter(faqignore.match, faqs)
        faqs = map(lambda x: x.replace("_", " "), faqs)
        if args in faqs:
            f = file(os.path.join(faqdir, args.replace(" ", "_")))
            value = f.read()
            f.close()

            bot.say(channel, value)
            
	else:
            if args=="index":
                faqs.sort()
                bot.say(channel, "FAQs for this channel: " + ", ".join(faqs))
	    else:
		bot.say(channel, "FAQ term '%s' not specified for this channel" % args)

