//problem 1

# def addBorder(picture):
    
#     answer = ['']

#     for i in range(len(picture[0])+2):
#         answer[0] += '*'

#     for i in range(len(picture)):
#         answer.append('*')
#         for j in range(len(picture[0])):
#             answer[i + 1] += picture[i][j]
#         answer[i + 1] += '*'

#     answer.append(answer[0])

#     return answer

//problem 2

# def oddNumbersBeforeZero(sequence):
#     #declare our function and pass in the sequence as an argument
#     result = 0
#  #result starts at zero   
#     for i in range(0, len(sequence)):
#         if sequence[i] == 0:
#             break         
#         if sequence[i] % 2 == 1:
#             result += 1
#     return result
#range gives us the entire range of a specific number len gives us the length
#for every item in the list from 1 to the length of the sequence break if it's 0
#if each item in sequence is divsble by 2 == 1 
#
#return the result 

//problem 3

# def minMaxDifference(inputArray):
    
#     indexOfMinimum = 0
#     indexOfMaximum = 0

#     for i in range(1, len(inputArray)):
#         if inputArray[i] < inputArray[indexOfMinimum]:
#             indexOfMinimum = i
#         if inputArray[i] > inputArray[indexOfMaximum]:
#             indexOfMaximum = i
#     return inputArray[indexOfMaximum] - inputArray[indexOfMinimum]

//problem 4





