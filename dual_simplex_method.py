import numpy as np
arr = np.array([[1,-1,-2,1,-6],
              [-1,0,1,0,2],
              [0,2,3,-2,8],
              [1,-1,1,-1,0]],float)




    
class DualSimplex():
    
    def __init__(self,A):
        self.a = np.copy(A)
        self.n, self.m = self.a.shape 
        self.main()
    
    def nonOptElem(self):
        for i in range(self.m-1):
            if self.a[self.n-1][i] < 0: # Проверка на отрицательный элемент
                print("План не является почти оптимальным.")
                return [self.n-1, i]
        return None
    
    def square_method(self,i,j, v,g, newA): # (i,j) - разрешающий элемент, (v,g) - текущий элемент перебора
        # Два остальныъ элемента в прямоугльника находятся так:
        # a = (i,g) и b = (v,j)
        # Формула: Новый элемент = старое значение текущего - (a*b)/ разрешающий    
        newA[v][g] = self.a[v][g] - ((self.a[i][g] * self.a[v][j])/self.a[i][j])  
    
    
    
    def jordan(self,i,j):
        newA = np.copy(self.a)
        for g in range(1, self.m):
            newA[i][g] *= -1
    
        for v in range(self.n):
            if (v != i):
                for g in range(self.m):
                    if g != j:
                        # (v,g) - элемент, который необходимо пересчитать
                        # он не попадает в стобец разрещающий и в строку
                    
                        self.square_method(i,j,v,g, newA)
        print(newA)
        return newA
    
    def minimum(self,row):
        m = 0
        for i in range(len(row)-1):
            if row[i] >= 0:
                if row[i] < row[m]:
                    m = i
        return m
    
    def findColElem(self,i):
        for j in range(self.n-1):
            if self.a[j][i] < 0:
                print(f"Разрешающая строка - ({j})")
                tempRow = self.a[self.n-1][:] / self.a[j][:]
                print(f"Разрешающий элемент: ({j},{self.minimum(tempRow)})")
                return [j,self.minimum(tempRow)]
        print("Отрицательный элемент в колонке не найден")
        return None
    
    def main(self):

        while True:
            rowElem = self.nonOptElem()
            
            if rowElem != None:
                print(f"Отрицательный элемент в целевой строке: ({rowElem[0]},{rowElem[1]})")
                rElem = self.findColElem(rowElem[1])
                if rElem != None:
                    resA = self.jordan(rElem[0],rElem[1])
                    self.a = np.copy(resA)
                else:
                    print("Задача не разрешима")
                    break
            else:
                print("План оптимален")
                break
    


# def minimum(row):
#     m = 0
#     for i in range(len(row)-1):
#         if row[i] >= 0:
#             if row[i] < row[m]:
#                 m = i
#     return m

# def square_method(i,j, v,g, newA): # (i,j) - разрешающий элемент, (v,g) - текущий элемент перебора
#     # Два остальныъ элемента в прямоугльника находятся так:
#     # a = (i,g) и b = (v,j)
#     # Формула: Новый элемент = старое значение текущего - (a*b)/ разрешающий    
#     newA[v][g] = a[v][g] - ((a[i][g] * a[v][j])/a[i][j])  
    
    
    
# def jordan(i,j):
#     newA = np.copy(a)
#     for g in range(1, m):
#         newA[i][g] *= -1
    
#     for v in range(n):
#         if (v != i):
#             for g in range(m):
#                 if g != j:
#                     # (v,g) - элемент, который необходимо пересчитать
#                     # он не попадает в стобец разрещающий и в строку
                    
#                     square_method(i,j,v,g, newA)
#     print(newA)
#     return newA

# def isOpt(A):    
#     for i in range(m-1):
#         if A[n-1][i] < 0: # Проверка на отрицательный элемент
            
    
# print(a)  
# for i in range(m-1):
#     if a[n-1][i] < 0: # Проверка на отрицательный элемент
#         print("Ищем почти оптимальный план")
        
#         for j in range(n-1):
#             if a[j][i] < 0:
#                 print(f"Отрицательный элемент- ({j},{i})")
#                 tempRow = a[n-1][:] / a[j][:]
#                 print(f"Разрешающий элемент: ({j},{minimum(tempRow)})")
#                 resA = jordan(j,minimum(tempRow))       
#                 a = np.copy(resA)
#                 print(i)
#                 break
#             else:
#                 print("Отрицательный элемент не найден")
#                 break

# # Нужно сделать, чтобы после каждой симплекс таблицы 
D = DualSimplex(arr)