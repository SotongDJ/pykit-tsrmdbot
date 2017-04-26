import tool, json

def chstr(a,b,c,d): # if a == b, return c; else return d
    if a == b :
        return c
    else:
        return d

def warn():
    final = "This chatbot is under constructing..."
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.start())
"""
def start():
    final="""  Welcome
----------------------------

This is Money Money Come Chatbot.
It can help you to trace your money flow moreeasily (Sure? )

Pls setup before using:
  Account setup = /set_Account
  Currency setup = /set_Currency
----------------------------
  /help  /Setting
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.help())
"""
def help():
    final="""  Help
----------------------------
  /start
    Welcome Card
  /help
    Command List Card
  /New
    Creating  Card
  /List
    Record Showing Card
  /Setting
    Setting Card
  /Whats_Now
    Check current work status
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.setting())
"""
def setting(): # will replace by Start Card after finished Account Card and Currency Card
    final="""Setting Card
----------------------------
Account Setting:
  /set_Account
Currency Setting:
  /set_Currency
----------------------------
P.S. You still can use the last card
  /Whats_Now
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outo(self._temra))
            self._temra = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
            keywo = ""
"""
def outo(dicto):
    final="""New Record
----------------------------

Date: """+dicto["datte"]+"""
Product: """+dicto["namma"]+"""
Class: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["karen"]+" "+dicto["price"]+"""
    ( /change_Currency )
Spent from which Account:
"""+chstr(dicto["fromm"],"","    ( /choose_Acc_From )",dicto["fromm"]+"\n    ( /choose_Acc_From )")+"""
Notes:
"""+dicto["desci"]+"""

----------------------------
  /Discard  /Save  /List  /Setting
----------------------------
P.S. Give me a word or a number
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outoKeywo(self._temra,keywo))
            self._temra = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
            keywo = ""
"""
def outoKeywo(keywo):
    final="""Filling the blank
----------------------------

Keyword:
  """+keywo+"""

  /set_as_Date (format: yyyy-mm-dd)
  /set_as_Product
  /set_as_Class
  /set_as_Seller
  /set_as_Price
  /set_as_Notes

----------------------------
  /Discard  /Save  /List  /Setting
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outoConti(self._temra))
            self._temra = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
"""
def outoFinis(dicto):
    final="""New Record Saved
----------------------------

Date: """+dicto["datte"]+"""
Product: """+dicto["namma"]+"""
Class: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["price"]+" "+dicto["karen"]+"""
    ( /change_Currency )
Notes:
"""+dicto["desci"]+"""

----------------------------
Spent from which Account:
"""+dicto["fromm"]+"""
Transfer to which Account:
"""+dicto["toooo"]+"""
----------------------------
  /Edit  /List  /Setting
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outoDiscard())
"""
def outoDiscard():
    final="""¡ Discard !
----------------------------

  Closed Creating Card

----------------------------
  /Setting  /help
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.lisFilte(self._temra))


"""
def lisFilte(dicto):
    final="""Filtering Card
----------------------------
Date range:"""+dicto["datte"]+"""
  /Today /This_Week
  /This_Month /This_Year

----------------------------
  /Discard  /Sumit  /Setting
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.lisDiscard())
"""
def lisDiscard():
    final="""¡ Discard !
----------------------------

  Closed Listing Card

----------------------------
  /Whats_Now  /Setting
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.home(self._keywo))
            self._keywo=""
"""
def home(keywo): # will replace by Start Card after finished Account Card and Currency Card
    final="""Home Card (Temporary)
----------------------------

    Welcome Home !

Keyword: """+keywo+"""
  /New  /List
----------------------------
  /Setting  /help
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.timesout())
"""
def timesout(): # will replace by Start Card after finished Account Card and Currency Card
    final="""Time's Out
----------------------------
Previous unsave work was clean out.
"""
    return final

def error():
    final=""""Status:
Received wrong message
Input:
    Undetactable content type
"""
    return final
