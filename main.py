import xlrd
import Config
from PropertyPortfolio import PropertyPortfolio
from property import Property
import newEmail

fileName = Config.fileConfig().fileName
book = xlrd.open_workbook(fileName)
scheduleSheet = book.sheet_by_name('Schedule')
book.release_resources()
propertyPortfolio = PropertyPortfolio(scheduleSheet)
propertyPortfolio.sendEmails()
#except Exception as e:
#    print('an error has occurred. Michael and Sam have been emailed')
#    toList = ["samuelr@yorkshiretrading.com", "superlistingteam@gmail.com", "michaelnicholsytc@gmail.com"]
#    toList.pop() # take out this line when Michael needs to see emails
#    newEmail.send("Error with leaseEmails script",
#                  "there's been an error with the script\ncall in Sam to debug",
#                  "<p>There's been an error with the script</p>"
#                  "<p>Call in <strong>Sam</strong> to debug</p>"
#                  "<p>${error}".replace('${error}', str(e)),
#                  toList)
