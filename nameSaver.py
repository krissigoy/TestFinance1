numApple = 9999
numAmazon = 9999
numGoogle = 9999

while 1:
    question1 = input("Hello, what is your first and last name? ('answer')")
    
    question2 = input("Would you like to buy more stocks? 1==yes | 2==no: ")
    question2 = int(question2)

    if question2 == 1:

        #if numAmazon < 1000 or numApple < 1000 or numGoogle < 1000:
        #    print "Not enough stocks left to trade"
        #    print ""
        #    print ""
        #    break

        stockNum = raw_input("Enter your preffered stock. 1=Apple, 2=Amazon, 3=Google: ")
        date = raw_input("Enter the 2016 date that you would like to search up in mm/dd/yy format: \n")
        datetemp = " "
        price = 0
        stockNameActual = ""
        transHistory1 = open('TRANSACTION_HISTORY', 'r')
        dates = open('dates.txt', 'r' )
        apple = open('apple.txt', 'r' )
        amazon = open('amazon.txt', 'r' )
        google = open('google.txt', 'r' )
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
        #print "Line number is " + lineNumber1

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
        else:
            stockName = "NA"
            print "Please enter a number from 1-3"

        stockName1 = str(stockName)
        print "Selected stock is " + stockName1

        date1 = str(date)
        price1 = str(price)
        pricelength = len(price1)
        pricelength = pricelength - 2
        price2 = price[1:pricelength]
        price3 = float(price2)
        stockResult = "The price of " + stockName1 + " at " + date1 + " was " + price1
        print stockResult

        shares = raw_input("Enter how many shares of " + stockName1 + " you would like: ")
        shares1 = int(shares)
        shares2 = str(shares)
        total = price3 * shares1

        total1 = str(total)
        totalresult = "Total price of " + shares2 + " shares of stock is $" + total1
        print totalresult


        lineCounter = 0
        lineCounterV2 = 0
        lineInTrans = 0
        lineInTrans3 = 0
        for line in transHistory1:
            lineInTrans = line
            if lineCounter % 3 == 0:
                lineInTrans3 = line
            lineCounter = lineCounter + 1
        lineCounter1 = str(lineCounter)
        print "Line count is " + lineCounter1

        #print lineInTrans3

        #numApple = lineInTrans3[:4]
        #numAmazon = lineInTrans3[18:22]
        #numGoogle = lineInTrans3[37:41]
        numApple = int(numApple)
        numAmazon = int(numAmazon)
        numGoogle = int(numGoogle)

        if stockNum == 1:
            stockName = "Apple"
            numApple = numApple - shares1
        elif stockNum == 2:
            stockName = "Amazon"
            numAmazon = numAmazon - shares1
        elif stockNum == 3:
            stockName = "Google"
            numAmazon = numAmazon - shares1

        numApple1 = str(numApple)
        numAmazon1 = str(numAmazon)
        numGoogle1 = str(numGoogle)
        stocksLeft = numApple1 + " of Apple ||| " + numAmazon1 + " of Amazon ||| " + numGoogle1 + " of Google"


        #Keep a HISTORY file of all transactions
        transHistory = open('TRANSACTION_HISTORY', 'a')
        transHistory.write(question1)
        transHistory.write(stocksLeft)
        transHistory.write('\n')
        transHistory.write(totalresult)
        transHistory.write('\n')
        transHistory.write("")
        transHistory.close()

        print " "
        print " "
        print " "

    else:
        print "Come trade again another time!"
        print " "
        print " "
        break
