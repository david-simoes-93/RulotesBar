# RulotesBar

Simple website for a food truck rental business. Check it out [here](http://94.60.3.235/).

Run with Flask and Python3

    python3 main.py > web.log 2>&1
    
Make it work on reboot:

    sudo nano /etc/rc.local
        export LANG=en_GB.UTF-8
        export LC_ALL=en_GB.UTF-8
        export LC_CTYPE=en_GB.UTF-8
        sudo -u pi -H sh -c "cd /home/pi/RulotesBar; ./run.sh &"
    
Install SMTP server (from [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-14-04) and [here](https://www.linode.com/docs/email/postfix/configure-postfix-to-send-mail-using-gmail-and-google-apps-on-debian-or-ubuntu)):

    sudo apt-get install mailutils libsasl2-modules postfix
    nano /etc/postfix/sasl/sasl_passwd
        [smtp.gmail.com]:587 rulotesbar@gmail.com:mypassword
    sudo postmap /etc/postfix/sasl/sasl_passwd
    sudo chown root:root /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db
    sudo chmod 0600 /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db
    sudo nano /etc/postfix/main.cf
        relayhost = [smtp.gmail.com]:587
        inet_interfaces = localhost
        # Enable SASL authentication
        smtp_sasl_auth_enable = yes
        # Disallow methods that allow anonymous authentication
        smtp_sasl_security_options = noanonymous
        # Location of sasl_passwd
        smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd
        # Enable STARTTLS encryption
        smtp_tls_security_level = encrypt
        # Location of CA certificates
        smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
    sudo service restart postfix
    
