#!/bin/bash

# Formatação ANSI
WHITE='\033[1;37m'
GREEN='\033[1;32m'

# Imprime dados formatados
printer() {
    counter=0
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
    HAS_OPTIONS=1
    case "${flag}" in
        m) printer `./collect/mem_data.sh`;;
        c) printer `./collect/cpu_data.sh`;;
        d) printer `./collect/disk_data.sh`;;
        n) printer `./collect/network_data.sh`;;
    esac
done

if [[ $HAS_OPTIONS != 1 ]]; then
    printer `./collect/mem_data.sh`
    printer `./collect/cpu_data.sh`
    exit 0
fi
