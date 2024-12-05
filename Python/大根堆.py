def max_heap(lis):
    i=len(lis)-1
    n=len(lis)
    while i >0:
        if i%2==1:
            left=i
            father=int(left/2)
            if lis[father]<lis[left]:
                tmp=lis[father]
                lis[father]=lis[left]
                lis[left]=tmp
            i-=1
        else:
            right=i
            left=i-1
            father=int(left/2)
            if max(lis[left],lis[right])>lis[father]:
                tmp=lis[father]
                if lis[left]>lis[right]:
                    lis[father]=lis[left]
                    lis[left]=tmp
                elif lis[right]>lis[left]:
                    lis[father]=lis[right]
                    lis[right]=tmp
                if 2*left+2<n and max(lis[2*left+1],lis[2*left+2])>lis[left]:
                    i=2*left+2
                    continue
                elif 2*left+1<n and lis[2*left+1]>lis[left]:
                    i=2*left+1
                    continue
                elif 2*right+2<n and max(lis[2*right+1],lis[2*right+2])>lis[right]:
                    i=2*right+2
                    continue
                elif 2*right+1<n and lis[2*right+1]>lis[right]:
                    i=2*right+1
                    continue
            i-=2
