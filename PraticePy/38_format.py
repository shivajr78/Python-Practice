name = "Shiva"
company = "Asus"
type = "VivoBook"
# a = f"Asus is {name}'s Laptop"  #This is an f string method


#This is an format method
#a = "{}'s Laptop is an {} Brand".format(name,company)


#if entring the argument not in serialwise, than use mentioning index no.
a = "{0}'s Laptop is an {2} of {1} Brand".format(name,company,type)

#if we don't use index no than result are different see:
#a = "{}'s Laptop is an {} of {} Brand".format(name,company,type)

print(a)