#import array as arr
def bubbleSort(arr):
    for j in range (len(arr)-1):
        for i in range (len(arr)-1):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
    return arr

a = []
while True:
    choice = input("Add:")
    try :
        a.append(int(choice))
        print(bubbleSort(a))
    except:
        break


