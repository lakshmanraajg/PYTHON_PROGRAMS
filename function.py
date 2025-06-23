# def fun(num, x=1):
#     for i in range(x):
#         num = num + 1
#         print(num)

#fun(2)
#fun(2,3)
#fun(x=2, num=3)  # Change of  arguments works based on names (no particular order)

# def multi_arg(*arg):      #  -> Variable Argument
#     result = 0
#     for i in arg:
#         result = result + i
#     print(result)
# multi_arg(1,2,3,1.2342567)


def multi_arg(arg1,arg2,*ar):
    print(arg1,arg2)
    print(ar)
multi_arg(2,3,45,1,3,5,1,3,5)