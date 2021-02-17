#!/bin/sh
cp monitor.py crm
sudo chmod +x crm
cp crm ~/.local/bin/
cp config.py ~/.local/bin/
sudo ln -s ~/.local/bin/crm /bin/
echo "All done!"
read -p "Do you want to delete the cloned folder (Y/n): " ans
if [ "$ans" == 'y' -o "$ans" == '' -o "$and" == 'Y' ]; then
	printf "Deleting the cloned folder\n"
	wd=$(pwd)
	rm -rfv $wd
	cd
else
	printf "You chose not to delete the cloned folder\n"
fi