#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@BlueEarOtter 2 Jan 2018  -- 151488595

Poof Patroller Bot

Basically Rolls a dice and returns a status
"""

#from uuid import uuid4
from telegram.ext import Updater
from telegram.ext import CommandHandler
import random as rand
from time import sleep
import logging

############
#Parameters#
############
authToken = '545347539:AAHAP2cv7DK6odbSPUrIfoMnh2w6x39XDaw' #a token that lets Python communicate with the bot

##############
#Py Functions#
##############

global Certified_Big
Certified_Big= ["aliothfox","socallioncub","poofpatrollerbot", "bouquetnine","jacarandadeer","saphs"]

def roll():
    """
    prng
    """
    nums=[[i] for i in range(6)]
    rand.shuffle(nums)
    return int(nums[0][0])

def check_pamps(username):
    """
    dictionary that lets us look up statuses and pick one.
    """
    #Roll the dice
    diapercheck = roll()
    
    #Apply the result
    str(username)
    status_dic ={
        0: ["@"+username+" is wet and messy. Bummer, kiddo. Looks like you won't be out of diapers any time soon.",
            "@"+username+" is wet and messy. Somebody change them before they get a bad rash!"],
        1: ["@"+username+" is messy. Oof! That smell is overpowering.",
            "@"+username+" is messy. Looks like potty training isn't going so well."],
        2: ["@"+username+" is soaked! Chance of leaking at 95% if not changed immediately.",
            "Oh no! @"+username+" is about to leak! Someone needs changing pronto!"],
        3: ["@"+username+" is wet, but their diaper can still hold quite a bit more.",
            "@"+username+" is wet. They probably like being in soggy padding or they would have asked for a change by now."],
        4: ["@"+username+" is a little damp. Looks like they're not as big as they think.",
            "@"+username+" is a little damp. Someone didn't quite make it to the potty."],
        5: ["@"+username+" is clean. What a big kid!",
            "@"+username+" is clean. They must have been changed recently.",
            "@"+username+" is clean. They deserve a sticker on their sticker chart."]
        }
    
    status = rand.choice(status_dic[diapercheck])
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
    /check function. Genetrates a random number between 0 and 5, and reports the status of someone's diaper based on the results
    """
    #Read username
    if not args:
        M1 = "Thank you for choosing Poof Patroller Bot for all your diaper checking needs. Please specify a person's diaper to check using the syntax \n\n/check @username."
        bot.send_message(chat_id=update.message.chat_id, text=M1)
        return
    #takes care of the @
    if args[0][0]=="@":
        bab=str(args[0][1::])
    else:
        bab=args[0]
    
    #Checks for certified big
    for bigkid in Certified_Big:
        if bab.lower() == bigkid:
            M1="Thank you for choosing Poof Patroller Bot for all your diaper checking needs.\n\n@"+bab+" is potty trained. You should be put in time out for trying to abuse Poof Patroller Bot."
            bot.send_message(chat_id=update.message.chat_id, text=M1)
            return
    
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
    
    outText = check_pamps(bab)
    #send output to bot
    bot.send_message(chat_id=update.message.chat_id, text=outText)
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

    
    #Tell the dispatcher where to find the handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(check_handler)
    
    #Start the bot
    updater.start_polling()
    
    return

####################
#Main Function Call#
####################

if __name__ == "__main__":
    main(authToken)
