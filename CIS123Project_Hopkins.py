#Jack Hopkins
#CIS123

#opens file and puts in read mode
openFile = open("lorem_ipsum.txt","r")
getOut = "again"

#read line variable
allLines = openFile.readlines()


while getOut == "again":

    startProg = input("Press enter to start: ")

    if startProg == "":
        #resets count
        wordCount = 0
        lookUp = input("Choose word to search for (case sensitive): ")
        #check all lines in file and prints row with specified value
        for line in allLines:
            if lookUp in line.split():
                print(lookUp)
                wordCount = wordCount + 1   #word occurrence counter

        print("The number of times", lookUp, "is used in this document are: ", wordCount)
        getOut = input("Type quit to exit or again to run again: ")

    #incorrect input restarts program
    else:
        continue


#close file
openFile.close()