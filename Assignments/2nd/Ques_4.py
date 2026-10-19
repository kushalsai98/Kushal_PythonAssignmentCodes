def num_pyramid(n):

    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()

num_pyramid(5)