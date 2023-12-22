#!/bin/bash

function menu(){
clear
clear
echo -e "\033[92;1m________________________________\033[0m"
echo -e "\033[1;96m         LT PROJECT \033[0m"
echo -e "\033[92;1m________________________________\033[0m"
echo ""
echo -e "\033[93[1] menu enc  dec \033[0m"
echo -e ""
read -p "pilih >>   " vc
case $vc in
1) clear ; wget -q  https://raw.githubusercontent.com/anubhavanonymous/Bash_Frustator/main/frustator.py && chmod +x frustator.py
python2 frustator.py ;;
*) exit 
;;
esac
}
clear
echo -e "\033[92;1m________________________________\033[0m"
echo -e "\033[1;96m         LT PROJECT \033[0m"
echo -e "\033[92;1m________________________________\033[0m"
echo ""
echo -e "\033[93[1] menu enc  dec \033[0m"
echo -e "\033[93[2] Back To Menu \033[0m"

echo -e ""
read -p "pilih >>   " vc
case $vc in
1) clear ; wget -q  https://raw.githubusercontent.com/anubhavanonymous/Bash_Frustator/main/frustator.py && chmod +x frustator.py
python2 frustator.py ;;
2) clear ; menu ;;
*) exit 
;;
esac
