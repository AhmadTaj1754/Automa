import pyautogui as py
import os, six

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys, pyAesCrypt
import requests, webbrowser, bs4


if six.PY2:
    import Tkinter as tk
    from Tkinter import *

else:
    import tkinter as tk
    from tkinter import *


#window setup
window = Tk()
window.title("Automa")



def getFilePath():
    path = py.prompt(text='Enter path to your file', title='File Path' , default='/base/filepath.(extension)')
    return path


#define buttons

def encryptFile():
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    match=False

    filePathEncrypt = getFilePath()

    while match is False:
        password = py.password(text='Enter password:', title='Password', default='enter password', mask='*')

        passwordConfirm = py.password(text='Confirm password:', title='Password', default='confirm password', mask='*')

        if password == passwordConfirm:
            match =True
        else:
            py.prompt(text='Passwords did not match, please click ok and try enter password again.', title='Password')


    # Encrypt
    pyAesCrypt.encryptFile(filePathEncrypt , filePathEncrypt+".aes" , password, bufferSize)

    os.system('rm ' + filePathEncrypt)

def decryptFile():
    filePathDecrypt = getFilePath()

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    password = py.password(text='Enter password:', title='Google Search', default='enter password', mask='*')

    # get length of file Path
    pathLen = len(filePathDecrypt)

    # get range for string array
    endRange = pathLen - 3

    #get file path without aes extension
    fileWithout, empty =  os.path.splitext(filePathDecrypt)[0:endRange]

    # decrypt
    pyAesCrypt.decryptFile(filePathDecrypt, fileWithout , password,bufferSize)


    os.system('rm ' + filePathDecrypt)

def searchClick():
    searchtext =  py.prompt(text='Enter search topic', title='Search Topic' , default='ex: cars')
    numSearches = py.prompt(text='Enter the number of links to return (up to 10)', title='Number of Searches' , default='ex: 10')

    print('Googling...')    # display text while downloading the Google page
    res = requests.get('http://google.com/search?q=' + searchtext)
    res.raise_for_status()

    #user enters number of pages to open
    numOpen=int(numSearches)


    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text)
    # Open a browser tab for each result.
    linkElems = soup.select('.r a')


    #open the search page
    webbrowser.open('http://google.com/search?q=' + searchtext)

    #open sreach result pages, based on numOpen:number of results requested
    for i in range(min(10,numOpen)):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))



def youClick():
    youtext = py.prompt(text='Enter search topic', title='Search Topic' , default='ex: java tutorial')
    # numSearches = py.prompt(text='Enter the number of links to return (up to 10)', title='Number of Searches' , default='ex: 10')
    # youtube - Opens several youtube search results.

    # print('Youtubing...')    # display text while downloading the Google page
    res = requests.get('https://www.youtube.com/results?search_query=' + youtext)
    res.raise_for_status()

    #user enters number of pages to open
    # numOpen=int(numSearches)


    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text)
    # Open a browser tab for each result.
    linkElems = soup.select('#video-title')


    #open the search page
    webbrowser.open('https://www.youtube.com/results?search_query=' + youtext)

    #open sreach result pages, based on numOpen:number of results requested
    # for i in range(max(10,numOpen)):
    #     webbrowser.open('http://www.youtube.com' + linkElems[i].get('href'))


def imgClick():
    imgtext = py.prompt(text='Enter images to return', title='Image Topic' , default='ex: wild bears')
    # youtube - Opens several youtube search results.

    for i in range(1):
        #create webbroswer object
        browser= webdriver.Firefox()
        #get website
        browser.get('https://www.google.com//search?q='+imgtext+'&client=safari&rls=en&source=lnms&tbm=isch')
        try:
            #get get links with desired text and open in a new tab
            elem=browser.find_elements_by_css_selector('.rg_l')
            print(len(elem))
            print(elem)
            #        for i in range(len)
            for i in range(len(elem)):
                elem[i].send_keys(Keys.COMMAND + Keys.SHIFT + Keys.RETURN)

            time.sleep(5)

               # browser.quit()
        except:
            alert(text='Operation Failed', title='Error', button='OK')

def movies():

    #open the search page
    webbrowser.open('https://www.imdb.com')



def gmailClick():

    # print('\n\n')
    # print('Opening Gmail...\n\n')    # display text while downloading the Google page

    webbrowser.open('https://mail.google.com/mail/u/1/#inbox')


def weather():

    zipcode = py.prompt(text='Enter zipcode for weather', title='Weather' , default='ex: 90210')
    webbrowser.open('https://weather.com/weather/hourbyhour/l/'+zipcode)


#create buttons and input boxes


####Left Side####
searchButton = Button(window, text="Google",width=8, bg='black', fg='green', command=searchClick)
searchButton.grid(column= 0, row= 0, padx=(1, 1), pady=(1,1))

youButton = Button(window, text="Youtube",width=8, bg='black', fg='green', command=youClick)
youButton.grid(column= 0, row= 1, padx=(1, 1), pady=(1,1))

imgButton = Button(window, text="Image",width=8, bg='black', fg='green', command=imgClick)
imgButton.grid(column= 0, row= 2, padx=(1, 1), pady=(1,1))

desktopEncryptButton = Button(window, text='Encrypt', width=8, bg='black', fg='green', command=encryptFile)
desktopEncryptButton.grid(column= 0, row= 3, padx=(1, 1), pady=(1,1))


####Right Side####
movies = Button(window, text="Movies",width=8, bg='black', fg='green', command=movies)
movies.grid(column= 1, row= 0, padx=(1, 1), pady=(1,1))

gmailButton = Button(window, text="Gmail",width=8, bg='black', fg='green', command=gmailClick)
gmailButton.grid(column= 1, row= 1, padx=(1, 1), pady=(1,1))

weatherButton = Button(window, text="Weather", width=8, bg='black', fg='green', command=weather)
weatherButton.grid(column= 1, row= 2, padx=(1, 1), pady=(1,1))

desktopDecryptButton = Button(window, text="Decrypt", width=8, bg='black', fg='green', command=decryptFile)
desktopDecryptButton.grid(column= 1, row= 3, padx=(1, 1), pady=(1,1))


#create gui

window.mainloop()
































#end
