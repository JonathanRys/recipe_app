#!usr/bin/sh

source env_$ENV.sh

for file in ../config/*.gpg; do
    gpg --decrypt $file --pinentry-mode loopback --passphrase $DECRYPT_PASSWORD > "${file//__/\/}"
done
