"""This is San Diego Python's chat bot.

It is based on the example "TestBot" from the "irc" Python module

The bot sends welcome messages when people join the channel

The known commands are:

    welcome -- Send a welcome message
    stats -- Prints some channel information.
    dcc -- Let the bot invite you to a DCC CHAT connection.
"""

import logging
import irc.bot
import irc.strings


logger = logging.getLogger('SDPythonBot')


class SanDiegoPythonBot(irc.bot.SingleServerIRCBot):
    MEETUP_PAGE = 'http://www.meetup.com/pythonsd/'

    def __init__(self, server='irc.freenode.net', port=6667):
        self.nick = 'SDPythonBot'
        self.channel = '#sandiegopython'
        self.known_nicks = [irc.strings.lower(self.nick)]
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], self.nick, self.nick)

    def on_nicknameinuse(self, connection, event):
        connection.nick(connection.get_nickname() + "_")

    def on_welcome(self, connection, event):
        connection.join(self.channel)

    def on_privmsg(self, connection, event):
        self.do_command(event, event.arguments[0])

    def on_pubmsg(self, connection, event):
        a = event.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
            self.do_command(event, a[1].strip())
        return

    def on_join(self, connection, event):
        nick = irc.strings.lower(event.source.nick)

        if nick not in self.known_nicks:
            self.do_welcome(connection, nick)

    def do_welcome(self, connection, nick):
        logger.info(u'Sending welcome message to {}'.format(nick))
        connection.privmsg(self.channel, u'{}: Check out our Meetup page for upcoming events: {}'.format(nick, self.MEETUP_PAGE))

    def do_command(self, event, cmd):
        nick = event.source.nick
        c = self.connection
        logger.debug(u'Received command {} from {}'.format(cmd, nick))

        if cmd == "welcome":
            self.do_welcome(c, nick)
        elif cmd.startswith('kick'):
            c.privmsg(self.channel, u"Don't tempt me")
        elif cmd == "import this":
            c.privmsg(self.channel, u"Don't get me started on The Zen of Python. I can talk for days.")
        else:
            c.notice(nick, "Not understood: " + cmd)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='San Diego Python IRC Bot')
    parser.add_argument(
        '--server',
        dest='server',
        default='irc.freenode.net',
        help='Hostname for the IRC server [irc.freenode.net]',
    )
    parser.add_argument(
        '--port',
        dest='port',
        type=int,
        default=6667,
        help='Port for the IRC server [6667]',
    )

    args = parser.parse_args()

    logging.basicConfig(format='[%(asctime)s]: %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    bot = SanDiegoPythonBot(server=args.server, port=args.port)
    bot.start()

if __name__ == "__main__":
    main()
