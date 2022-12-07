#!/bin/bash

# Formatação ANSI
export WHITE='\033[37m'
export GREEN='\033[32m'
export BOLD='\033[1m'

while getopts mc flag
do
    case "${flag}" in
        m) ./collect_mem_data.sh;;
        c) ./collect_cpu_data.sh;;
    esac
done