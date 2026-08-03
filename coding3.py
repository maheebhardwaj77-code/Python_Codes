#Dictionary:-
dict = {
    "name" : "mahee",
    "course" : "btech aiml",
    "college" : "wctm"
}
print(dict)
print(type(dict)) #type dict
print(len(dict)) #length of dict
print(dict["course"]) #check info
dict["surname"] = "bhardwaj" #adding new value
print(dict)
source = {} #synatax for empty dictionary
print(type(source))
subject = {     #nested dictionary
    "subject_name" : "physic",
    "marks" : {
        1 : 98,
        2 : 95,
        3 : 92
    } 
}
print(subject)
print(subject["marks"][2])

#Set:-
nums1 = {1, 3, 5, 7, 9, 11}
nums2 ={2, 4, 6, 8, 10}
print(nums1)
print(type(nums1)) #type sets
print(len(nums1)) #length os set
age = set() #syntax for empty set
print(type(age))
nums1.add(2) #adding new value
print(nums1)
nums1.remove(5) #remove any value
print(nums1)
print(nums1.union(nums2)) #combines both set
print(nums1.intersection(nums2)) #combines common value 

#practice time:-
dict1 = {
    "table" : ["a piece of furniture", "lists of facts and figures"],
     "cat" : "a small animal"
}
print(dict1)

lang = {
    "python", "java", "C++", "python", "javascript", "java", "pyhton",
    "java", "C++", "C"
}
print(len(lang))