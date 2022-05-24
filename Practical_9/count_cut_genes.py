# input fa file
# extract gene name
# select the gene that can be cut
# calculate length
# output
x=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all (1).fa')  # input the initial file
y=input('Please type the fasta file name that you want to store selected sequence in: ')    # input the store file
output=open(y,'w')
output1=open('cut1.fa','w') # cut1.fa and cut2.fa are files to store incomplete change
output2=open('cut2.fa','w')
import re
for line in x:
    if line.startswith('>'):    # select gene name
        line=''.join(re.findall(r'gene:(\S+)',line))+'\t'
        output1.write('\n'+'>'+line+'\n')
    else:
        line=line.strip()   # delete \n
        output1.write(''.join(line))
output1.close()
output1=open('cut1.fa','r') # why use cut1.fa and cut2.fa is that if only use output, the open can't write things in a 'w' file
for line in output1:
    if not line.startswith('>'):
        if re.search(r'GAATTC', line):  # find seq that can be cut
            Fn = len(re.findall(r'GAATTC', line)) + 1   # calculate the number of fragments
            output2.write(str(Fn)+'\n'+line)
    else:
        line=line.strip()
        output2.write('\n' + line + '\t')   # modify the look
output2.close()
output2=open('cut2.fa','r')
for line in output2:
    if line.startswith('>'):
        if re.search(r'\t\d',line):
            output.write(''.join(line)) # conserve the gene name that can be cut
        else:
            continue
    else:
        output.write(line)
output.close()  # finish and save


# cut_genes.fa
# Saccharomyces_cerevisiae.R64-1-1.cdna.all (1).fa
