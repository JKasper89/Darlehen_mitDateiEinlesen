#!/usr/local/bin/python
# coding: utf-8

"""
program: determine the annuity
author: Jan Kasper
"""

from decimal import *
import locale
import time
import math
locale.setlocale(locale.LC_ALL, 'german')

def greeting(name,date):
    __infoWidth__ = 80
    __version__ = '0.2'
    __author__ = name

    x = ''.center(80, '*') + "\n" + (' '*76).center(80, '*') + "\n" + \
        'Annuitätisches Darlehen'.center(76, ' ').center(80, '*') \
        + "\n" + (__version__ + ' vom ' + (date)).center(76, ' ').center(80, '*') \
        + "\n" + 'Fehler bitte an jan.kasper@students.tbs1.de'.center(76, ' ').center(80, '*') \
        + "\n" + (' '*76).center(80, '*')+"\n"+''.center(80, '*')
    print(x)

""" version info and greeting"""
"""__infoWidth__ = 80
__version__ = '0.2'
__author__ = 'Jan Kasper'

x = ''.center(80, '*') + "\n" + (' '*76).center(80, '*') + "\n" + \
    'Annuitätisches Darlehen'.center(76, ' ').center(80, '*') \
    + "\n" + (__version__ + ' vom ' + (time.strftime("%d.%m.%y"))).center(76, ' ').center(80, '*') \
    + "\n" + 'Fehler bitte an jankasper@students.tbs1.de'.center(76, ' ').center(80, '*') \
    + "\n" + (' '*76).center(80, '*')+"\n"+''.center(80, '*')
print(x)"""

def checkInput(iloanAmount,irateOfInterest,irunTime):
    "inputs & check"
    while True:
        try:
            loanAmount = iloanAmount
            loanAmount = Decimal(loanAmount)
            if loanAmount <= 0:
                raise ValueError
            break
        except InvalidOperation:
            print("Achtung! Bitte geben Sie eine Zahl ein!")
        except ValueError:
            print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")
    while True:
        try:
            rateOfInterest = irateOfInterest
            rateOfInterest = Decimal(rateOfInterest) * Decimal(0.01)
            if rateOfInterest <= 0:
                raise ValueError
            break
        except InvalidOperation:
            print("Achtung! Bitte geben Sie eine Zahl ein!")
        except ValueError:
            print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")
    while True:
        try:
            runTime = irunTime
            runTime = Decimal(runTime)
            if runTime <= 0:
                raise ValueError
            break
        except InvalidOperation:
            print("Achtung! Bitte geben Sie eine Zahl ein!")
        except ValueError:
            print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")
    return [loanAmount,rateOfInterest,runTime]

def determineAnnuity(loanAmount,rateOfInterest,runTime):
    """determine the annuity"""
    annuity = Decimal(loanAmount*(((1+rateOfInterest)**runTime)*rateOfInterest/(((1+rateOfInterest)**runTime)-1)))
    sumOfInterest = Decimal((annuity*runTime)-loanAmount)
    print("Die jährliche Annuität beträgt: " + locale.currency(annuity,True,True,True))
    print("Die Gesamtzinsen betragen: " + locale.currency(sumOfInterest,True,True,True))

    """Berechnung der Jahreswerte"""

    partInterestYear1 = loanAmount * rateOfInterest
    partRepaymentYear1 = annuity - partInterestYear1
    print(''.center(80, '*'))
    print("Anteile im Jahr: 1")
    print("Zinsanteil im Jahr 1: " + locale.currency(partInterestYear1, True, True, True))
    print("Tilgunsanteil im Jahr 1: " + locale.currency(partRepaymentYear1, True, True, True))
    tempYear = 2
    while tempYear <= math.ceil(runTime):
        partRepaymentYear = partRepaymentYear1 * (1 + rateOfInterest) ** (tempYear - 1)
        partInterestYear = annuity - partRepaymentYear
        print(''.center(80, '*'))
        print("Anteile im Jahr: " + str(tempYear))
        print("Zinsanteil im Jahr " + str(tempYear) + ": " + locale.currency(partInterestYear, True, True, True))
        print("Tilgunsanteil im Jahr " + str(tempYear) + ": " + locale.currency(partRepaymentYear, True, True, True))
        tempYear += 1

    print(''.center(80, '*'))

def readFile(path):


while True:

    "inputs & check"
    """while True:
        try:
            loanAmount = input("Bitte geben Sie den Darlehensbetrag in Euro ein:")
            loanAmount = Decimal(loanAmount)
            if loanAmount <= 0:
                raise ValueError
            break
        except InvalidOperation:
            print("Achtung! Bitte geben Sie eine Zahl ein!")
        except ValueError:
            print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")
    while True:
        try:
            rateOfInterest = input("Bitte geben Sie den Zinssatz in Prozent ein:")
            rateOfInterest = Decimal(rateOfInterest) * Decimal(0.01)
            if rateOfInterest <= 0:
                raise ValueError
            break
        except InvalidOperation:
            print("Achtung! Bitte geben Sie eine Zahl ein!")
        except ValueError:
            print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")
    while True:
        try:
            runTime = input("Bitte geben Sie die Laufzeit in Jahren ein:")
            runTime = Decimal(runTime)
            if runTime <= 0:
                raise ValueError
            break
        except InvalidOperation:
            print("Achtung! Bitte geben Sie eine Zahl ein!")
        except ValueError:
            print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")"""

    """determine the annuity"""
    """annuity = Decimal(loanAmount*(((1+rateOfInterest)**runTime)*rateOfInterest/(((1+rateOfInterest)**runTime)-1)))
    sumOfInterest = Decimal((annuity*runTime)-loanAmount)
    print("Die jährliche Annuität beträgt: " + locale.currency(annuity,True,True,True))
    print("Die Gesamtzinsen betragen: " + locale.currency(sumOfInterest,True,True,True))

    """"""Berechnung der Jahreswerte""""""

    partInterestYear1 = loanAmount * rateOfInterest
    partRepaymentYear1 = annuity - partInterestYear1
    print(''.center(80, '*'))
    print("Anteile im Jahr: 1")
    print("Zinsanteil im Jahr 1: " + locale.currency(partInterestYear1, True, True, True))
    print("Tilgunsanteil im Jahr 1: " + locale.currency(partRepaymentYear1, True, True, True))
    tempYear = 2
    while tempYear <= math.ceil(runTime):
        partRepaymentYear = partRepaymentYear1 * (1 + rateOfInterest) ** (tempYear - 1)
        partInterestYear = annuity - partRepaymentYear
        print(''.center(80, '*'))
        print("Anteile im Jahr: " + str(tempYear))
        print("Zinsanteil im Jahr " + str(tempYear) + ": " + locale.currency(partInterestYear, True, True, True))
        print("Tilgunsanteil im Jahr " + str(tempYear) + ": " + locale.currency(partRepaymentYear, True, True, True))
        tempYear += 1

    print(''.center(80, '*'))
    print("Die Berechnung ist fertig!")
    print(''.center(80, '*'))"""




    """new run?"""
    newRun = False
    while True:
        try:
            choose = input("Möchten Sie ein neues Darlehen berechnen?(y/n)")
            if choose == "n":
                break
            elif choose == "y":
                newRun = True
                break
            else:
                raise ValueError
        except ValueError:
            print("Bitte wählen Sie eine Entscheidung! y=Ja, n=Nein")

    if newRun is False:
        break
print("Das Programm beendet sich!")

"""start"""
greeting('Jan Kasper',time.strftime("%d.%m.%y"))





