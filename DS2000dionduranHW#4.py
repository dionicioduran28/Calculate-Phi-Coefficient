import math 
from itertools import islice

#read in early spring years into list 
def readSpring(filename):
    earlySpringList = []
    file = open(filename)
    
    for line in file:
        year = line.rstrip()
        earlySpringList.append(int(year))
    return earlySpringList

#loop through ground hog data adding into dictionary and changing dict values 
#to true or false based on result 
def readGround(filename):
    groundData = {}
    file = open(filename)
    
 
    #in each list as key and posions [1,2] as the values for each year
    for line in islice(file,2,None):
        splitLine = line.split()
        
        #dont read in years where 'no record' was found 
        #read in line where year is key and the result is joined
        if(splitLine[2] != 'Record'):
            groundData[int(splitLine[0])] = " " .join(splitLine[1:])
    
    #loop throuugh dictionary and replace results with true or false     
    for year in groundData:
        if(groundData[year] == "Full Shadow"):
            groundData[year] = True
        elif(groundData[year] == "No Shadow"):
            groundData[year] = False
        elif(groundData[year] == "Partial Shadow"):
            groundData[year] = None      
            
    return groundData
        
#takes in years with early spring and a dictionary containing 
def calculatePhi(springList, shadowTable):
    
    c1 = 0 
    c2 = 0
    i1 = 0
    i2 = 0

    #loop thru shadow table to create counters for each part of correlation calc
    for year in shadowTable:
        #omit year from calc if year is before 1936
        if(year >= 1936):        
            
            if(shadowTable[year] == True and year not in springList):
                c1 += 1 
            elif(shadowTable[year] == False and year in springList):
                c2 += 1
            elif(shadowTable[year] == True and year in springList):
                i1 += 1
            elif(shadowTable[year] == False and year not in springList):
                i2 += 1 
                
    #perform correlation calc once counter varibles have been calc 
    x = (c1 * c2 - i1 * i2)
    y = math.sqrt(c1 * c2 * i1 *i2)
    phi = x/y
    print (phi)

    
def main():
    springList = readSpring('early_spring_years.txt')
    shadowTable = readGround('groundhog_data.txt')
    calculatePhi(springList,shadowTable)

main()
    