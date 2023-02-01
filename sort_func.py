from typing import List

def bubble_sort(numbers: List[int]):
    """冒泡排序"""
    stop_postion = len(numbers) - 1
    while stop_postion > 0:
        for i in range(stop_postion):
            current, next_ = numbers[i], numbers[i+1]
            # 当左指针数据 > 右指针交换
            if current > next_:
                numbers[i], numbers[i+1] = next_, current
        stop_postion -= 1
    return numbers
    

def select_sort(numbers: List[int]):
    stop_postion = len(numbers) - 1
    while stop_postion > 0:
        max_id = 0
        for i in range(stop_postion):
            if numbers[i+1] > numbers[max_id]:
                max_id = i + 1
        numbers[stop_postion], numbers[max_id] = numbers[max_id], numbers[stop_postion]
        stop_postion -= 1
    return numbers


def insert_sort(numbers: List[int]):
    stop_postion = 1
    while stop_postion < len(numbers) :
        end = stop_postion
        while end > 0:
            if numbers[end] < numbers[end-1]:
                numbers[end], numbers[end-1] = numbers[end-1], numbers[end]
            end -= 1
        stop_postion +=1
    return numbers

        
    