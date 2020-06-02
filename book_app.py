import os
import time
import csv
import platform


with open("./books.csv",encoding="utf8") as fp:
    books=list(csv.reader(fp))
    return
    
def get_return():
    time.sleep(1)
    return input("メニューに戻ります　>> 　Enterキー")

def get_confirm():
    while True:
        x=input("以上でよろしいでしょうか？（ yes / no ）
        if x in ['y','yes','Y','Yes','YES']:
            return True
        elif x in ['n','no','N','No','NO']:
            return False
        else:
            print("yes / no どちらかを入力してください。")

def clear_screen():
    # ターミナルコマンドを入力するメソッド　画面クリア
    if platform.system()=="Windows":
        os.system('cls')
    else:
        os.system('clear')

def int_check(value,string):
                
                

        