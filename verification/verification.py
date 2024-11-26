from curses import pair_number
import xyz_parse
aminos={
  "ACE":["H1","CH3","H2","H3","C","O"],
  "GLH":["N","H","CA","HA","CB","HB2","HB3","CG","HG2","HG3","CD","OE1","OE2","HE2","C","O"],
  "NHE":["N","HN1","HN2"],
  "GLN": ["N","H","CA","HA","CB","HB2","HB3","CG","HG2","HG3","CD","OE1","NE2","HE21","HE22","C","D"],
  "HIE": ["N","H","CA","HA","CB","HB2","HB3","CG","ND1","CE1","HE1","NE2","HE2","CD2","HD2","C","O"],
  "LEU": ["N","H","CA","HA","CB","HB2","HB3","CG","HG","CD1","HD11","HD12","HD13","CD2","HD21","HD22","HD23","C","O"]


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
  print (n)
  # for res in n:
  #   t=aminos[res]
  #   t=list(zip(t,[(res,rn)]*len(t)))
  #   ret=ret+t
  #   rn=rn+1
  return ret
s="GLH_HIS_GLH_5.xyz"
l=resList(s)
# f=open("./tripeptide/xyz/GLH_GLH_GLH_1.xyz")
# f=f.read()
# mol = xyz_parse.parse_xyz(f)
# z=list(zip(l,mol.molecules[0].atoms))

# i=1
# o="CRYST1   31.398   34.100   29.273  90.00  90.00  90.00 P 1           1\n"
# for v in z:
#   s="%.3f  %.3f  %.3f  1.00  0.00\n"%(v[1].x,v[1].y,v[1].z)
#   o=o+"ATOM%s%d  %s%s%s     %d      %s"%(" "* (7-len(str(i))),i,v[0][0]," "*(7-len(str(v[0][0]))-len(v[0][1][0])),v[0][1][0],v[0][1][1],s)
#   i=i+1
# o=o+"TER\nEND"
# print(len(o))
# f=open("out.pdb","w")
# f.write(o)
# f.close()

# # mol=mol.parse(f)
# # print(mol.molecules[0].atoms)