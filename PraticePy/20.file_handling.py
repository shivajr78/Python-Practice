
# # syntax for file handling

# f = open('simple01.txt', 'r')  #using open function to open file
# data = f.read()   #using reading function
# #data = f.read(5)   #read only 5 character
# print(data)
# f.close()    #Here using close function to close the opened file




# ######### For Readline function #################
# f = open('simple01.txt', 'r') 

# # read 1st line
# data = f.readline()  
# print(data)

# #read 2nd line
# data = f.readline()   
# print(data)

# #read 3rd line..... and so on......
# data = f.readline()   
# print(data)

# f.close()   


# ############ For Write Mode #####################

# f = open('another.txt','a')
# f.write("Shiv shiv shiv shiv")
# f.close()


################# With Statment ####################

# with open('1223344','r') as f: 
#     a = f.read()
# # with open('another.txt','w') as f: 
# #     a = f.write("Myself Shiva")
#     print(a)
#     f.close()

# import pandas as pd

# file = pd.read_csv("C:/Users/shiva/OneDrive/Desktop/DBMS.pdf")
# print(file)