#!/bin/bash
# to-do
# [ ] permitir coleta de dados de memória
# [x] permitir o envio de dados a outro email e outro milestone, recebido por argumento
# [x] criar inputs que determinam milestone e email caso parâmetros não sejam recebidos

email=arthurresendefaria@gmail.com
limit=90

while getopts e:l: flag
do
    case "${flag}" in
        e) email="${OPTARG}";;
        l) limit="${OPTARG}";;
    esac
done

while true; do
    cpu_use=(`sar 1 1 | head -n4 | tail -n1 | tr , .`)
    cpu_use_total=`bc <<<"${cpu_use[2]} + ${cpu_use[3]} + ${cpu_use[4]}"`

    if [ ${cpu_use_total%%.*} -gt $limit ]; then
        echo "Uso do cpu está em ${cpu_use_total}%, superando a marca de ${limit}%, alerta será enviado por email para ${email}."
        echo "Alerta, o uso de cpu da máquina superou ${limit}%" | mail -s "Alerta" "${email}"
        echo "Email enviado"
        sleep 60
    fi
done