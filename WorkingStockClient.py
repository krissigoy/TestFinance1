import logging
import random
import socket
from threading import Thread
import threading
import time


PORT=38814
BUFF=1024
FALSE=0
TXTIMEOUT=1

log = logging.getLogger(__name__)

class ClientCommService():
    def __init__(self, clientId):
        self.active = False
        self.clientId = clientId
        self.connected = False
        self.sock = None

    def initCommClient(self, address, replyHandler):
        functionName = self.initCommClient.__name__
     #       helpers.entrylog(log, functionName, level=logging.INFO)

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.settimeout(TXTIMEOUT)

        retries = 0
        while not self.connected:
            log.info("Trying to connect to server, attempt #%d..." % (retries+1))
            try:
                self.sock.connect((address, PORT))
                self.connected = True
                log.info("Connected to server")
            except socket.error as e:
                retries += 1
                log.info("Socket timed out, exception: %s" % repr(e))
                time.sleep(0.1 + (random.random()*0.3))

        data = {'src': self.clientId}
        self.sock.send(str(data))

        self.active = True
        thread = Thread(name="ClientHandler for " + self.clientId, target=self.ClientHandler, args=(replyHandler,))

    	#setting to daemon so all the clients die when the main thread is dead
        thread.daemon = True
        thread.start()

      #      helpers.exitlog(log, functionName, level=logging.INFO)
        return thread

    def ClientHandler(self, replyHandler):

        t = threading.currentThread()
        log.info("Running %s"  % t.name)

        while self.active:
                #blocks on recv, but may timeout
            try:
                rxdata = self.sock.recv(BUFF)
                log.debug("Data Received: %s" %(repr(rxdata)))
            except socket.timeout:
                continue

            try:
                data = rxdata.strip()
            except:
                log.info("ClientHandler could not parse JSON string: %s" % repr(rxdata))
                continue
            print t
            log.debug('Client RX jdata: %s'  %(repr(data)))

        if data == '':
            print "server disconnected"
            self.active = False
    	else:
            replyHandler(data)

            #cleanup
        self.sock.close()
        log.info("Leaving %s" % threading.currentThread().name)

    def sendData(self, data):

        tmp = eval(data)
        tmp['src'] = self.clientId
        data = str(tmp)

        log.debug('Sending data %s' %(data))
        self.sock.send(data)

    def stop(self):
        self.active = False

def echoHello(message):
    print "message received"


if __name__ == "__main__":

    #arguments/options get clientId

    import sys,getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:')
    except getopt.GetoptError as err:
        print (str(err))
        print ("Arguments missing or invalid, indicate client id")
        sys.exit(2)


    clientId = ''


    for opt, arg in opts:
        if opt == 'id =':
            clientId = arg





    client = ClientCommService(clientId)
    client.initCommClient('localhost', echoHello)
    #dic = {'src' : clientId, 'stockName' : 'Apple', 'date' : '2016/1/1', 'shareCount' : '10'}

    #client.sendData(str(dic))

    #  Example code snippet: sending multiple messages from the same client
    #i = 0
    #while i < 10:
	#dic = {'src' : client.clientId, 'message': i}
	#client.sendData(str(dic))
	#sleep to avoid message concatination on the server
	#time.sleep(2);
	#i = i + 1

    numApple = 9999
    numTesla = 9999
    numAmazon = 9999
    numGoogle = 9999
    numNetflix = 9999
    numFacebook = 9999
    numMicrosoft = 9999

    while 1:
        question = input("Would you like to buy more stocks? 1==yes | 2==no: ")
        question1 = int(question)

        if question == 1:

            stockNum = raw_input("Enter your preffered stock. 1=Apple, 2=Amazon, 3=Google, 4=Netflix, 5=Facebook, 6=Microsoft, 7=Tesla: ")
            date = raw_input("To search up the stock price, enter today's date in mm/dd/yy format: \n")
            datetemp = " "
            price = 0
            stockNameActual = ""
            transHistory1 = open('TRANSACTION_HISTORY', 'r')
            dates = open('dates.txt', 'r' )
            apple = open('apple.txt', 'r' )
            amazon = open('amazon.txt', 'r' )
            google = open('google.txt', 'r' )
            netflix = open('netflix.txt', 'r' )
            facebook = open('facebook.txt', 'r' )
            microsoft = open('microsoft.txt', 'r' )
            tesla = open('tesla.txt', 'r' )
            counter = 0
            priceCounter = 0
            stockName = ""
            stockResult = ""

            month = date[:2]
            day = date[3:5]
            monthNumber = int(month)
            dayNumber = int(day)

            if monthNumber == 1:
                lineNumber = dayNumber - 3
            elif monthNumber == 2:
                lineNumber = dayNumber + 28
            elif monthNumber == 3:
                lineNumber = dayNumber + 57
            elif monthNumber == 4:
                lineNumber = dayNumber + 88
            elif monthNumber == 5:
                lineNumber = dayNumber + 118
            elif monthNumber == 6:
                lineNumber = dayNumber + 149
            elif monthNumber == 7:
                lineNumber = dayNumber + 179
            elif monthNumber == 8:
                lineNumber = dayNumber + 210
            elif monthNumber == 9:
                lineNumber = dayNumber + 241
            elif monthNumber == 10:
                lineNumber = dayNumber + 271
            elif monthNumber == 11:
                lineNumber = dayNumber + 302
            elif monthNumber == 12:
                lineNumber = dayNumber + 332
            else:
                lineNumber = (monthNumber-1) * 30 + dayNumber - 8
                lineNumber = int(lineNumber)

            lineNumber1 = str(lineNumber)

            stockNum = int(stockNum)

            if stockNum == 1:
                stockName = "Apple"
                for line in apple:
                    if priceCounter == lineNumber - 1:
                        price = line
                        priceCounter = priceCounter + 1
            elif stockNum == 2:
                stockName = "Amazon"
                for line in amazon:
                    if priceCounter == lineNumber - 1:
                        price = line
                        priceCounter = priceCounter + 1
            elif stockNum == 3:
                stockName = "Google"
                for line in google:
                    if priceCounter == lineNumber - 1:
                        price = line
                        priceCounter = priceCounter + 1
            elif stockNum == 4:
                stockName = "Netflix"
                for line in netflix:
                    if priceCounter == lineNumber - 1:
                        price = line
                        priceCounter = priceCounter + 1
            elif stockNum == 5:
                stockName = "Facebook"
                for line in facebook:
                    if priceCounter == lineNumber - 1:
                        price = line
                        priceCounter = priceCounter + 1
            elif stockNum == 6:
                stockName = "Microsoft"
                for line in microsoft:
                    if priceCounter == lineNumber - 1:
                        price = line
                        priceCounter = priceCounter + 1
            elif stockNum == 7:
                stockName = "Tesla"
                for line in tesla:
                    if priceCounter == lineNumber - 1:
                        price = line
                        priceCounter = priceCounter + 1
            else:
                stockName = "NA"
                print "Please enter a number from 1-7"

            stockName1 = str(stockName)
            print "Selected stock is " + stockName1


            date1 = str(date)
            price1 = str(price)
            pricelength = len(price1)
            pricelength = pricelength - 2
            price2 = price[1:pricelength]
            price3 = float(price2)
            stockResult = "The price of " + stockName1 + " today, " + date1 + ", is " + price1
            print stockResult

            shares = raw_input("Enter how many shares of " + stockName1 + " you would like: ")
            shares1 = int(shares)
            shares2 = str(shares)
            total = price3 * shares1


            numApple = int(numApple)
            numAmazon = int(numAmazon)
            numGoogle = int(numGoogle)
            numNetflix = int(numNetflix)
            numFacebook = int(numFacebook)
            numMicrosoft = int(numMicrosoft)
            numApple1 = str(numApple)
            numAmazon1 = str(numAmazon)
            numGoogle1 = str(numGoogle)
            numNetflix1 = str(numNetflix)
            numFacebook1 = str(numFacebook)
            numMicrosoft1 = str(numMicrosoft)
            numTesla1 = str(numTesla)

            if stockNum == 1:
                stockName = "Apple"
                if shares1 > numApple:
                    print "Please select a number of shares less than " + numApple1
                else:
                    numApple = numApple - shares1
            elif stockNum == 2:
                stockName = "Amazon"
                if shares1 > numAmazon:
                    print "Please select a number of shares less than " + numAmazon1
                else:
                    numAmazon = numAmazon - shares1
            elif stockNum == 3:
                stockName = "Google"
                if shares1 > numGoogle:
                    print "Please select a number of shares less than " + numGoogle1
                else:
                    numGoogle = numGoogle - shares1
            elif stockNum == 4:
                stockName = "Netflix"
                if shares1 > numNetflix:
                    print "Please select a number of shares less than " + numNetflix1
                else:
                    numNetflix = numNetflix - shares1
            elif stockNum == 5:
                stockName = "Facebook"
                if shares1 > numFacebook:
                    print "Please select a number of shares less than " + numFacebook1
                else:
                    numFacebook = numFacebook - shares1
            elif stockNum == 6:
                stockName = "Microsoft"
                if shares1 > numMicrosoft:
                    print "Please select a number of shares less than " + numMicrosoft1
                else:
                    numMicrosoft = numMicrosoft - shares1
            elif stockNum == 7:
                stockName = "Tesla"
                if shares1 > numTesla:
                    print "Please select a number of shares less than " + numTesla1
                else:
                    numTesla = numTesla - shares1

            numApple1 = str(numApple)
            numAmazon1 = str(numAmazon)
            numGoogle1 = str(numGoogle)
            numNetflix1 = str(numNetflix)
            numFacebook1 = str(numFacebook)
            numMicrosoft1 = str(numMicrosoft)
            numTesla1 = str(numTesla)
            stocksLeft = numApple1 + " of Apple | " + numAmazon1 + " of Amazon | " + numGoogle1 + " of Google | " + numNetflix1 + " of Netflix | " + numFacebook1 + " of Facebook | " + numMicrosoft1 + " of Microsoft | " + numTesla1 + " of Tesla"



            total1 = str(total)
            totalresult = "Total price of " + shares2 + " shares of " + stockName1 + " is $" + total1
            print totalresult
            toSend = stocksLeft + "\n" + totalresult
            sock.send(toSend)
        else:
            print "Come trade again another time!"
            print " "
            print " "
            client.stop()
