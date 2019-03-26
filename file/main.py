#encoding=utf-8

def MakeChoice():
    while True:
        print("please select: 1, create one 2,overwrite one")
        cho = input("please input your choice 1 or 2: ")
        if cho == '1':
            return True
            break
        elif cho == '2':
            return False
            break
        else:
            print("wrong choice")


def LineProcess(line):
    return line.strip()

if __name__ == '__main__':
    filename = input('please input the filename: ') # 代码与文件在同一文件夹下
    newlines = []
    try:
        with open(filename, 'r') as f:
            newlines = map(LineProcess, f.readlines())
        cho = MakeChoice()
        if cho:
            newFile = open('new.txt', 'w')
            for eachline in newlines:
                newFile.write(eachline + '\n')
            newFile.close()
        else:  # 覆盖原来的文件
            overwriteFile = open(filename, 'w')
            for eachline in newlines:
                overwriteFile.write(eachline + '\n')
            overwriteFile.close()
    except:
        print('filename is wrong!')

