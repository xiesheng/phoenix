# -*- coding: utf-8 -*-
import glob
from timeit import default_timer as timer


class CalculationResult:
    def __init__(self):
        self.file_num = 0
        self.line_num = 0

    def increase_file_num(self):
        self.file_num += 1

    def increase_line_num(self):
        self.line_num += 1


def calculate(pathname, result_):
    start = timer()
    for file in glob.iglob(pathname, recursive=True):
        result_.increase_file_num()
        with open(file, "r", errors="ignore") as fp:
            lines = fp.readlines()
            for line in lines:
                if line.strip() != "":
                    result_.increase_line_num()

    end = timer()
    print(f"num_of_file:{result_.file_num}, num_of_line:{result_.line_num}")
    print(f'calculate {pathname} - elapsed time: {end - start}')


if __name__ == '__main__':
    path_name = "/Users/admin/linux-5.11/**/*.c"
    result = CalculationResult()
    calculate(path_name, result)

