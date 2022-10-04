import sys
Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx,Gy) 

def modinv(a,n=Pcurve): 
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high//low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n

def ECadd(a): 
    LamAdd = ((GPoint[1]-a[1]) * modinv(GPoint[0]-a[0],Pcurve)) % Pcurve
    x = (LamAdd*LamAdd-a[0]-GPoint[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def ECdouble(a): 
    Lam = ((3*a[0]*a[0]) * modinv((2*a[1]),Pcurve)) % Pcurve
    x = (Lam*Lam-2*a[0]) % Pcurve
    y = (Lam*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def EccMultiply(GenPoint,ScalarHex): 
    if ScalarHex == 0 or ScalarHex >= N: raise Exception("Invalid Scalar/Private Key")
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint

    for i in range (1, len(ScalarBin)): 
    
        Q=ECdouble(Q); 
        if ScalarBin[i] == "1":
            Q=ECadd(Q); 
    return (Q)

print("******* Starting hunter *********"); 

# pubtype = sys.argv[1].lower()
ranli =str(sys.argv[1]).split(":")
start_range = int(ranli[0],16)
end_range = int(ranli[1],16)
# if pubtype == c or pubtype == compressed or pubtype == comp:
#     target = sys.argv[3][2:]
# elif pubtype == u or pubtype == uncompressed or pubtype == uncomp:
target = int(sys.argv[2][2:66],16)
trace = 0
speed  =0
finaltrace = end_range-start_range

p = EccMultiply(GPoint,start_range)
print("Hunter started and running ------>")
while True:
    p = ECadd(p)
    trace+=1
    # if trace%1000000==0:
    #     print(f"Total keys checked: {trace}")
    if p[0] == target:
        break
if p[0] == target:
    print("Hit!! Wrote into CHEST.txt")
    with open("CHEST.txt", "w") as storage:
        storage.write(f"{str(trace)} Keys from start range\n")
        storage.write(hex(trace+int(start_range)))


    
