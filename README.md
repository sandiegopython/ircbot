# San Diego Python's IRC Bot

This is a bot built to idle in #sandiegopython on freenode.


## Functionality

The bot doesn't do much right now. It welcomes people who come to the channel,
informs them about our upcoming events and reminds them of our code of conduct.

It responds to a few commands but you'll have to check the source for that.


## Starting the bot

Assuming you have the requirements (`requirements.txt`) installed:

    % python sandiegopythonbot.py

This will run the bot forever until you hit `ctrl+C`.


### Running the bot from a server

The bot is intended to idle in a channel so it is typically run from a server.
The following command will run the bot and persist the bot process even
after the user's ssh session to the server ends:

    % nohup python sandiegopythonbot.py > /dev/null 2>&1 &

To stop the bot:

    % killall sandiegopythonbot.py


##  License

The MIT License (MIT)

Copyright (c) 2015 David Fischer and other contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
