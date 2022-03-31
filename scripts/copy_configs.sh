# copy decrypted config files
for file in /vagrant/config/*; do
    # ignore encrypted files
    if [[$( echo "$file"|grep ".gpg$" ) && $? -eq 0]]; then
        break;
    fi
    
    cp $file "${file//__/\/}"
done
