import json
import caauto as ca

with open('csrdata.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    ca.genCsr(distro['caKey'],distro['csrName'],distro['pPhrase'])

    IsSigned = 1
    IsVerified1 = ca.verifyCSR(distro['csrName'])
    if (IsVerified1 == 0):
        IsSigned = ca.signCSR(distro['csrName'],distro['caCert'],distro['caKey'],distro['days'],distro['certName'],distro['pPhrase'])
    if (IsSigned == 0):
        print("certificate signed successfully\n")
    else:
        print("certificate signing failed\n")
    IsValid1 = ca.verSignedCert(distro['certName'],distro['caKey'],distro['pPhrase'])
    if (IsValid1 == 0):
        print("Certificate Generated successfully")
    else:
        print("Certificate Generation failed successfully")
