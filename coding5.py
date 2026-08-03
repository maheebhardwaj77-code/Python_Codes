# File I/O IN Python:-
#create a new file"demo.txt" using python. add the following data in it:-
f = open("demo.txt", "w")
data = f.write("Hi everyone\nWe are learning file I/O\nUsing java\nI like programming in java")
print(data)

#WAF that replace all occurrences of "java" with "python" in above file:-
with open("demo.txt", "r") as f:
    info = f.read()

new_info = info.replace("java", "python")
print(new_info)    

with open("demo.txt", "w") as f:
    f.write(new_info)

#search if the word "learning" exists in the file or not:-
word = "learning"
with open("demo.txt", "r") as f:
    info = f.read()
    if (info.find(word) != -1):
        print("found")
    else:
        print("not found")    