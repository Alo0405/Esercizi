import time
#8-1


'''def display_message():
    print('in this chapter I learn the function')
display_message()'''


#8-2


'''def favorite_book(Title:str):
    print(f'One of my favorite books is {Title}')
favorite_book('Alice in wonderland')'''







#implementazione bubble sort
numbers: list = [i for i in range(0, 10000)]

def bubblesort(numbers: list):
    for i in range(len(numbers)):
        swap_flag: bool = False
        for j in range (len(numbers) - i - 1):
            if(numbers[j] > numbers[j + 1]):
                swap_flag = True
                temp: int = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j+1] = temp
            continue
        if (swap_flag == False):
            return numbers
        continue
    return numbers
start: int = time.time()
numbers1 = bubblesort(numbers)
print(numbers1)
print(time.time() - start)