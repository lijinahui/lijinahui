#!/bin/bash
cd /root/lijianhui/
echo `pwd`
git add -A
git commit -m "$1"
git push 
