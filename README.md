# PoofPatrollerBot
Repository for @PoofPatrollerBot on Telegram

# Version History
- v0.2.1
  - Fixed a spelling error
  - PoofPatrollerBot added to "Certified Big" list
- v0.2.0
  - Introduction of "Certified Big" list
  - More responses to each status added

- v0.1
  - Allows users to check diapers
  - has 6 available statuses and 1 response per status

# Under The Hood
This work uses the [Telegram Bot API](https://core.telegram.org/bots/api), and the [python-telegram package](https://github.com/python-telegram-bot/python-telegram-bot). The basic command is /check, which has they syntax:
  ```
  /check @username
  ```
The code works to generate a pseudo random number between 1 and 6 (basically rolling a die), and then assigning a status based on that number. Based on this status, it picks a response from a list of possible corresponding responses and reports it back to the user.

As of v0.2 there is a "Certified Big" mechanic which can acts as an opt-out for people who do not wish to be checked. In future versions this list will be able to be edited dynamically, but that is currently under development. 

# Google Form
Want to submit your own response for the bot to see if it might make it into the next iteration? Please use our [google form](https://goo.gl/forms/f797W0ylSL8cboyc2)

# Production Credits
## Design:
Lead Designer
- twitter user @smolyote1

Additional Input
- Krev
- Jimmy
## Programming:
Lead Programmer
- twitter user @diaperace

Assistant Programmers
- Krev
# Special Thanks
## Testers:
Thanks to the SoCalCubChat for field testing. You guys rock.
## Submissions to Google Form
