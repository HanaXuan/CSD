def insertionSort(a):
    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            for j in range(i-1,-1,-1):
                if a[j] > a[j+1]:
                    tmp = a[j]
                    a[j] = a[j+1]
                    a[j+1] = tmp
                    print(a)
                if a[j] <= a[j+1]:
                    continue
    return a
a = []
while True:
    choice = input("Add:")
    try :
        a.append(int(choice))
        print(insertionSort(a))
    except:
        break

