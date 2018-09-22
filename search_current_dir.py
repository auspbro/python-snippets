#!/usr/bin/env python
# coding: utf-8

'''
search keyword from current directory and sub-directory.
'''

__author__ = 'Xiang Xue'
__version__ = '1.0'

import os
import sys
import getopt
from colorama import init, Fore, Back

init(autoreset=True)


class Colored(object):

    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.RED + s + Fore.RESET

    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    #  前景色:黄色  背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    #  前景色:蓝色  背景色:默认
    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET

    #  前景色:洋红色  背景色:默认
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    #  前景色:青色  背景色:默认
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    #  前景色:白色  背景色:默认
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    #  前景色:黑色  背景色:默认
    def black(self, s):
        return Fore.BLACK

    #  前景色:白色  背景色:绿色
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET

    #  前景色:黄色  背景色:白色
    def yellow_white(self, s):
        return Fore.YELLOW + Back.WHITE + s + Fore.RESET + Back.RESET


color = Colored()


def args_chk():
    if len(sys.argv) == 2:
        pass
    else:
        print color.yellow("========================================================")
        print color.yellow(" Warnning: Please input 2 arguments!")
        print color.yellow(" Usage: Python xxx.py keyword")
        print color.yellow(" e.g.: Python search_current_dir.py test")
        print color.yellow("========================================================")
        exit()


opts, args = getopt.getopt(sys.argv[1:], '-h-f:-v', ['help', 'filename=', 'version'])
for opt_name, opt_value in opts:
    if opt_name in ('-h', '--help'):
        print("[*] Help info")
        print color.yellow("========================================================")
        print color.yellow(" Warnning: Please input 2 arguments!")
        print color.yellow(" Usage: Python xxx.py keyword")
        print color.yellow(" e.g.: Python search_current_dir.py test")
        print color.yellow("========================================================")
        exit()
    if opt_name in ('-v', '--version'):
        print("[*] Version is 1.0 ")
        exit()
    if opt_name in ('-f', '--filename'):
        fileName = opt_value
        print("[*] Filename is ", fileName)
        # do something
        exit()


def search_keyword(keyword, dir):
    list = os.listdir(dir)
    for line in list:
        newline = os.path.join(dir, line)
        if os.path.isdir(newline):
            search_keyword(keyword, newline)
        else:
            if keyword in newline:
                print newline


if __name__ == '__main__':
    args_chk()
    keyword = sys.argv[1]
    dir = os.getcwd()
    search_keyword(keyword, dir)
