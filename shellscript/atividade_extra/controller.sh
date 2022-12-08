#!/bin/bash

# Formatação ANSI
WHITE='\033[37m'
GREEN='\033[32m'
BOLD='\033[1m'

# Imprime dados formatados
printer() {
    counter=0
    printf "${BOLD}"
    for arg in $@; do
        if [ ${counter} == 1 ]; then
            printf "${GREEN}%-19s" $arg | tr '.' ' '
            counter=2
        elif [ ${counter} == 2 ]; then
            printf "${WHITE}------------------------- $arg\n"  | tr '.' ' '
            counter=1
        else
            printf "${WHITE}$arg\n\n" | tr '.' ' '
            counter=1
        fi
    done
    printf "\n\n"
}

# Controla quais dados serão coletados
while getopts mcdne flag
do
    case "${flag}" in
        m) printer `./collect/mem_data.sh`;;
        c) printer `./collect/cpu_data.sh`;;
        d) printer `./collect/disk_data.sh`;;
        n) printer `./collect/network_data.sh`;;
    esac
done