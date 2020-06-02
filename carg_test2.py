import sys
 
try:
    for num in sys.argv[1::]:
        float(num)
except ValueError:
    print("Error:数値を入力してください")
    sys.exit()
sum_ = 0.0
 
for i in range(1, len(sys.argv)):
    sum_ += float(sys.argv[i])
print(sys.argv)
print("総和：",sum([float(a) for a in sys.argv[1::]]))