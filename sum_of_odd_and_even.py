def sum_of_odd_and_even(a):
    odd, even=0,0
    for i in a:
        while i !=0:
            num=i%10 
            if num %2==0: 
                even +=num
            else:
                odd +=num
            i //=10 
        return even,odd 
a=[345,334,454,224,789]
odd, even=sum_of_odd_and_even(a)  
print("odd", odd)
print("even", even)