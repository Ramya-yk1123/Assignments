dict={
    "id":101,
    "name":"Ramya",
    "age":22,
    "Course":"MCA",
    "College":"UBDT College",
    "Place":"Davangere"
}
print(dict["id"])
print(dict.get("id"))
dict.update({"USN":"4UB24MC076"})
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.pop("USN"))
print(dict.popitem())
dict.clear()
print(dict)
print(dict.items())

