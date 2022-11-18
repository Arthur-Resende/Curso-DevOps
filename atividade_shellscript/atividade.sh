#!/bin/bash
cpu_use=(`sar 1 1 | head -n4 | tail -n1 | tr , .`)
cpu_use_total=`bc <<<"${cpu_use[2]} + ${cpu_use[3]} + ${cpu_use[4]}"`
milestone=90
message="Alerta, o uso de cpu da máquina superou ${milestone}%"

if [ ${cpu_use_total%%.*} -gt $milestone ]; then
    echo "Uso do cpu está em ${cpu_use_total}%, superando a marca de ${milestone}, alerta será enviado por email."
    echo "${message}" | mail -s "Alerta" arthurresendefaria@gmail.com
    echo "Email enviado"
    sleep 60
fi