#!/usr/bin/env python

from os import environ
from sys import argv, exit
from telegram.ext import Updater

if "TELEGRAM_TOKEN" not in environ:
    print("Unknown Token")
    exit(1)

if "TELEGRAM_CHAT_ID" not in environ:
    print("Unknown Chat Identifier")
    exit(2)

if len(argv) != 2:
    print("Unknown Message")
    exit(4)

updater = Updater(token=environ["TELEGRAM_TOKEN"], use_context=True)
updater.bot.send_message(chat_id=environ["TELEGRAM_CHAT_ID"], text=argv[1])
