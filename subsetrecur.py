

n = int(input())
aset = [int(input())for i in range(n)]
powset = []
powsetn_1 = []
def Subset(aset):
    if(len(aset) == 0):
        return([])
    else:
        temp = aset[0]
        del aset[0]
        powset = []
        powset.append(Subset(aset))
        #print(powset)
        powsetn_1 = powset
        for i in range(len(powset)):
            powset[i].append(temp)
            #print(powset)
        powset += powsetn_1
        #print(powset)
        return powset

#finalset = Subset(aset)
print(Subset(aset))
#print(powset)
