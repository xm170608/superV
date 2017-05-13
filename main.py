#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
import os
import platform
import datetime
import psutil
import net

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
    _cpu_state = ''
    _cpu_count = psutil.cpu_count(logical = False)
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

def _get_boot_time():
    _boot_time = ''
    _boot_time = '本机启动时间：' + datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    return _boot_time

def _get_server_state():
    _server_state = ''
    _os_version = platform.platform()
    _cpu = platform.processor()

    _server_state = '操作系统： %s ; CPU: %s' %(
        _os_version,
        _cpu)

    return _server_state


def main():
    print()
    print(_get_boot_time())
    print(_get_cpu_state())
    print(_get_memory_state())
    print(_get_disk_state())
    print(net.main())

if __name__ == '__main__':
    main()
