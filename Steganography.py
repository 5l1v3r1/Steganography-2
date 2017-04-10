#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import time

cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'
amarelo= '\033[1;33m'
ciano='\033[46m'
magenta='\033[45m'

os.system('clear')

Ban='''

     .--------.
    / .------. \					+=========================================+
   / /        \ \				|      Steganography Picture Toolkit      | 
   | |        | |				+=========================================+
  _| |________| |				| ♚ Coded: @DreadPirateRobertt (Telegram) |
.' |_|        |_| '.	| ♚ Date: 08/04/2017    łuŧЋ1єr           |
'._____ ____ _____.'	| ♚ Chanell:telegram.me/Phantasm_Lab      |
|     .'____'.     |	| ♚ Changing the Description of this tool |
'.__.'.'    '.'.__.'	|   Won't made you the coder ^_^ !!!      |
'.__  | ACRE |  __.'	| ♚ I take no responsibilities for the    |
|   '.'.____.'.'   |	|   Use of this Program!                  |
'.____'.____.'____.'	+=========================================+
'.________________.'
'''

Ban_Help = '''
+===================================================+
|................Steganografia......................|
+===================================================+
  Esteganografia é uma palavra que vem do grego e 
  significa “escrita oculta”. 
  Trata-se do estudo de técnicas que permitam 
  esconder informações dentro de outros arquivos, 
  sejam imagens, músicas, vídeos ou mesmo textos.
+===================================================+

'''


print(cyanClaro +Ban)
print(azul+'   [1] Encrypted')
print('')
print(amarelo + '   [2] Decrypted\n')


def help():
	print(azul+Ban_Help)
try:
  x = sys.argv[1]
  if x == '-h' or x == '--help':
    help()
    print('')
except:
	print ('')

def Stegano():
	file = input(purpleClaro+'[*] Digite o nome ou Diretório da imagem > ')
	f = open(file,
		encoding="ISO-8859-1", mode="a+")
	Top_Secret = input('[*] Text File > ')
	The_Flag_Banner = open(Top_Secret,'r').read()
	f.write(The_Flag_Banner)
	print(verde + '[-] Aguarde Sua Mensagem está sendo Criptografada como String...')
	try:
		byte = f.read(1)
		str =  ""
		while byte != "":
			str = str + byte
			byte = f.read(1)
		print(str)
	finally:
		f.close()
	time.sleep(0.8)	
	print (verde + 'Message Encrypted Sucefull.... [Ok]')

def Decrypt_Flag():
	file = input(purpleClaro + '[*] Digite o nome ou Diretório da imagem > ')
	f = open(file,
		encoding="ISO-8859-1", mode="r")
	try:
		byte = f.read(1)
		str =  ""
		while byte != "":
			str = str + byte
			byte = f.read(1)
		print(str)
		sys.exit(1)
	finally:
		f.close()

def main():
	try:
		output = input(cyanClaro+'Escolha uma opção > ')
		print('')
		if output == '1':
			Stegano()
		elif output == '2':
			Decrypt_Flag()	
		else:
			print(vermelho + '\n\n[*] Exiting...\n')
			time.sleep(0.6)
			sys.exit(1)
	except KeyboardInterrupt:
		print(vermelho + '\n\n[*] Exiting....\n')
		time.sleep(0.6)
		sys.exit(1)

if __name__ == '__main__':
	main()
