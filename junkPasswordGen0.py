import hashlib
from Crypto.Cipher import AES
import base64

def Hash(password):
	h=hashlib.new('sha256')
	h.update(password)
	return h

def GenPassword(masterKey,website):
	key=Hash(masterKey)
	website=pad(website)
	p = AES.new(key.digest()[0:16],AES.MODE_CBC,key.digest()[16:]).encrypt(website)
	encoded = base64.b64encode(p,"_@")
	encoded=encoded[0:14]	#some sites have max 16 chars, two left aside for spec char and num
	if encoded.isalpha():
		encoded+='1'
	if ('_' not in encoded and '@' not in encoded):
		encoded+='_'
	return encoded

def pad(name):
	N=len(name)%16
	return name + '0'* (16-N)

def inputProcedure():
	masterKey=raw_input("please enter you secret phrase>")
	website=raw_input("Enter the website>")
	p1=GenPassword(masterKey,website)
	print "This is your password for ",website,":\n",p1

if __name__ == "__main__":
	inputProcedure()
