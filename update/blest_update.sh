cd /usr/share/BLEST
BRANCH="main"
LAST_UPDATE=`git show --no-notes --format=format:"%H" $BRANCH | head -n 1`
LAST_COMMIT=`git show --no-notes --format=format:"%H" origin/$BRANCH | head -n 1`

git remote update > /dev/null 2>&1
if [ $LAST_COMMIT != $LAST_UPDATE ]; then
        echo -e "\033[1;33m[!] \033[0mBLEST Yenileniyor, Ekranı Kapatmayın..."
        rm -rf /usr/share/BLEST
        rm -rf /usr/bin/blest
        git clone https://github.com/G00Dway/BLEST-BOTNET /usr/share/BLEST > /dev/null 2>&1
        chmod +x /usr/share/BLEST/core/bin/blest > /dev/null 2>&1
        cp -r /usr/share/BLEST/core/bin/blest /usr/bin > /dev/null 2>&1
        echo -e "\033[1;32m[+] \033[0mBitirmek için lütfen blest'i kapatıb yeniden açın"
else
        echo -e "\033[1;77m[i] \033[0mYenilenme Yok"
fi