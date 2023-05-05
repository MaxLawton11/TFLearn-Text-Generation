#!/bin/bash
clear
rm model.ckpt-*
python3 Python/Train.py $1
