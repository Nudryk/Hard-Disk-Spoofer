@echo off

py -m ensurepip --upgrade
py -3 -m pip install -U asyncio

cd..
cd..
cd HardDiskSpoofer-main
cd not_touch
start main.py




