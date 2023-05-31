import random as ran
import helpers.log
import wikipedia


user_search = input("Which page would you like to see: ")
try:
    user_page = wikipedia.page(user_search)
    print(user_page.title)
    print(user_page.content)
except IndexError:
    print("Sorry, that page does not exist")
except wikipedia.exceptions.PageError:
    print("Sorry, that page does not exist")
except:
    print("Something went wrong. Sorry,")


my_num = ran.randint(0,100)
if(my_num >= 50):
    print("Winner")
else:
    print("Loser")


helpers.log.log("What will this do?")
helpers.log.log("Oh, that's neat")
helpers.log.log("Test.")

