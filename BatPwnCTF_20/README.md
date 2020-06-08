# CRfuckPhuck
Miscellaneous

![What is it ](./CRfuckPhuck/CRfuckPhuck.jpg)


We are provided with a file [flag](./CRfuckPhuck/flag) which have no extensions and is corrupted in some sort. After using most of the tools I was not able to find anything. Then we looked at the Hexdump of file and found a file flag.zip and a corrupted png header at the last reversed. ![hex1](./CRfuckPhuck/hex1.jpg) ![hex2](./CRfuckPhuck/hex2.jpg) The whole hex was reveresed using 

	$ <flag xxd -p -c1 | tac | xxd -p -r > reverse 

found the reveresed file [reverse](./CRfuckPhuck/reverse). 
