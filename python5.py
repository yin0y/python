import random
import time

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print()

menulist = []
set_menulist = set(menulist)

while True:
    menu = input("메뉴추가: ")
    menulist.append(menu)
    add_menu_set = set_menulist | set([menu])

    if set_menulist == add_menu_set:
            del menulist[-1]
            print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요")
            print("현재 메뉴 수 = ", len(menulist))
            print()

    else:
        set_menulist = add_menu_set
        print("현재 메뉴 수 = ", len(menulist))
        print()

        if len(menulist) == 5:
            break

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(menulist)
print("과연 오늘의 메뉴는?")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

a = random.choice(menulist)
print("오늘의 메뉴는", menulist.index(a)+1 ,"번 째 메뉴,", a ,"입니다.")

        

     

