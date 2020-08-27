D=input
C=print
import requests as G
def B():
	M='Press enter.';C('\r')
	try:
		E=D('Token > ');H={'Authorization':E,'Content-Type':'application/json'};A=G.get('https://discord.com/api/v6/users/@me',headers=H)
		if A.status_code==200:I=A.json()['username']+'#'+A.json()['discriminator'];J=A.json()['id'];F=A.json()['phone'];K=A.json()['email'];L=A.json()['mfa_enabled'];C(f"""
 ID       : {J}
 Username : {I}
 A2F      : {L}
 Mail    : {K}
 Number   : {F if F else""}
 Token    : {E}

            """);D(M);B()
		else:C(Fore.RED+'Invalid Token'+Fore.RESET);D([M]);B()
	except KeyboardInterrupt:sys.exit()
B()
