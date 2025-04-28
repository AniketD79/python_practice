

#Q1
# def recursive_sum(a):
#     if(a==0):
#         return 0
   
#     # print(a)
#     return recursive_sum(a-1) +a
# sum= recursive_sum(5)
# print(sum)

# recursive_sum(5)


#Q2

# def recursive_list(list, index=0):
#     if(index==len(list)):
#         return
#     print(list[index])
#     recursive_list(list, index+1)
# nums=[1,2,4,2,5,3,4]
# recursive_list(nums)

def recursiveList(list, index):
    if(index==0):
        print(list[index])
        return
    print(list[index])
    recursiveList(list, index-1)

recursiveList([1,2,3,4,5,6,7],len((list)-1))






