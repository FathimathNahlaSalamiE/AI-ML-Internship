try:
    file = open("data.txt","r")
except FileNotFoundError:
    print("there is no such files")