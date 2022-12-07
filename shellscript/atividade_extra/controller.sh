#!/bin/bash

# Formatação ANSI
export WHITE='\033[37m'
export GREEN='\033[32m'
export BOLD='\033[1m'

while getopts mcd flag
do
    case "${flag}" in
        m) ./mem_data.sh;;
        c) ./cpu_data.sh;;
        d) ./disk_data.sh;;
    esac
done