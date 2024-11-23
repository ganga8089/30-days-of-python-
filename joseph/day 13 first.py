colour_list_1=["red","blue","green","black"]
colour_list_2=["red","yellow","blue","violet"]
print("colours present in list 1 that are not present in list 2 are:")
for i in colour_list_1:
    if i not in colour_list_2:
        print(i)
