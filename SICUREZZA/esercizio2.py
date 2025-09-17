M = "ciao"
Mi = int(M.encode("utf-8").hex(), 16)
print("Messaggio in intero (Mi)", Mi)

n = (
    "009055d79d51b01b527b11fd2d10ddb481aacbe95ca7dde3dab9a36f17ee"
    "9434b2f76fd415b087b0952e65dc4ac59093dc9fe25e9b2d9f7584b35e0d"
    "640d7dc1563ec306aa7b061b01a6dff691f38b0b8db8e2caa14a2d571019"
    "ceba4bb5613110ac7854eebe898996d4a3e6472cd9caa6f12adeb31f0a9f"
    "ead8e50c2844e93f335bc1c305e1a5480571ff050f47b129241f870ef9c9"
    "7bd548ec36ebe13f7ed080ca4b0239d56c5b81edc37227681c53ea5d812c"
    "6c34535910453d8ef25eb12322723ff7c8045564a821240547bf493776a3"
    "f287d44c7c2a598fc917b9c3117c4478aab4a2bdde23aba51226f45ba6fe"
    "1164e136e414e5fdcfe5e2bfd9ba09f1f1"
)

e = 3
decimale = int(n, 16)

C = pow(Mi, e, decimale)
print("Messaggio cifrato (C)", C)

mp = (
    "060393a68e1201236fcb6a8c8b5e92"
    "3011c87f0e86fe94291d1179f6549b"
    "82321fa4a8d63cb0520637443e831d"
    "90b0d3dbfec3f121e6a4e58779408e"
    "d5e53d6397f2caf1c5204120119eaa"
    "4614d075d0925ec871631738f60113"
    "47c3278eb760b1da58df47f065bb9e"
    "317eeda1de68719f61c94776a07154"
    "73b435d702df0d4cbe787a7daccfad"
    "d3107da96c64e82782665d38d21c17"
    "10c34d7f3abfb0b91df590bdbd9e68"
    "7f1b57badccdd6bc0e3bdac71645a7"
    "2d50f134752134107801b5f9ea8562"
    "f118a851d5efc183c142bbe5276d19"
    "f12126a3fb65eb3cae9b1adf848e7a"
    "6ad97190aba9949a1d1bcf99e61f3d"
    "8f783fa07e2a2a40d197f29ebf4323"
    "eb" 
)
decimale1 = int(mp, 16)
print(decimale1)

 
