import numpy as np  #numpy library imported

#Function that converts numbers entered by the user to a 4x4 matrix
def createMatrix(arry, matrixName = ""):
    for i in range(np.size(arry[0:4])):
        for j in range(np.size(arry[0:4])):
            eleman = int(input(f"\n Enter the item of the {i+1}. column of the {j+1}. row of the matrix {matrixName}\n:"))
            arry = np.append(arry, eleman)

    arry = np.delete(arry, np.s_[:16])
    arry = np.reshape(arry, (4,4))
    return arry


#"A" matrix created with numpy library
a = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
a = createMatrix(a, "A")

print("\n\n")

#"B" matrix created with numpy library
b = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
b = createMatrix(b, "B")


print(f"\n\n----\nFirst Matris:\n\n{a}\n----")
print(f"\n\n----\nSecond Matris:\n\n{b}\n----")


matrixSum = np.add(a,b) 
print(f"\n\n----\nSum of A and B matrix:\n\n{matrixSum}\n----\n")


determinantOfSum = np.linalg.det(matrixSum)    


donguKontrol = True
while(donguKontrol):
    ask = int(input("\n\nDo you want find sum of determinant\n1) Yes\n0) No\n:"))

    if ask == 1:
        print(f"\n\n----\nDeterminant of sum A and B matrix:\t{determinantOfSum}")
        donguKontrol = False

    elif ask == 0:
        print("\n\n----\nOk. I don't calculating determinant of the sum.")
        donguKontrol = False

    else:
        print("\n\n----\nYour input was wrong. Please check and try again.\n----")