import xlrd
import newEmail

filename = '//Sbs2011/JCNDATA/ECOMM/leaseEmails.xlsx'


book = xlrd.open_workbook(filename)
sheet1=book.sheet_by_name('Sheet1')
book.release_resources()
toList = ["samuelr@yorkshiretrading.com", "superlistingteam@gmail.com"]
newEmail.send("Test Message", "another new message\nyesyesyes", toList)
