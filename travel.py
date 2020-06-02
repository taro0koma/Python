import sys
import csv
import os

class Error(Exception):
    pass
class InputError(Error):
    def __init__(self,filename,message):
        self.filename=filename
        self.message=message
    @property
    def name(self):
        return self.name


if len(sys.argv)<2:
    print("csvファイルを指定してください。")
    sys.exit()

answer=[]
# try:
#     if os.path.exists(sys.argv[1]):
#         filename=sys.argv[1]
#     else:
#         raise InputError(filename,"ファイルが見つかりません。")
# except InputError as e:
#     print(e.name(),e.message)
#     continue

try:
    
    with open(sys.argv[1],"r",encoding="utf8") as f:
        rd=csv.reader(f)
        for row in rd:
            for column in row:
                answer.append(column)
except FileNotFoundError:
    print("ファイルが見つかりません",sys.argv[1])
    sys.exit()
            
results={}
print(answer)
for region in answer:
    if region in results:
        results[region]+=1
    else:
        results[region]=1
for region in sorted(results.items(),key=lambda c:c[1],reverse=True):
    print(region[0],":",region[1])