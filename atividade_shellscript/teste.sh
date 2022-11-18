while getopts a:b:c: flag; do
    case "${flag}" in
        a) a="${OPTARG}";echo "${a}";;
        b) b="${OPTARG}";echo "${b}";;
        c) c="${OPTARG}";echo "${c}";;
    esac
done