#!/bin/bash

# asci escape sequence
# ESC[{attr1};{attr2};.....{attrn}m
# caractere ESC em asci = \033
# em textos
    # attr1 = estilo de fonte (bold, italic, underline, etc)
    # attr2 = cor texto

# Formatação ANSI
NORMAL_TXT='\033[0;37m' # white and normal
TITLE='\033[1;32m'      # green and bold
HIGHLIGHT="\033[0;32m"  # green and normal

# Coleta dados cpu
model=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $5" "$6" "$7" "$8" "$9}' | head -n1`
cores=`cat /proc/cpuinfo | grep -i 'cpu cores' | awk '{print $4}' | head -n 1`
threads=`cat /proc/cpuinfo | grep -i 'model name' | awk '{print $5" "$6" "$7" "$8" "$9}' | wc -l`
cpu_gen=`echo "${model}" | head -n1 | awk '{print $2}' | cut -c 4-4`

# Coleta dados memória
available_mem=`bc <<<"$(cat /proc/meminfo | grep -i memavailable | awk '{print $2}')/1024"`
total_mem=`bc <<<"$(cat /proc/meminfo | grep -i memtotal | awk '{print $2}')/1024"`
swap_total=`bc <<<"$(cat /proc/meminfo | grep -i swaptotal | awk '{print $2}')/1024"`
swap_free=`bc <<<"$(cat /proc/meminfo | grep -i swapfree | awk '{print $2}')/1024"`

# Escreve dados cpu
printf "
${TITLE}CPU

${HIGHLIGHT}Modelo da CPU      ${NORMAL_TXT}------------------ $model
${HIGHLIGHT}Geração            ${NORMAL_TXT}------------------ $cpu_genª geração
${HIGHLIGHT}Qntd de núcleos    ${NORMAL_TXT}------------------ $cores
${HIGHLIGHT}Qntd de threads    ${NORMAL_TXT}------------------ $threads



${TITLE}MEMÓRIA

${HIGHLIGHT}Memória disponível ${NORMAL_TXT}------------------ $available_mem M
${HIGHLIGHT}Memória total      ${NORMAL_TXT}------------------ $total_mem M
${HIGHLIGHT}Swap total         ${NORMAL_TXT}------------------ $swap_total M
${HIGHLIGHT}Swap free          ${NORMAL_TXT}------------------ $swap_free M
"