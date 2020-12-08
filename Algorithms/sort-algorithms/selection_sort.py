# to sor a sequence of no.s in ascending order

def selecn_sort(li):
    #scaning the slices li[0,len(li)], li[1,len(li)]....
    for start in range(len(li)):
        min_posn = start  #position of minum value
        for i in range(start,len(li)):
            if li[i] < li[min_posn]:
                min_posn = i
        (li[start],li[min_posn]) = (li[min_posn],li[start]) #swapin th min element to first

li = [3,7,2,1,45]

print(selecn_sort(li))
print(li)