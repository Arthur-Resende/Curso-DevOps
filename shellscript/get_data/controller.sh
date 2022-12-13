#!/bin/bash

# Formatação ANSI e diretório base
WHITE='\033[1;37m'
GREEN='\033[1;32m'
BASE_DIR='/home/tatiane/Curso-DevOps/shellscript/get_data/collect'

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
            printf "\n${WHITE}$arg\n\n" | tr '.' ' '
            counter=1
        fi
    done
    printf "\n"
}

# Controla quais dados serão coletados
while getopts mcsn flag
do
    HAS_OPTIONS=1
    case "${flag}" in
        m) printer `${BASE_DIR}/mem_data.sh`;;
        c) printer `${BASE_DIR}/cpu_data.sh`;;
        s) printer `${BASE_DIR}/disk_data.sh`;;
        n) printer `${BASE_DIR}/network_data.sh`;;
    esac
done

if [[ $HAS_OPTIONS != 1 ]]; then
    printer `${BASE_DIR}/mem_data.sh`
    printer `${BASE_DIR}/cpu_data.sh`
    exit 0
fi
