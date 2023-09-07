import sys, os, re, chardet


def utf8_gbk(file_path):
    with open(file=file_path, mode="r+b") as file:
        content = file.read()
        print("file: " + file_path)
        result = chardet.detect(content)
        print(result)
        if result["encoding"] == "utf-8" and result["confidence"] > 0.9:
            print("utf8->gbk")
            decoded_content = content.decode("utf-8").encode("gbk")
            file.seek(0)
            file.truncate()
            file.write(decoded_content)
        else:
            print("编码不符合要求")


def gbk_utf8(file_path):
    with open(file=file_path, mode="r+b") as file:
        content = file.read()
        print("file: " + file_path)
        result = chardet.detect(content)
        print(result)
        if result["encoding"] == "GB2312" and result["confidence"] > 0.9:
            print("gbk->utf8")
            decoded_content = content.decode("gbk").encode("utf-8")
            file.seek(0)
            file.truncate()
            file.write(decoded_content)
        else:
            print("编码不符合要求")


def scan_directory(directory, pattern=r".*\.lrc$"):
    file_list = []
    print("正在读取列表")
    print("————————————————————————————")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                file_list.append("{0}\\{1}".format(root, file))
                print("{0}\\{1}".format(root, file))
    print("————————————————————————————")
    return file_list


if __name__ == "__main__":
    arguments = sys.argv
    print(arguments)
    assert len(arguments) == 3,"参数数量不正确"
    assert arguments[2] == "gbk" or arguments[2] == "utf8","参数内容不正确 只能是 'gbk' 或者 'utf8'"
    for arg in arguments:
        print(arg)
    file_list = scan_directory(arguments[1])
    if arguments[2] == "gbk":
        for path in file_list:
            utf8_gbk(path)
    else:
        for path in file_list:
            gbk_utf8(path)

        
