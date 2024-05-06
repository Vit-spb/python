my_list = [1,2,34,5,7,8,99,0,30,67,89,35,2]

# res_list = list(map(lambda x: x**2, my_list))
# print (res_list)

res_list = list(filter(lambda x: x*2==4, my_list))
print (res_list)

res_list=[]
f = lambda x: x%2 != 0
for el in my_list:
    if f(el):
        res_list.append(el)
print(res_list)

