def returner():
    with open('links.txt','r') as file:
        str1 = file.read()
        list1 = str1.split("\n")
        set1 = set(list1)
        return list(set1)