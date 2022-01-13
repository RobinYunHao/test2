#!/usr/bin/python
# -- coding:utf8 --
# filename = "gold.game"


# @@@line:['money', '1']
# Reading line： 2
# processMainLogic......, name = 1
# @@@line:['key', '5']
# Reading line： 3
# processMainLogic......, name = 1
# @@@line:['stone', '9']
def test_processMainLogic(line, name):
    print("processMainLogic......, name = " + name)
    # js = line.strip().split('=')[0]
    js = line.strip().split('=')
    print('@@@line:' + str(js))


def getValueInFile(keyName, filename):
    value = myMain(keyName, filename)
    print("###Success! Get the value of name :" + keyName + ", the value is : " + str(value))
    return value


def processMainLogic(line, name):
    key = line.strip().split('=')[0]
    if key == name:
        value = line.strip().split('=')[1]
        print("@@@get the value:" + value)
        return key ,value
        #key,value
    else:
        return "null", ""


def process(line, index, name):
    # print("Reading line： " + str(index))

    key, value = processMainLogic(line, name)

    print ("Get the value :" + str(value) + ", get the key: " + str(key))
    return key, value


def myMain(name, filename):
    index = 1
    value = ""
    with open(filename) as f:
        # 按行迭代文件
        for line in f.readlines():
            key, value = process(line, index, name)
            if key == name:
                break
    return value


if __name__ == '__main__':
    getValueInFile("stone","gold.game")