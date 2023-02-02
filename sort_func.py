from typing import List

def bubble_sort(numbers: List[int]):
    """冒泡排序"""
    stop_postion = len(numbers) - 1
    while stop_postion > 0:
        for i in range(stop_postion):
            current, next_ = numbers[i], numbers[i+1]
            # 当左指针数据 > 右指针，进行数据交换
            if current > next_:
                numbers[i], numbers[i+1] = next_, current
        stop_postion -= 1
    return numbers
    

def select_sort(numbers: List[int]):
    """选择排序"""
    stop_postion = len(numbers) - 1
    while stop_postion > 0:
        max_id = 0
        for i in range(stop_postion):
            if numbers[i+1] > numbers[max_id]:
                # 选择最大值索引
                max_id = i + 1
        numbers[stop_postion], numbers[max_id] = numbers[max_id], numbers[stop_postion]
        stop_postion -= 1
    return numbers


def insert_sort(numbers: List[int]):
    """插入排序"""
    stop_postion = 1
    while stop_postion < len(numbers) :
        end = stop_postion
        while end > 0:
            if numbers[end] < numbers[end-1]:
                numbers[end], numbers[end-1] = numbers[end-1], numbers[end]
            else:
                # 不用交换即可退出循环
                break
            end -= 1
        stop_postion +=1
    return numbers

        
def quick_sort(numbers: List[int], left, right):
    """快速排序, 递归"""
    if left >= right:
        return
    mid_value, start, end = numbers[left], left, right
    while start < end:
        if start < end and numbers[end] >= mid_value:
            end -= 1
        numbers[start] = numbers[end]
        if start < end and numbers[start] < mid_value:
            start += 1
        numbers[end] = numbers[start]
    numbers[start] = mid_value
    quick_sort(numbers, left, start-1)
    quick_sort(numbers, end+1, right)