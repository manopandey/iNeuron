def sock_merchant(unpaired_socks):
    pairs = 0
    for sock in set(unpaired_socks):
        total_count_of_current_sock = unpaired_socks.count(sock)
        pairs += total_count_of_current_sock//2
    print(pairs)
        
# sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])
# sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90])
# sock_merchant([])


def find_fulcrum(list):
    for i,v in enumerate(list):
        sum_of_right = sum(list[i+1:])
        sum_of_left  = sum(list[:i])
        if sum_of_right==sum_of_left:
            print(str(v))
            return v
    print("-1")
    return -1
        

# find_fulcrum([3, 1, 5, 2, 4, 6, -1])
# find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) 
# find_fulcrum([9, 1, 9])
# find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3])
# find_fulcrum([8, 8, 8, 8])

def pairs(array):
    midpoint = round((len(array)-1)/2)
    final = []
    for i in range(len(array)):
        final.append([array[i],array[-i-1]])
        if i == midpoint:
            break
    print(final)


# pairs([1,2,3,4,5,6,7])
# pairs([1,2,3,4,5,6])
# pairs([5,9,8,1,2])
# pairs([])



def count_lone_ones(number):
    number_list=[int(d) for d in str(number)]
    temp_index = []

    try:
        for idx,num in enumerate(number_list):      
            if number_list[idx]==1 and number_list[idx+1]==1 :
                temp_index.extend([idx,idx+1])
    except:
        pass
    finally:
        for i in set(temp_index):
            number_list[i] = 2
    print(number_list.count(1))
 

count_lone_ones(1)