# -*- coding: utf-8 -*-

from templates import base_template
from Config import fileConfig
import locale
import newEmail

class CreateEmail:

    def __init__(self, property_dict, month_count, email_type, extra_content):
        """
        :type property_dict: dict
        :type month_count: int
        :type email_type: str
        :type extra_content: str
        :return:
        """
        locale.setlocale(locale.LC_ALL, "")
        self.emails = [property_dict[u'YTC Directors Email'],
                       property_dict[u'YTC Managers Email'],
                       property_dict[u'YTC Accounts Email'],
                       property_dict[u'YTC Property Manager']]
        while '' in self.emails:
            self.emails.remove('')
        self.template_args = {
            'month-count':month_count,
            'path-to-file':'file:///' + fileConfig().fileName.replace('/','\\'),
            'email-type':email_type,
            'property-name':property_dict['Name'],
            'address-lines':property_dict['Address Lines'],
            'town':property_dict['Town'],
            'county':property_dict['County'],
            'post-code':property_dict['Post Code'],
            'landlord':property_dict['Landlord'],
            'tenant':property_dict['Tenant'],
            'extra-content':extra_content,
            'purchase-value':'£' + locale.currency(property_dict['Property Purchase Value'],
                                                   grouping=True)[1:],
            'property-size':str(property_dict['Property Size']) + ' sqFt'
        }
        self.html_email = ''
        self.populateTemplate()
        self.plain_text_email = strip_tags(self.html_email).replace(
            ' - click to see Properties','')
        self.subject = property_dict['Name'] + ' : ' + email_type + ' in ' + str(month_count) + \
                       ' months'

    def populateTemplate(self):
        self.html_email = base_template().format(**self.template_args)

    def send(self):
        newEmail.send(self.subject, self.plain_text_email, self.html_email, self.emails)


from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()