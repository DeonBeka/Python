#try:
 #    result = 10/0
#except ZeroDivisionError:
#    print("THERE is an error")

fruits = {
    "apple": 5,
    "banna" :7,
    "ornage": 3,
}
try:
    print(fruits["cherry"])
except KeyError:
    print("The key does not exist")