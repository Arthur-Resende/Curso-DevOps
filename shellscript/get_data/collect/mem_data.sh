#!/bin/bash

# Coleta dados
available_mem=`bc <<<"$(cat /proc/meminfo | grep -i memavailable | awk '{print $2}')/1024"`
total_mem=`bc <<<"$(cat /proc/meminfo | grep -i memtotal | awk '{print $2}')/1024"`
swap_total=`bc <<<"$(cat /proc/meminfo | grep -i swaptotal | awk '{print $2}')/1024"`
swap_free=`bc <<<"$(cat /proc/meminfo | grep -i swapfree | awk '{print $2}')/1024"`

# Envia dados
printf "MEMORIA Memoria.disponivel $available_mem.M Memoria.total $total_mem.M Swap.total $swap_total.M Swap.free $swap_free.M"