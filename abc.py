def search(p,new,count):
    half=int(len(p)/2)
    #print(half)
    #print(p)
    if len(p)==2:
        print(p)
        print(count)
        
        
    elif p[half-1]>=new:
        print(p)
        search(p[:half],new,count)
    elif p[half-1]<=new:
        count=count+half
        print(p)        
        search(p[half:],new,count)
    
 

p=[1,1,1,2,3]
new=1
print(search(p,new,0))
'''p[search(p,new,0)]=new
print(p)'''
