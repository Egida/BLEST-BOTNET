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
git clone https://github.com/G00Dway/BLEST-BOTNET /usr/share/BLEST > /dev/null 2>&1
chmod +x core/bin/blest
cp -r core/bin/blest /usr/bin
mkdir /root/.blest
mkdir /usr/var/blest_bin
apt install python3-pip ruby perl wget curl steghide nmap figlet toilet lolcat xterm zenity -y > /dev/null 2>&1
apt install python-is-python3 -y > /dev/null 2>&1
apt install python2 -y > /dev/null 2>&1
pip install colorama scapy pyinstaller &> pip.log
echo -e "\033[1;32m[+] \033[0mBlest Hazır!, Blest'i açmak için terminalda 'blest' yaz!"
echo '---------------------------------------------------'
echo -e "Discordumuz : \033[1;32mhttps://discord.gg/NE7REnjs2p\033[0m - Blest Boyz"
echo -e "BLEST By    : Blest Boyz"