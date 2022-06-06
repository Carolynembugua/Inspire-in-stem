
###################
#PYRAMIDS                                                       1
#Name : CAROLYNE MBUGUA
#date : 5/30/2022
###################
rows = int (input ("enter number of rows"))
k = 0
for i in range (1, rows + 1) :
    for space in range (1,(rows - i) + 1) :
        print(end = "")

while k != (2*i - 1) :
    print ("*",end ="")
k += 1    
k = 0
