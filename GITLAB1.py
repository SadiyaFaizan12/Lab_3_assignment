class Flight():
    def __init__(self):
        self.d1={"AI161E90":["BLR"," BOM", 5600],"BR161F91 ":["BOM","BBI", 6750],"AI161F99":["BBI","BLR", 8210],"VS171E20 ":["JLR", "BBI", 5500],"AS171G30 ":["HYD", "JLR", 4400],"AI131F49":["HYD","BOM", 3499]}
    def city1(self):
        c=input("Enter city->")
        for i in self.d1:
            if self.d1[i][1]==c:
                print(i,self.d1[i],end="\n")
    def city2(self):
        c=input("Enter city->")
        for i in self.d1:
            if self.d1[i][0]==c:
                print(i,self.d1[i],end="\n")
    def city3(self):
        c1=input("Enter city1->")
        c2=input("Enter city2->")
        for i in self.d1:
            if (self.d1[i][0]==c1) and (self.d1[i][1]==c2):
                print(i,self.d1[i],end="\n")
def main():
    print("1. Flights for a particular City\n2. Flights From a city\n3. Flights between two given cities")
    ch=int(input("Enter your choice->"))
    obj=Flight()
    if ch==1:
        obj.city1()
    elif ch==2:
        obj.city2()
    elif ch==3:
        obj.city3()
    else:
        print("Invalid")
main()
                    
            
        
        
    