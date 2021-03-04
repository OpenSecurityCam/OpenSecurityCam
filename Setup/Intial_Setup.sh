echo "Installing OpenSecurityCam"

echo "Installing Python"
sudo apt install python3

echo "Installing MariaDB"
sudo apt install mariadb

echo "Configuring MariaDB. Please remember your root password"
mysql_secure_installation

echo "Creating the database"
read -sp "Type the current root password for MySQL: " rootpass
echo
read -p "MySQL Username for new user: " SQLUname
echo
read -sp "MySQL Password for new user: " SQLPass
echo
mysql -u root -p$rootpass -e "CREATE TABLE IF NOT EXISTS opensecuritycam;CREATE USER '$SQLUname'@'localhost' IDENTIFIED BY '$SQLPass'; GRANT DELETE,INSERT,SELECT ON opensecuritycam.* TO '$SQLUname'@'localhost';FLUSH PRIVILEGES;"

read -p "Type in your Pi local IP Address: " ipaddr
echo -e "SERVER_NAME=$ipaddr:80" >> Entities/config.cfg



echo "Installing the project's requirements"
sudo pip3 install -r Entities/requirements.txt

sudo python3 Entities/CreateFirstUser.py



