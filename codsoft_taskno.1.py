def main():
    print("1 - To add item\n2 - To delete item\n"
          "3 - To edit item\n4 - To read list\n5 - To exit")
def repeat(result):
    if result == 1:
        add()
    elif result == 2:
        dele()
    elif result == 3:
        edit()
    elif result == 4:
        read()
    elif result == 5:
        return 0

def add():
    item = input("enter the item to be added: ")
    print("Item is added sucessfully")
    nums.append(item)
    process()

def dele():
    item = int(input("enter the index of item to be deleted: "))
    print("Item is deleted sucessfully")
    nums.pop(item)
    process()

def edit():
    item = int(input("enter the index of item to be edited: "))
    nums[item] = input("enter the new item: ")
    print("Item is edited sucessfully")
    process()

def read():
    process()

def process():
    print(nums)
    main()
    s = int(input("enter the number to continue the process: "))
    repeat(s)

print("To Do List:\nEnter:")
main()
nums = []
remo = int(input("enter the number:"))
repeat(remo)


