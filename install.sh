#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m
echo -e "\033[1;77m[i] \033[0mAPT Keş Temizleniyor..."
apt clean > /dev/null 2>&1
apt autoclean > /dev/null 2>&1
echo -e "\033[1;33m[!] \033[0mGüncellemeler kontrol ediliyor..."
bash src/updates/blest_update.sh
echo -e "\033[1;77m[i] \033[0mBlest yükleniyor... (Arka fon)"
pip install colorama &> colorama.log
python3 core/setup/git_setup.py /usr/share/BLEST install
echo -e "\033[1;77m[i] \033[0mAPT paketler yükleniyor... (Arka fon)"
apt install python3-pip ruby perl wget curl steghide nmap figlet toilet lolcat xterm zenity -y > /dev/null 2>&1
apt install python-is-python3 -y > /dev/null 2>&1
apt install python2 -y > /dev/null 2>&1
pip install colorama scapy pyinstaller &> pip.log
echo -e "\033[1;32m[+] \033[0mBlest Hazır!, Blest'i açmak için terminalda 'blest' yaz!"
echo '---------------------------------------------------'
echo -e "Discordumuz : \033[1;32mhttps://discord.gg/NE7REnjs2p\033[0m - Blest Boyz"
echo -e "BLEST By    : Blest Boyz"