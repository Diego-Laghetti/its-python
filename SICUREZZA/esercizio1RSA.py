m = '00a895bb103dbc054000221bbc61a8c2e35c65e65c4cb42a6ae2062bce34f7a540b44409a724cedf5063da7a5f711014d9adc20a2b5b1f3492ca62231c758b6941a3df00ce23b7c574da1b3ca148d8186c3937769ec62eb53f80a79b8c8ae7e86eef7c2d735ab4fc61aabe83ccf5b3186c2d1bc173be7b169310f4f5ed2d17feb953195d60964fc68007146e09adf12909385ef3cfd3163f77f3aec2cf183e08c4a97d122bf35145c44f748317941e76585d967e92856e696ec329b8daa391f96afaf365dd8849a7551017569853064ab358f49396ff2cbd0ddd5804b022b0cd8e1a2d0f1baa2c31366eb27b6db23521ca64d546bab24b13218c9a63f515e1bf17'

e = 65537

#transformo il modulo in intero 
modint = int(m, 16)

#scrivo un messaggio
messaggio = "laghettodelleur"

#trasformo il messaggio da stringa in esadecimale, e dopo in intero
messint = int(messaggio.encode('utf-8').hex(),16)

#questa funzione cifra il mio messaggio
messcifrato = pow(messint, e, modint)
print(messcifrato)


#esponente privato in esadecimale
privesp = '19c66ac75ce8f65486b0b054e909886282aa01c272e7c8e4769242f85018dce73ba87b6156bb5a614c23073ab86aa105770f87c681341031b147b7de8e0a369996986de3168aee61a3472ec9e9fd401eabd0d30e0b76f0b738d06773e178fb8c9a88fdd9f9305ab6040904d5bd6b187cd198c0c71584743b200893e12357dbd5f23ba2060abe3f0ee782b0a67498a2f61f2ebb7f79748e8df893ee05ae1205801b45d148f9003d42105f9bdd4c472954f653e7d674220665df1827175fc9a11dc969472663501723d4893d32838baa6cd85039ffe7b43b35d026d46e24bca13104c21b19f10f787a842149c852de3cf3e32380dd777fd7cd9ffa9792118b4f61'

#transformo l'esponente privato in intero 
privespint = int(privesp, 16)

#questa funzione decifra il mio messaggio
messdecifrato = pow(messcifrato, privespint, modint)
print(messdecifrato)

#lunghezza in byte, il +7 arrotonda per eccesso, diviso 8 perchè ogni byte è 8 bit
lunghezza = (messdecifrato.bit_length()+7)//8

#trasforma il messaggio cifrato in byte
msgbyte = messdecifrato.to_bytes(lunghezza, 'big')

#trasforma il messaggio da byte in stringa
plaintext = msgbyte.decode('utf-8')
print(plaintext)

