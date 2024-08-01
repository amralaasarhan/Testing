# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def isPalindrome(str):
    str = str.upper()
    i=0
    j=len(str)-1
    while i<j:
        if str[i] != str[j]:
            return False
        i+=1
        j-=1
    return True

def binarySearch(nums, target):
    low = 0
    high = len(nums)-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1
# print(isPalindrome("Dad"))
nums = [3, 4, 5, 6, 7, 8, 9]
print(binarySearch(nums,9))