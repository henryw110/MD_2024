from parmed.amber import LoadParm
from parmed.parameters import ParameterSet
from parmed.tools.actions import printDihedrals,printAngles,printBonds

import sys

print(sys.argv)

inputParms=sys.argv[1]
inputCoords=sys.argv[2]
outputFile=sys.argv[3]
c=LoadParm(inputParms,inputCoords)
c.load_pointers()
p=ParameterSet.from_structure(c)
clist=c.coordinates.tolist()

lj_dict=dict(map(lambda a:(a[1],(lambda b:{"nb_idx":a[1],"mass":b.mass,"epsilon":b.epsilon,"sigma":b.sigma})(p.atom_types[a[0]])),c.LJ_types.items()))

atoms_list=[l for l in list(map(lambda a:(list(map(lambda b:dict([("nb_idx",b.nb_idx),("idx",b.idx),("charge",b.charge),("residue",a.name),("name",b.name),("coords",clist[b.idx])]),a))),c.residues)) for l in l]

bond_types=list(map(lambda a:{"idx":a.idx,"r0":a.req,"k":a.k},c.bond_types))
bonds_list=list(map(lambda a:{"type":a.type.idx,"a1_name":a.atom1.name,"a2_name":a.atom2.name,"a1":a.atom1.idx,"a2":a.atom2.idx},c.bonds))

angle_types=list(map(lambda a:{"idx":a.idx,"teq":a.utheteq._value,"k":a.uk._value},c.angle_types))

angles_list=list(map(lambda a:{"a1":a.atom1.idx,"a1_name":a.atom1.name,"a2":a.atom2.idx,"a2_name":a.atom2.name,"a3":a.atom3.idx,"a3_name":a.atom3.name,"type":a.type.idx},c.angles))

dih =[]
for a in c.dihedrals:
  def extract(b):
    if(len(dih)==0 or((b.atom1,b.atom2,b.atom3,b.atom4)!=(dih[-1][-1].atom1,dih[-1][-1].atom2,dih[-1][-1].atom3,dih[-1][-1].atom4))):
      dih.append([b])
    else:
      dih[-1].append(b)
  extract(a)
dih_dict={}
dict2={}
for a in dih:
  t=(a[0].atom1.idx,a[0].atom2.idx,a[0].atom3.idx,a[0].atom4.idx)
  dih_dict[t]=list(map(lambda b:[b.type.idx,b.type.per,b.type.phi_k,b.type.phase],a))
for a in dih_dict.values():
  t=tuple(map(lambda b:b[0],a))
  t2=list(map(lambda b:b[1:],a))
  dict2[t]=t2
for a in dih_dict.keys():
  t=tuple(map(lambda b:b[0],dih_dict[a]))
  dih_dict[a]=t
i=0
for a in dict2.keys():
  i=i+1
  dict2[a]=[i,len(dict2[a])]+dict2[a]

T_DIHEDRAL_COUNT=i

ATOMS_COUNT=((atoms_list[-1]["idx"])+1)
BONDS_COUNT=len(bonds_list)
ANGLES_COUNT=len(angles_list)
DIHEDRAL_COUNT=len(dih_dict.keys())

T_ATOMS_COUNT=(len(lj_dict.keys()))
T_BONDS_COUNT=len(bond_types)
T_ANGLES_COUNT=len(angle_types)



strs=""
strs=["LAMMPS Description\n\n"]
strs.append("%d atoms\n"%(ATOMS_COUNT))
strs.append("%d bonds\n"%(BONDS_COUNT))
strs.append("%d angles\n"%(ANGLES_COUNT))
strs.append("%d dihedrals\n"%(DIHEDRAL_COUNT))
strs.append("%d impropers\n\n"%(0))
strs.append("%d atom types\n"%(T_ATOMS_COUNT))
strs.append("%d bond types\n"%(T_BONDS_COUNT))
strs.append("%d angle types\n"%(T_ANGLES_COUNT))
strs.append("%d dihedral types\n"%(T_DIHEDRAL_COUNT))
strs.append("%d improper types\n\n"%(0))
strs.append("0. %f xlo xhi \n"%(1.0*c.box[0]))
strs.append("0. %f ylo yhi \n"%(1.0*c.box[1]))
strs.append("0. %f zlo zhi \n\n"%(1.0*c.box[2]))
strs.append("Masses\n\n")

i=0
j=1
for a in lj_dict.values():
  i=i+1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  strs.append("%d %f\n"%(a["nb_idx"],a["mass"]))

i=0
j=j+1
strs.append("\nPair Coeffs\n\n")

for a in lj_dict.values():
  i=i+1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  strs.append("%d %f %f %f %f\n"%(a["nb_idx"],a["epsilon"],a["sigma"],a["epsilon"],a["sigma"]))

j+=1
i=0

strs.append("\nBond Coeffs\n\n")

for a in bond_types:
  i+=1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  strs.append("%d %f %f\n"%((a["idx"]+1),a["k"],a["r0"]))

j+=1
i=0

strs.append("\nAngle Coeffs\n\n")
for a in angle_types:
  i+=1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  strs.append("%d %f %f\n"%((a["idx"]+1),a["k"],a["teq"]))

j+=1
i=0

strs.append("\nDihedral Coeffs\n")
for a in dict2.values():
  i+=1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  di_idx=a[0]
  di_len=a[1]
  fourier="\n%d %d"%(di_idx,di_len)
  for b in a[2:]:
    fourier=fourier+(" %f %d %f"%(b[1],b[0],b[2]))
  strs.append(fourier)

j+=1
i=0
mc=1

strs.append("\n\nAtoms\n\n")
for a in atoms_list:
  i+=1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  a_idx=(a["idx"]+1)
  lj_idx=a["nb_idx"]
  a_res=a["residue"]
  mol=1
  if(a_res=="WAT"):
    mol=mc
    if(lj_idx==18):
      mc+=1
  q=a["charge"]
  print(a)
  co=a["coords"]
  na=a["name"]
  s="%d %d %d %f %f %f %f # %s %s\n"%(a_idx,mol,lj_idx,q,co[0],co[1],co[2],na,a_res)
  strs.append(s)

j+=1
i=0

strs.append("\nBonds\n\n")
for a in bonds_list:
  i+=1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  b_t=(a["type"]+1)
  a1_idx=(a["a1"]+1)
  a2_idx=(a["a2"]+1)
  s="%d %d %d %d # %s %s\n"%(i,b_t,a1_idx,a2_idx,a["a1_name"],a["a2_name"])
  strs.append(s)

j+=1
i=0

strs.append("\n\nAngles\n\n")
for a in angles_list:
  i+=1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  b_t=(a["type"]+1)
  a1_idx=(a["a1"]+1)
  a2_idx=(a["a2"]+1)
  a3_idx=(a["a3"]+1)
  s="%d %d %d %d %d # %s %s %s\n"%(i,b_t,a1_idx,a2_idx,a3_idx,a["a1_name"],a["a2_name"],a["a3_name"])
  strs.append(s)

j+=1
i=0

strs.append("\n\nDihedrals\n\n")
for a in dih_dict.keys():
  i+=1
  if(i%100==0):
    print("\n %d | %d\n"%(j,i))
  t=dih_dict[a]
  t2=dict2[t]
  dih_idx=t2[0]
  a1=a[0]+1
  a2=a[1]+1
  a3=a[2]+1
  a4=a[3]+1
  s="%d %d %d %d %d %d\n"%(i,dih_idx,a1,a2,a3,a4)
  strs.append(s)

fin="".join(strs)
print(c.box)
f=open(outputFile,"w")
f.write(fin)
f.close
