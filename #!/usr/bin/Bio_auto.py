#!/usr/bin/python3

import os
from sys import argv
from subprocess import Popen, PIPE
from Bio.SeqIO import convert

print("WARNING! This script only uses default settings.")

#conversion
inp = str(input("Provide file name: "))
inp_form = str.lower( input("Provide file format: "))
out = str(input("Provide output name: "))
out_form = str.lower(input("Provide desired output's format: "))

convert(inp, inp_form, out, out_form)

print("Procedure done. File", out, "was created.")

#distance matrix creator
print("Creation of the distance matrix started.")
suppressed = open(os.devnull, 'w')
protdist = Popen(['phylip', 'protdist'], stdin = PIPE, stdout = suppressed)
inp = input(str("Enter input name: "))
protdist.communicate((inp + "\ny\n").encode())
out = input(str("Enter output name: "))
os.rename('outfile', out)
print(out, "file was created")

#Neighbor joining method
print("Neighbor joining method program")
nj = Popen(['phylip', 'neighbor'], stdin = PIPE, stdout = suppressed)
inp_nj = input(str("Enter input name: "))
nj.communicate((inp_nj + "\ny\n").encode())
out_nj_f = input(str("Provide name for outfile: "))
out_nj_t = input(str("Provide name for tree file: "))
os.rename('outfile', out_nj_f)
os.rename('outtree', out_nj_t)
print(out_nj_f, out_nj_t, "files were created.")

#Maximum Parsimony method
print("Maximum parsimony program")
mp = Popen(['phylip', 'protpars'], stdin = PIPE, stdout = suppressed)
inp_mp = input(str("Enter input name: "))
mp.communicate((inp_mp + "\ny\n").encode())
out_mp_f = input(str("Enter name for outfile: "))
out_mp_t = input(str("Enter name for tree file: "))
os.rename("outfile", out_mp_f)
os.rename("outtree", out_mp_t)
print(out_mp_f, out_mp_t, "files were created.")

#Maximum Likelyhood method
print("Maximum likelyhood program")
ml = Popen(['phylip', 'proml'], stdin = PIPE, stdout = suppressed)
inp_ml = input(str("Enter input name: "))
ml.communicate((inp_mp + "\ny\n").encode())
out_ml_f = input(str("Enter name for outfile: "))
out_ml_t = input(str("Enter name for tree file: "))
os.rename("outfile", out_ml_f)
os.rename("outtree", out_ml_t)
print(out_mp_f, out_mp_t, "files were created.")

print("All files were created. Procedure done.")
suppressed.close()
