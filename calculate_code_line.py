# -*- coding: utf-8 -*-
import glob
import time
import os
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count


def cal_line_of_code(file):
    count = 0

    if os.path.isfile(file):
        with open(file, "r", errors="ignore") as fp:
            lines = fp.readlines()
            for line in lines:
                if line.strip() != "":
                    count += 1

    return count


def calculate(pathname_):
    files = glob.iglob(pathname_, recursive=True)
    ret_, cnt = [], 0
    num_of_process = cpu_count()
    with Pool(num_of_process) as pool:
        ret_ = pool.map(cal_line_of_code, files)

    for n in ret_:
        cnt += n

    return len(ret_), cnt


if __name__ == '__main__':
    print(f"main process:{os.getpid()}, cpu_count:{cpu_count()}")

    pathname = ["/Users/admin/Downloads/linux-5.11/**/*",
                "/Users/admin/Downloads/Python-3.9.1/**/*",
                "/Users/admin/Downloads/tensorflow-master/**/*",
                "/Users/admin/Downloads/pytorch-master/**/*"
                ]

    for pn in pathname:
        start = timer()
        num_of_file, num_of_line = calculate(pn)
        end = timer()
        print(f"elapsed time:{round(end - start, 2)}s, num_of_file:{num_of_file}, num_of_line:{num_of_line} for {pn}")
