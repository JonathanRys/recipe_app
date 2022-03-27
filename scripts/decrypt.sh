#!/bin/sh

source /root/scripts/env_$ENV.sh

# Encrypt with
# gpg --batch --yes --passphrase <password> --output $file.gpg -c $file

for file in ../config/*.gpg; do
    gpg --pinentry-mode loopback --passphrase $DECRYPT_PASSWORD --decrypt $file > "${file//__/\/}"
done
