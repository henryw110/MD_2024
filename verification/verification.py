import xyz_parse
import sys

aminos={
  "ACE":[" H1 "," CH3"," H2 "," H3 "," C  "," O  "],
  "GLH":[" N  "," H  "," CA "," HA "," CB "," HB2"," HB3"," CG "," HG2"," HG3"," CD "," OE1"," OE2"," HE2"," C  "," O  "],
  "NHE":[" N  "," HN1"," HN2"],
  "GLN": [" N  "," H  "," CA "," HA "," CB "," HB2"," HB3"," CG "," HG2"," HG3"," CD "," OE1"," NE2","1HE2","2HE2"," C  "," O  "],
  "HIE": [" N  "," H  "," CA "," HA "," CB "," HB2"," HB3"," CG "," ND1"," CE1"," HE1"," NE2"," HE2"," CD2"," HD2"," C  "," O  "],
  "LEU": [" N  "," H  "," CA "," HA "," CB "," HB2"," HB3"," CG "," HG "," CD1","1HD1","2HD1","3HD1"," CD2","1HD2","2HD2","3HD2"," C  "," O  "],
  "MET":[" N  "," H  "," CA "," HA "," CB "," HB2"," HB3"," CG "," HG2"," HG3"," SD "," CE "," HE1"," HE2"," HE3"," C  "," O  "],
  "PRO":[" N  "," CD "," HD2"," HD3"," CG "," HG2"," HG3"," CB "," HB2"," HB3"," CA "," HA "," C  "," O  "],
  "TYR":[" N  "," H  "," CA "," HA "," CB "," HB2"," HB3"," CG "," CD1"," HD1"," CE1"," HE1"," CZ "," OH "," HH "," CE2"," HE2"," CD2"," HD2"," C  "," O  "],
  "TRP":[" N  "," H  "," CA "," HA "," CB "," HB2"," HB3"," CG "," CD1"," HD1"," NE1"," HE1"," CE2"," CZ2"," HZ2"," CH2"," HH2"," CZ3"," HZ3"," CE3"," HE3"," CD2"," C  "," O  "],
}


def resList (name):
  n=name.split("_")
  n.pop(-1)
  n.insert(0,"ACE")
  n.append("NHE")
  for e in range(len(n)):
    if(n[e]=="HIS"):
      n[e]="HIE"
  ret=[]
  rn=1
  #print (n)
  for res in n:
    t=aminos[res]
    t=list(zip(t,[(res,rn)]*len(t)))
    ret=ret+t
    rn=rn+1
  return ret

s=sys.argv[1]
st=s[0:-4]
l=resList(s)
f=open("./tripeptide/xyz/%s"%s)
f=f.read()
mol = xyz_parse.parse_xyz(f)
z=list(zip(l,mol.molecules[0].atoms))

i=1
o="CRYST1   31.398   34.100   29.273  90.00  90.00  90.00 P 1           1\n"
for v in z:
  s="%.3f  %.3f  %.3f  1.00  0.00\n"%(v[1].x,v[1].y,v[1].z)
  o=o+"ATOM%s%d %s %s     %d      %s"%(" "* (7-len(str(i))),i,v[0][0],v[0][1][0],v[0][1][1],s)
  i=i+1
o=o+"TER\nEND"
f=open("./pdb/%s.pdb"%st,"w")
f.write(o)
f.close()
