rm -rf temp-papirus
git clone --depth=1 https://github.com/PiSupply/PaPiRus.git temp-papirus
cp -r temp-papirus/papirus/ ./papirus
rm -rf temp-papirus
rm -rf papirus/.git