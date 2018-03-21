import subprocess
def genKey() :
    p=subprocess.Popen("openssl",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True) #this is for text communication
    result, err = p.communicate(input="genrsa -des3 -out server2.key 1024 \n1234\n1234\n")
    print(result, err)

def genCsr(caKey,reqcsr,passphrase) :
    p = subprocess.Popen("openssl",
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)  # this is for text communication

    input1 = "req -new -key " + caKey + " -sha256 -out " + reqcsr+"\n"
    pp = passphrase + "\n"
    imput2 = input1 + pp + "IN\n"+"Noida\n"+"3CLogic\n"+"3C.com\n"+"abc@3c.com\n"+"IN\n"+"IN3C\n"+"IN3C\n"+"IN3C\n"
    print(imput2)
    result, err = p.communicate(input= imput2)
    print(result, err)
    line =err
    print(line)

def verifyCSR(reqcsr):
    p1 = subprocess.Popen("openssl",
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)  # this is for text communication
    input1 = "req -verify -in " + reqcsr + " -text -noout"
    resut, err = p1.communicate(input1)
    #print(resut,err)
    if(err == "verify OK\n"):
        return 0
    else: return 1

def signCSR(reqcsr,caCert,caKey,days,certName,passPhrase) :
    p2 = subprocess.Popen("openssl",
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)  # this is for text communication
    line = "x509 -req -days " + days + " -in " + reqcsr + " -CA " + caCert + " -CAkey " + caKey + " -CAcreateserial -out " +certName + " -sha256 \n" + passPhrase + "\n"
    print(line)
    resut, err = p2.communicate(input= line)
    line = err.split("\n")
    if (line[0] == "Signature ok"):
        return 0
    else:
        return 1

def verSignedCert(newCert,caKey,passPhrase):
    p3 = subprocess.Popen("openssl",
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)  # this is for text communication
    resut, err = p3.communicate(input="x509 -req -in newkey.csr -CA " + newCert + " -CAkey " + caKey + " -CAcreateserial -out newcert.crt -days 500 \n" +passPhrase +"\n")
    line = err.split("\n")
    if(line[0]=="Signature ok"):
        print(line[0])
        return 0
    else:return 1

