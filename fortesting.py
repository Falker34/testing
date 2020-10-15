#Series26
#K = int(input("Введите число K: ")) # два числа мне удалось перенести из файла
#N = int(input("Введите число N: "))
f = open('left.txt','r') #файл ввода
g = open('dead.txt','w') #файл вывода
N = f.read(1)
N = int(N) #перевожу элемент из строки в число
K = f.read(2)
K = int(K)
Kna = []
Kna.append(f.read()) # вся строчка выходит как одно число
#Kna.remove('\n') # неудачная попытка убрать "\n"
print(N,K,Kna)
