#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# mkfifo ./hogepipe
# < ./hogepipe awk '{printf("!%d\n", $1)}' &
# CMDSS=$(history -m '*ls*' 14000 \
# | tee ./hogepipe \
# | awk '{for(i=2;i<NF;i++){printf("%s ",$i)} print $NF}')
# rm ./hogepipe

import sys
import io


def print_help(text):
    print("Usage: python3 {} text".format(text))


def check_arg():
    argvs = sys.argv
    argc = len(argvs)
    filename = argvs[0]
    if argc < 2:
        print_help(filename)
        quit()
    else:
        return argvs


def main():
    argvs = check_arg()

    histline = argvs[1]
    print(histline)
    exit()


# for script
if __name__ == '__main__':
    main()
