import random

class ShamirSecretSharing:



    def SSSEncode(n,t,s):   # Shamir-Secret-Sharing: Geheimnis zerlegen
      # Aufruf: SSSEncode(n,t,s) mit natuerlichen Zahlen n,t,s mit 2<=t<=n
      # Ausgabe: (p,t,y) mit
      #     p = Primzahl > max(n+1,s+1)
      #     t = Wert aus der Eingabe
      #     y = Hashmap der Geheimnisteile y[1],...,y[n]
      ...

    def SSSDecode(p,t,y):   # Shamir-Secret-Sharing: Geheimnis rekonstruieren
      # Aufruf: SSSDecode(p,t,y) mit den von SSSEncode ausgegebenen Zahlen p,t und
      #     y = Hashmap, die mindestens t Werte der von SSSEncode
      #         ausgegebenen Hashmap enthaelt
      # Ausgabe: s = rekonstruiertes Geheimnis
      #
      ...

def SSSTest():  # zum Testen des Shamir-Secret-Sharing
  n=20
  t=17
  s=1234567890
  (p,t,y)=SSSEncode(n,t,s)
  #
  for i in range(0,10):
    s = SSSDecode(p,t,y)
    print("von " + str(20-i) + " Teilnehmern rekonstruiertes Geheimnis: "+str(s))
    del y[i+1]
  return