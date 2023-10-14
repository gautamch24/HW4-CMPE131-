#using bubble sort to sort through the combined(unsorted)list 
def merge_list(list1, list2):
    #concatenate both lists into one list
    conList = list1+list2
    lenVal = len(conList)
    #outter loop runs from 0 to the vale of lenVal
    for i in range (lenVal):
        #isSwapped is equal to false so it can be used later in the code when checking if all elements are sorted(saves up space and is more effcient)
        isSwapped = False
        #inner for loop is used to traverse the list and compare each one to see if it is greater than the other(runs from 0 till length - whatever i counter is at -1(basically to get from 0 to the final element at each iteration))
        for j in range(0, lenVal-1):
            #comparing each element(j is the value of whatever number iteration it is at)
            if conList[j] > conList[j+1]:
                #swapping: step1 set the value of element j in conList to a temporary variable(whatever iteration it is at)
                temp = conList[j]
                #step2: set that value of element j to the next element of j+1
                conList[j] =conList[j+1]
                #step3: now the next element is equal to temp(can be used again in the next iteration to compare again)
                conList[j+1] = temp
                #isSwapped is true now because it is checking if the list is fully sorted 
                isSwapped = True
                
            #the purpose of this function is to make sure that it is alread sorted
        if not isSwapped:
            break





#defines both lists
#list1 = [1,29,11,4]
#list2 = [6,91,82,3]
#merge_list(list1,list2)
