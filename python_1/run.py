
import time
def sum_two_smallest_numbers(numbers):
    total=0

    ari=sorted(numbers,reverse=True)


    # print(ari)

    # ari=ari.sort(reverse=True)
    a=ari.pop()
    b=ari.pop()
    print(a)
   

    return (a+b)
    # return [num*num2 for num,num2 in ari]
    


# Test.describe("Basic tests")
# sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
# Test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
# Test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)  
s=sum_two_smallest_numbers([25, 42, 12, 18, 22])

def sum_two_numbers(numbers):
    ari=[numbers[0],numbers[1]]

    for i in range(2,len(numbers)):
        for num in ari:
            if  numbers[i]<num:

                ari.remove(num)
                ari.append(numbers[i])


        

    return ari


def odd_or_even(number):
    return "Even" if number%2==0 else "Odd"

def even_or_odd(number):
    return ["Even", "Odd"][number % 2]


def opposite(number):
   
    return int(-number)


def unique_in_order(iterable):
    print("Sw")
    first=0
    iterable=list(iterable)
    print(iterable[-1])
    for i in range(1,len(iterable)):
        if iterable[first]==iterable[i]:
            iterable[first]=None

        first+=1
          
    return  [x for x in iterable if x is not None]


def unique_in_order(iterable):
    result=[None]
    for item in iterable:
        if item!=result[-1]:
            print(result[-1])
            result.append(item)
    return result[1:]


def is_divisible(n,x,y):
    # if n%y==0 and n%x==0:

    #     return True
    return True if (n%(x*y)==0) else False


def is_divisible(n,x,y):
    return n%x==0 and n%y==0



def minMax(nums):
    minValue=nums[0]
    maxValue=nums[0]
    for i in range(1,len(nums)):
        if nums[i]<minValue:
            minValue=nums[i]
        elif nums[i]>maxValue:
            maxValue=nums[i]


    return [minValue,maxValue]

# print(f'seconds spent is {(time.time()-c)}')

# def minMax(nums):
#     minValue=min(nums)
#     maxValue=max(nums)
#     print("As")
#     return [minValue,maxValue]


# def minMax(nums):
#     return [min(nums),max(nums)]
c=time.time()
print(minMax([8,2,10,11,13]))

print(time.time()-c)


print(is_divisible(21,2,3))







       
    
    
        
    
        
    


    #your code here