# Raspberry pi veiledning pi

Last ned Raspberry Pi imager fra nettet til operativ systemet du bruker.

1. Sett inn sd-kortet inni pc-en din
2. Inni imageren, sett inn riktig Raspberry Pi, sett inn Ubuntu på operativ system, og last det ned på sd-kortet. Deretter trykk next.

Nå skal du sette opp Raspberryen ved å bygge den, plugge inn kablene den trengs, også gjøre klar ubuntu til det du ønsker.  
Når du har gjort klart Ubuntu, åpne Terminal med å trykke CRTL + Alt + T, også skriv:

``` console
sudo apt update
sudo apt upgrade
```
Nå skal du ha lasta ned oppdateringer den trenger.

**Sett opp brannmur med UFW:**

``` console
sudo apt install ufw
sudo ufw enable
sudo ufw allow ssh
```
Brannmuren skal være klar når du starter opp pi-en


# SSH
**Gjør klar SSH**
``` console
sudo apt install openssh-server
sudo systemtcl enable ssh
sudo systemctl start ssh
```
**Koble til ssh**  
På din pc, skriv i command prompt:
``` console
ssh brukernavn@ip 
```
Du finner ip adressen din ved å skrive: 
``` console
ip a
```


# Python og Git

**Installer Python, Git og MariaDB:**

``` console
sudo apt install python3-pip
sudo apt install git
sudo mysql_secure_installation
```

# MariaDB
**Sett opp MariaDB:**
``` sql
//Installer MariaDB
sudo apt install mariadb-server
//Logg inn i brukeren "root":
sudo mariadb -u root
//Lag en ny bruker (du kan velge navn og passord selv):
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
//Gi brukeren rettigheter:
GRANT ALL PRIVILEGES ON *.* TO 'username'@’localhost’ IDENTIFIED BY 'password';
//Oppdater rettighetene
FLUSH PRIVILEGES;
```

ok
**Kjør sudo apt update og upgrade igjen**