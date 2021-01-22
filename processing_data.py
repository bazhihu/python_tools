#!/usr/bin/python
# -*- coding: utf8 -*-

# 接收两个文件名
# 第一个文件名 待处理文件
# 第二个文件名 处理后文件

import getopt
import sys
import re
import csv
import html


def initialization(argv):
    input_file = ''
    output_file = ''

    if len(argv) < 1:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt == '':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit(2)

    print('输入的文件为：', input_file)
    print('输出的文件为：', output_file)

    return [input_file, output_file]


def open_file(input_file, output_file):
    with open("./" + input_file, "r") as file:
        for line in file.readlines():
            try:
                new_line = run(line)
                write_txt(output_file, new_line)
            except ValueError:
                print("异常")
                pass


def write_file(output_file, list):
    with open(output_file, 'a+') as file:
        spam_writer = csv.writer(file, dialect='excel')
        spam_writer.writerow(list)
    return


def write_txt(output_file, list):
    fo = open(output_file, "a+")
    fo.write(list)
    fo.write('\r\n')


def run(line):
    new_line = line

    # 去除特殊标签
    new_line = html.unescape(new_line)

    # 特殊字符
    new_line = new_line.replace("↓", " ")
    new_line = new_line.replace("①", "1、")
    new_line = new_line.replace("②", "2、")
    new_line = new_line.replace("③", "3、")
    new_line = new_line.replace("④", "4、")
    new_line = new_line.replace("⑤", "5、")
    new_line = new_line.replace("⑥", "6、")
    new_line = new_line.replace('，', ',')
    new_line = new_line.replace('。', '.')
    new_line = new_line.replace('：', ':')
    new_line = new_line.replace('“', '"')
    new_line = new_line.replace('”', '"')
    new_line = new_line.replace('【', '[')
    new_line = new_line.replace('】', ']')
    new_line = new_line.replace('《', '<')
    new_line = new_line.replace('》', '>')
    new_line = new_line.replace('？', '?')
    new_line = new_line.replace('；', ':')
    new_line = new_line.replace('、', ',')
    new_line = new_line.replace('（', '(')
    new_line = new_line.replace('）', ')')
    new_line = new_line.replace('‘', "'")
    new_line = new_line.replace('’', "'")
    new_line = new_line.replace('’', "'")
    new_line = new_line.replace('『', "[")
    new_line = new_line.replace('』', "]")
    new_line = new_line.replace('「', "[")
    new_line = new_line.replace('」', "]")
    new_line = new_line.replace('﹃', "[")
    new_line = new_line.replace('﹄', "]")
    new_line = new_line.replace('〔', "{")
    new_line = new_line.replace('〕', "}")
    new_line = new_line.replace('—', "-")
    new_line = new_line.replace('·', ".")

    # 清理标签
    new_line = re.sub(r'(\[img\](.*?)\[\/img\])|(\[video\](.*?)\[\/video\])|\{u.*?u\}|(\[\/?[a-z](.*?)\])|(\<\/?[a-z].*?>)', "", new_line)

    # 移除空格
    i = 0
    while i < 1000:
        new_line = new_line.replace("  ", " ")
        i = i + 1

    print("line:" + new_line)
    return new_line.strip()


if __name__ == "__main__":
    input_file, output_file = initialization(sys.argv[1:])
    open_file(input_file, output_file)
