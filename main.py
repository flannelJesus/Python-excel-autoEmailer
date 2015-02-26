import xlrd
import Config
from PropertyPortfolio import PropertyPortfolio
from property import Property
import newEmail

try:
    fileName = Config.fileConfig().fileName
    book = xlrd.open_workbook(fileName)
    scheduleSheet = book.sheet_by_name('Schedule')
    book.release_resources()
    propertyPortfolio = PropertyPortfolio(scheduleSheet)
    propertyPortfolio.sendEmails()
except:
    newEmail.send('Error in lease email script',
                  'Check out the error',
                  '<p>Check out the error</p>',
                  ['samuelr@yorkshiretrading.com'])