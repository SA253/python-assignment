obj=[{
    "fname":"sachin",
    "lname":"tendulkar",
    "city":"mumbai"
    },
    {
    "fname":"sharmila",
    "lname":"chowdary",
    "city":"anantapur"
    },{
    "fname":"saurav",
    "lname":"gangauly",
    "city":"bengal"
    }]
def mysort(el):
    print("mysort called for  "+el["fname"])
    return el["fname"]
obj.sort(key=mysort)
print(obj)