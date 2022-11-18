#!/bin/bash
email=arthurresendefaria@gmail.com
limit=90

while getopts e:l:h flag
do
    case "${flag}" in
        e) email="${OPTARG}";;
        l) limit="${OPTARG}";;
        h) cat /home/arthur/Curso-DevOps/atividade_shellscript/help && exit 0;;
    esac
done

while true; do
    cpu_use_raw=(`sar 1 1 | head -n4 | tail -n1 | tr , .`)
    cpu_use_float=`bc <<<"100 - ${cpu_use_raw[7]}"`
    cpu_use="${cpu_use_float%%.*}"

    if [ $cpu_use -gt $limit ]; then
        echo "Uso do cpu está em ${cpu_use}%, superando a marca de ${limit}%, alerta será enviado por email para ${email}."
        echo "Alerta, o uso de cpu da máquina superou ${limit}%" | mail -s "Alerta" "${email}"
        echo "Email enviado"
        sleep 60
    fi
done