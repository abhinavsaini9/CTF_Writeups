# AS3 Turtles
Stego

Given File in the challenge [turtles128.zip](./A3S_turtles/turtles128.zip) is a password protected zip file having recursive zip files.

So I automated the cracking process. Here's the script [Exploit](./A3S_turtles/exploit.sh).

```bash

b=""

while [ 1 ]
do
        file $filename | grep "Zip"
        if [ "$?" -eq "0" ]
        then
                echo "$filename"
                $zip2john $filename > hash
                $john hash
                x=$($john --show hash)
                pass=$(echo $x | cut -d':' -f 2)
                b="$b$pass"
                unzip -P$pass $filename
                rm $filename
                rm hash
                filename=$(ls *)

        fi

        file $filename | grep "PNG"
        if [ "$?" -eq "0" ]
        then
                echo "$b"               
                break
        fi
done

cd ..

```

The password for all the files was 0/1, I could have run just 0/1 on zips but wasn't sure at first so jtr, So I concated all the password in hope to get a binary.

`00111101110010010000011011110110100100101000111011101000100000101100110010110001101110001011110111010001010010101010001001001100`

And we got a png [Key](./A3S_turtles/key.png). So guessing from the challenge name it is pretty obvious it is AES128 Encryption.

Cipher text Hex `3DC906F6928EE882CCB1B8BDD14AA24C`.

Using [CyberChef](https://gchq.github.io/CyberChef/) and the key in ECB mode, decodes Raw text.

`flag{steg0_a3s}` 
