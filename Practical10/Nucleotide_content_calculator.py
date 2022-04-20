# def a function
# change a the seq input to upper cases
# calculate the length of seq and number of A, T, C, G
# return
def Nucleotide_content(seq,type):
    seq=list(seq.upper())  # change into upper cases
    print('The length of sequence is '+str(len(seq)))
    A,T,C,G=0,0,0,0
    for i in range(len(seq)):
        if seq[i]=='A':
            A+=1
        elif seq[i]=='T':
            T+=1
        elif seq[i] == 'C':
            C += 1
        elif seq[i]=='G':
            G+=1    # calculate the content of each base group

    if type == 'A':
        return print('The number of A is {0}. The percentage of A is {1}'.format(str(A), format(A / len(seq),'0%')))
    elif type == 'T':
        return print('The number of T is {0}. The percentage of T is {1}'.format(str(T), format(T/ len(seq),'0%')))
    elif type == 'C':
        return print('The number of C is {0}. The percentage of C is {1}'.format(str(C), format(C/ len(seq),'0%')))
    elif type == 'G':   # count specific content of A/T/C/G
        return print('The number of G is {0}. The percentage of G is {1}'.format(str(G), format(T/ len(seq),'0%')))

### example:
Nucleotide_content('attatgccGTTcGAATTgCCaTga','T')


