# -*- coding: utf-8 -*-

import datetime
from propertyEmails import CreateEmail
import locale


class Property:
    def __init__(self, prop_dict):
        self.attributes = prop_dict


    def send_emails(self):
        self.send_lease_end_email()
        self.send_rent_review_email()
        self.send_break_clause_email()

    def send_lease_end_email(self):
        leaseEnd = self.attributes[u'Lease End Date']
        leaseEndEarliestAlert = self.attributes[u'Lease End Earliest Alert']
        if need_email(leaseEnd, leaseEndEarliestAlert) and not (
        self.attributes[u'Lease End Acknowledged']):
            email = CreateEmail(self.attributes, monthsUntil(leaseEnd), 'Lease End', '')
            email.send()

    def send_rent_review_email(self):
        reviewDates = [self.attributes[u'1st Review Date'], self.attributes[u'2nd Review Date'],
                       self.attributes[u'3rd Review Date'], self.attributes[u'4th Review Date'], '']
        # empty string in above list in case all 4 have been acknowledged
        outcomes = [self.attributes[u'1st Review Outcome/ Acknowledged'],
                    self.attributes[u'2nd Review Outcome/ Acknowledged'],
                    self.attributes[u'3rd Review Outcome/ Acknowledged'],
                    self.attributes[u'4th Review Outcome/ Acknowledged']]
        numDone = outcomes.index('')
        nextReview = reviewDates[numDone]
        earliestAlert = self.attributes[u'Rent Review Earliest Alert']
        if need_email(nextReview, earliestAlert):
            if numDone > 0:
                currentRent = outcomes[numDone - 1]
            else:
                currentRent = self.attributes['Initial Rent']
            locale.setlocale(locale.LC_ALL, "")
            extraContent = 'Current Rent: £' + \
                           locale.currency(currentRent, grouping=True)[1:] + '<br>'
            email = CreateEmail(self.attributes, monthsUntil(nextReview), 'Rent Review',
                                extraContent)
            email.send()

    def send_break_clause_email(self):
        breakDate = self.attributes[u'Break Date']
        earliestAlert = self.attributes[u'Break Clause Earliest Alert']
        if need_email(breakDate, earliestAlert) and \
                not (self.attributes[u'Break Outcome/ Acknowledged']):
            email = CreateEmail(self.attributes, monthsUntil(breakDate), 'Break Clause', '')
            email.send()


def need_email(date_next_due, max_months_before):
    if not (date_next_due):
        return False
    if not (max_months_before):
        max_months_before = 6
    max_days_before = max_months_before * 30
    today = datetime.datetime.now()
    daysUntilDue = (date_next_due - today).days
    if (daysUntilDue % 30 == 0 and daysUntilDue <= max_days_before):
        return True
    return False


def monthsUntil(date):
    today = datetime.datetime.now()
    daysUntil = (date - today).days
    return daysUntil / 30