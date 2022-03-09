#Write a Python program find a list of integers with exactly two occurrences of nineteen
# and at least three occurrences of five.


list1=[10,12,14,13,10,12,12]
if list1.count(12)>=3 and list1.count(10)==2:
    print("list is :",list1)
    print("the total count of 12 is:",list1.count(12))
    print("list is:",list1)
    print("the total count of 10 is:",list1.count(10))

    print(True)