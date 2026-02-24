def solution(number):#function that brings the number of the list
    #If case to segmente negative values
    if number == -1:
        return 0
    #otherwise we need to count
    else:
        #variable count is needed to acumulate the sum
        count=0
        #we need a repetitive cycle to validatae each number of the list
        for i in range(1,number):
            #if condition to validate with a module if is multiple of 3 or 5. 'OR' is needed for count it once
            if (i % 3 == 0) or (i % 5 == 0):
                #we count the actual number of the list we are poiting and make a sum with the historical value of count variable
                count=count+i
        #we return expected value
        return count