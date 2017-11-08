
import copy
# n = int(input())
# aset = [int(input())for i in range(n)]
# powset = []
# powsetn_1 = []
def Subset(aset):
    if(len(aset) == 0):
        return([[]])
    else:
        temp = aset[0]
        del aset[0]
        # powset = []
        powset = Subset(aset)
        # if len(powset) == 0:
        # 	powset = [[], [temp]]
        # 	return powset
        # print(powset)
        powsetn_1 = copy.deepcopy(powset)
        # print powsetn_1
        for i in range(len(powset)):
            powset[i].append(temp)
            # print("loop ", powset)
        powset = powset + powsetn_1
        #print("powersetn_1 ", powsetn_1)
        #print("powerset ",powset)
        return powset

#finalset = Subset(aset)
aset = [1, 2, 3]
print(Subset(aset))
#print(powset)
