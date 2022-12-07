#!/bin/bash

# Coleta dados
available_mem=`bc <<<"$(cat /proc/meminfo | grep -i memavailable | awk '{print $2}')/1024"`
total_mem=`bc <<<"$(cat /proc/meminfo | grep -i memtotal | awk '{print $2}')/1024"`
swap_total=`bc <<<"$(cat /proc/meminfo | grep -i swaptotal | awk '{print $2}')/1024"`
swap_free=`bc <<<"$(cat /proc/meminfo | grep -i swapfree | awk '{print $2}')/1024"`

# Escreve dados
printf "${BOLD}
${WHITE}MEMÓRIA

${GREEN}Memória disponível ${WHITE}------------------------- $available_mem M
${GREEN}Memória total      ${WHITE}------------------------- $total_mem M
${GREEN}Swap total         ${WHITE}------------------------- $swap_total M
${GREEN}Swap free          ${WHITE}------------------------- $swap_free M
\n\n"