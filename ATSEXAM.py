""" arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]

for i in range(len(arr)):
  if arr[i] < mini:
     mini = arr[i]

print (mini)


n = int(input("Enter NUmber n: "))

if n %2 != 0 :
    print("Weird")
elif n%2 == 0 and 5 >= n >=2:
    print("Not Weird")
elif n%2 == 0 and 6 >= n >=20:
    print("Weird")
elif n%2 == 0 and 20 >= n:
    print("Not Weird")
 """

sum = 0
for i in range(1,101):
    sum = sum + i
   
print(sum)



