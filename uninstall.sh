#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m
echo -e "\033[1;77m[i] \033[0mAPT Keş Temizleniyor..."
apt clean > /dev/null 2>&1
apt autoclean > /dev/null 2>&1
echo -e "\033[1;33m[!] \033[0mBlest siliniyor..."
rm -rf /usr/share/BLEST
rm -rf /usr/bin/blest
sleep 1
rm -rf /root/.blest
rm -rf /usr/var/blest_trash
echo -e "\033[1;34m[*] \033[0mBlest'i Kullandığınız İçin Teşekkür Ediyoruz :)"