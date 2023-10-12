# fruits = ['Banana','Mango','Watermelon','Apple','Orange']

# for item in fruits:
#     print(item)

######################## FOR IN Range  #######################

# for i in range(1,8,2):   ## (From start,At end,step size)
#     print(i)    # step size: returing element,after mention size,
#                 # i.e, Here after every 2 element is returing

# for i in range(10):
#     print(i)

# else:
#     print("The condition is not satisfy Here, i.e,The End of loop")



# #### BREAK Statement ################
# for i in range(10):
#     print(i)

#     if(i == 5):
#         break

###### Continue Statement #########

for i in range(10):
    if i == 5:
        continue  # skiping 5 and print all element

    print(i)