d= {
    "amit":90,
    "om":80,
    "ram":60,
    
}
i = input("Enter user name :")
if i in d:
    print( f" {i}'s  marks : {d[i]}")
else:
    print("student not found")