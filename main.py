#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
import os
import time
import psutil

BYTES_2_GB = 1024 ** 3

def _get_memory_state():

    _mem = psutil.virtual_memory()

    _mem_total = _mem.total / BYTES_2_GB
    _mem_percent = _mem.percent
    _mem_used = _mem.used / BYTES_2_GB
    _mem_free = _mem.free / BYTES_2_GB

    _mem_state = '内存： %.2f GB； 已用： %.2f %%  %.2f GB； 未使用： %.2f GB' %(
        _mem_total,
        _mem_percent,
        _mem_used,
        _mem_free)

    return _mem_state

def _get_cpu_state():

    _cpu_count = psutil.cpu_count(logical=False)
    _cpu_count_logical = psutil.cpu_count()
    _cpu_percent = psutil.cpu_percent(1)

    _cpu_state = 'CPU： %d 个； 核心 %d 个； 使用率： %.2f %%' %(_cpu_count, _cpu_count_logical, _cpu_percent)

    return _cpu_state

def _get_disk_state():
    _disk_state = ''
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        _disk_state = _disk_state + '分区： %s 共： %.2f GB； 使用： %.2f GB； 空闲： %.2f GB； 使用率： %.2f %% \n' % (
            part.device,
            usage.total / BYTES_2_GB,
            usage.used / BYTES_2_GB,
            usage.free / BYTES_2_GB,
            usage.percent)

    return _disk_state


def main():
    try:
        _interval = 0
        while True:
            print(_get_cpu_state())
            print(_get_memory_state())
            print(_get_disk_state())
            _interval = 1
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
