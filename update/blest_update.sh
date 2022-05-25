echo -e "\033[1;77m[i] \033[0mGüncellemeler kontrol ediliyor..."
cd /usr/share/BLEST
BRANCH="main"
LAST_UPDATE=`git show --no-notes --format=format:"%H" $BRANCH | head -n 1`
LAST_COMMIT=`git show --no-notes --format=format:"%H" origin/$BRANCH | head -n 1`

git remote update > /dev/null 2>&1
if [ $LAST_COMMIT != $LAST_UPDATE ]; then
        echo -e "\033[1;33m[!] \033[0mBLEST Yenileniyor, Interneti açık tutun ve ekranı kapatmayın..."
        python3 /usr/share/BLEST/core/setup/git_setup.py /usr/share/BLEST update
        echo -e "\033[1;32m[+] \033[0mBitirmek için lütfen blest'i kapatıb yeniden açın"
else
        echo -e "\033[1;77m[i] \033[0mYenilenme Yok"
fi