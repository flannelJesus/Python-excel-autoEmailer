from datetime import datetime
from xlrd import xldate_as_tuple
from xlrd.sheet import Sheet
from property import Property

class PropertyPortfolio:

    def __init__(self, xlSheet):
        """
        :type xlSheet: Sheet
        """
        self.dateMode = xlSheet.book.datemode
        self.properties = self.processSheet(xlSheet)

    def processSheet(self, xlSheet):
        """
        :type xlSheet: Sheet
        """
        headerRow = xlSheet.row(0)
        headers = []
        properties = []
        for cell in headerRow:
            headers.append(cell.value)
        for rowNum in range(1, xlSheet.nrows):
            row = xlSheet.row(rowNum)
            propertyDict = {}
            for i, cell in enumerate(row):
                propertyDict[headers[i]] = self.valueOf(cell)
            properties.append(Property(propertyDict))
        return properties

    def valueOf(self, cell):
        if cell.ctype == 3:
            dateTup = xldate_as_tuple(cell.value, self.dateMode)
            return datetime(dateTup[0], dateTup[1], dateTup[2], dateTup[3],dateTup[4], dateTup[5])
        if cell.ctype == 4:
            # ctype of 4 is boolean
            # int; 1 means TRUE, 0 means FALSE
            return bool(cell.value)
        return cell.value

    def sendEmails(self):
        for property in self.properties:
            property.send_emails()