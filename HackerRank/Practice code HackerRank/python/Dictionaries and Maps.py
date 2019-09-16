# Enter your code here. Read input from STDIN. Print output to STDOUT

phoneBook = {}



def telephone(mystr):
    arr = mystr.split(" ")
    # print(arr)
    savecontact(arr)

def savecontact(arr):
    phoneBook.update({arr[0]:arr[1]})
    # print(phoneBook)

if __name__ == "__main__":
    entries = int(input())
    for c in range(0,entries):
        mystr = input()
        telephone(mystr)

    try:
        while True:
            namesearch = input()
            try:
                print(namesearch+"="+phoneBook[namesearch])
            except:
                # print(namesearch,"this is")
                print("Not found")

    except EOFError:
        pass
