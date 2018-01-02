#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@BlueEarOtter 2 Jan 2018  -- 151488595

Poof Patroller Bot

Basically Rolls a dice and 
"""

from uuid import uuid4
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import random as rand
from time import sleep
import logging

############
#Parameters#
############
authToken = 'TOKEN_GOES_HERE' #a token that lets Python communicate with the bot

##############
#Py Functions#
##############

def roll():
    nums=[[i] for i in range(6)]
    rand.shuffle(nums)
    return nums[0][0]

def check_pamps():
    #Roll the dice
    diapercheck = roll()
    
    #Apply the result
    if diapercheck == 0:
        status = " is wet and messy. Bummer, kiddo. Looks like you won't be out of those diapers any time soon."
    elif diapercheck == 1:
        status = " is messy. Oof! That smell is overpowering."
    elif diapercheck == 2:
        status = " is soaked! Chance of leaking at 95% if not changed immediately."
    elif diapercheck == 3:
        status = " is wet, but their diaper can still hold quite a bit more."
    elif diapercheck == 4:
        status = " is a little damp. Looks like they're not as big as they think"
    elif diapercheck == 5:
        status = " is clean. What a big kid!"
    return status

#############
# /functions#
#############

def start(bot, update):
    """
    /start fucntion
    Message that greets users when they first launch the bot.
        -indicates what the /check command does
    """
    #Write welcome message
    welcomeText = "Thank you for choosing Poof Patroller Bot for all your diaper checking needs. Please use /check @username to check the status of someone's padding"
    #Send welcome message to bot
    bot.send_message(chat_id=update.message.chat_id,text=welcomeText)
    return

def check(bot, update,args):
    """
    /check function. Genetrates a random number between 1 and 6, and reports the status of someone's diaper based on the results
    """
    #Read username
    if not args:
        M1 = "Thank you for choosing Poof Patroller Bot for all your diaper checking needs. Please specify a person's diaper to check using the syntax \n\n/check @username."
        bot.send_message(chat_id=update.message.chat_id, text=M1)
        return
    if args[0][0]=="@":
        bab=str(args[0][1::])
    else:
        bab=args[0]
    
    #write output strings for greeting
    
    M1 = "Thank you for choosing Poof Patroller Bot for all your diaper checking needs. Please hold while I check the status of @"+bab+"'s diaper."
    bot.send_message(chat_id=update.message.chat_id, text=M1)
    sleep(2) #pause for effect
    
    M2 = "Tugging on the back of @"+bab+"'s diaper..."
    bot.send_message(chat_id=update.message.chat_id, text=M2)
    sleep(1.5)#etc
    
    M3 = "Checking @"+bab+"'s leg cuff for sogginess..."
    bot.send_message(chat_id=update.message.chat_id, text=M3)
    sleep(2)#etc
    
    status = check_pamps()
    
    outText = "@" + bab + status
    #send output to bot
    bot.send_message(chat_id=update.message.chat_id, text=outText)
    return


def inline_check(bot, update):
    '''Handle the inline query.'''
    bab = update.inline_query.query
    M1 = "Thank you for choosing Poof Patroller Bot for all your diaper checking needs. Please hold while I check the status of @"+bab+"'s diaper."
    results = [
        InlineQueryResultArticle(
        id=uuid4(),
        title="Greeting 1",
        input_message_content=InputTextMessageContent(M1))]
    update.inline_query.answer(results)
    
    M2 = "Tugging on the back of @"+bab+"'s diaper..."
    sleep(2) #pause for effect
    results = [
        InlineQueryResultArticle(
        id=uuid4(),
        title="Greeting 2",
        input_message_content=InputTextMessageContent(M2))]
    update.inline_query.answer(results)
    sleep(1.5) #pause for effect
    
    M3 = "Checking @"+bab+"'s leg cuff for sogginess..."
    results = [
        InlineQueryResultArticle(
        id=uuid4(),
        title="Greeting 3",
        input_message_content=InputTextMessageContent(M3))]
    update.inline_query.answer(results)
    sleep(2) #pause for effect
    
    status = check_pamps()
    outText = "@" + bab + status
    
    results = [
        InlineQueryResultArticle(
        id=uuid4(),
        title="Check",
        input_message_content=InputTextMessageContent(outText))]
    update.inline_query.answer(results)
    
    return
        

######
#Main#
######

def main(Token):
    #Create an update/dispatch channel to communicate with bot
    updater = Updater(token=Token)
    dispatcher = updater.dispatcher
    
    #Create a log file
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    #Define the start and roll handlers
    start_handler = CommandHandler('start', start)
    check_handler = CommandHandler('check', check, pass_args=True)
    #inline_check_handler = InlineQueryHandler(inline_check)

    
    #Tell the dispatcher where to find the handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(check_handler)
    #dispatcher.add_handler(inline_check_handler)
    
    #Start the bot
    updater.start_polling()
    
    return

####################
#Main Function Call#
####################

if __name__ == "__main__":
    main(authToken)
