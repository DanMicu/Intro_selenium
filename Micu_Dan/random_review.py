import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# browser.get("https://myfewsteps.blogspot.com/selenium-practice")
# browser.maximize_window()
#
# username = browser.find_element(By.XPATH, value ='//*[@id="fname"]')
# username.clear()
# username.send_keys("dan")
# time.sleep(5)

'''
X Y Z 
324


'''

# X, Y, Z = 2 , 3, 4
#
# print(X,Y)
#
# X=Y=Z = 2
# print(X,Y)
#
# X = str('3')
# print(X)
# print(type(X))
# x = 'one two three four five'
# print(x[0:5])
# print(x.upper())
# y = 3
# y += 3
# print(y)
# n = 3.21433434
# print(n)
# n %= y
# print(n)
#
# nota_de_trecere = 4.5
# nota = float(input('scrie nota ta \n'))
# if nota >= nota_de_trecere and nota <= 10:
#     print(f'ai trecut cu {nota}')
# elif nota < nota_de_trecere:
#     print("failed")
# else:
#     print('invalid')
#
# list1 = [1, 2, 'one', 3]
# print(list1)
# print(type(list1))
# print(list1[0])
# print(len(list1))
#
# dict1 = {1:True,2:True,4:'one'}
# print(dict1)
# print(type(dict1))
# print(dict1[1])
# print(len(dict1))
# set1 = {'alb', 'rosu', 'galben', 'alb'}
# print(set1)
# print(len(set1))
# print(type(set1))
#
# tuple1 = ('apple','banana',"point")
# print(tuple1)
# print(len(tuple1))
# print(type(tuple1))
#
# x = 10
#
# while x<=22:
#     print(f'true {x}')
#     x+=1
# else:
#     print('finished')

# for i in range(4):
#     print(i)
# else:
#     print('done')

list2 = [1, 2, 4, 3]
# for num in list2:
#     print(f'{num} is')
# for num in list2:
#     if num >= 4:
#         continue #break
#     print(num)

def print_hi():
    print('Hi!')

def print_hi_user(user):
    print(f'hi! {user}')

print_hi()
print_hi()
print_hi_user('dan')

