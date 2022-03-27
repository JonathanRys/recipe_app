#!/bin/sh

source /root/scripts/env_$ENV.sh

# Encrypt with
# gpg --batch --yes --passphrase <password> --output $file.gpg -c $file

# decrypt encrypted files
for file in /vagrant/config/*.gpg; do
    decrypted_file="${file//.gpg/}"
    gpg --decrypt $file --pinentry-mode loopback --passphrase $DECRYPT_PASSWORD > $decrypted_file
done

# move files
for file in /vagrant/config/*; do
    if [[$( echo "$file"|grep ".gpg$" ) && $? -eq 0]]; then
        break;
    fi
    
    mv $decrypted_file "${decrypted_file//__/\/}"
done
