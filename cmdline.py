import sys
 
if len(sys.argv) < 2:
    print("ファイル名を指定してください。")
    sys.exit()  # プログラムを終了する
 
f = open(sys.argv[1], "r",encoding="utf8")
 
lines = f.readlines()
 
for line in lines:
    print(line, end="")
 
f.close()