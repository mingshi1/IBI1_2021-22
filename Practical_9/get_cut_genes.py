# read the data
# find the name of genes and extract
# calculate the length of genes
# identify the seq that can be enzyme cut into >1 parts
# output in a fasta--cut_genes.fa
import re
import os
print('os.getcwd()', os.getcwd())   # find where I am
print('os.listdir()', os.listdir()) # find the data name
genes=open('C:/Users/dream/IBI1_2021-22/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all (1).fa','r')   # read the initial file
output=open('C:/Users/dream/IBI1_2021-22/Practical8/cut_genes.fa','w')  # output the changed seq into the cut_genes.fa
output1=open('C:/Users/dream/IBI1_2021-22/Practical8/cut1.fa','w')
output2=open('C:/Users/dream/IBI1_2021-22/Practical8/cut2.fa','w')
#genes.seek(0,0) # define readline from the primal position
for line in genes:
    if line.startswith('>'):    # find the line with name
        l1=re.findall(r'gene(:\S+)',line)   # extract gene name
        output1.write('\n'+''.join(l1)+'\n') # add it into the file
    else:
        l2=line.strip() # remove \n
        output1.write(''.join(l2))   # change into string
output1.close() # without the operation, it will report unsupported error
output1=open('C:/Users/dream/IBI1_2021-22/Practical8/cut1.fa','r')
for l in output1:
    if not l.startswith(':'):
        if re.search('GAATTC',l):   # select the seq needed
            output2.write(str(len(l))+'\n'+l)
    else:
        l4=re.findall(r':(\S+)',l)  # add name
        output2.write('\n'+'>'+''.join(l4)+'\t')
output2.close()
output2=open('C:/Users/dream/IBI1_2021-22/Practical8/cut2.fa','r')
for l in output2:
    if l.startswith('>'):
        if re.search(r'\t[0-9]',l):    # add length
            output.write("".join(l))
        else:
            continue
    else:
        output.write(l)
output2.close()





