# Read Seq1, Seq2
# Read BLOSUM62 matrix
# For each aa[i]. Find score and add it to a new vector. Sum scores
# Print Seq1 name/sequence
# Optional: Print alignment
# Print Seq2 name/sequence
# Print Scores
import re
import numpy as np
def readline(i):    # Read Seq1, Seq2
    seq=open(i)
    for line in seq:
        if not line.startswith('>'):
            j=line
    return j
s1=readline('DLX5_human.fa').strip()
s2=readline('DLX5_mouse.fa').strip()
s3=readline('RandomSeq.fa').strip()
def BLOSUM62_dic(): # Read BLOSUM62 matrix
    dic={'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19,'B':20,'Z':21,'X':22,'*':23}
    return dic
dic=BLOSUM62_dic()

def BLOSUM62_grade():
    grade=np.matrix([[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,0,-4],
                     [-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0,-1,-4],
                     [-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0,-1,-4],
                     [-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1,-1,-4],
                     [0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3,-2,-4],
                     [-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3,-1,-4],
                     [-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
                     [0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2,-1,-4],
                     [-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0,-1,-4],
                     [-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3,-1,-4],
                     [-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3,-1,-4],
                     [-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1,-1,-4],
                     [-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1,-1,-4],
                     [-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3,-1,-4],
                     [-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1,-2,-4],
                     [1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0,0,-4,],
                     [0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,0,-4],
                     [-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3,-2,-4],
                     [-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2,-1,-4],
                     [0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2,-1,-4],
                     [-2,-1,3,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1,-1,-4],
                     [-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
                     [0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1,-1,-4],
                     [-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]]) # The matrix's raw data is obtained from https://github.com/Raha-Kheirinia/BLOSUM62, the raw data describes the BLOSUM62 table's data
    return grade
grade=BLOSUM62_grade()
def getContent(a,b):  # find content and alignment
    global content
    global alignment
    l=0
    alignment=''
    for i in range(len(a)):
        if a[i]==b[i]:
            l+=1
            alignment+=a[i]
        elif grade[dic[a[i]],dic[b[1]]]>0:
            alignment += '+'
        else:
            alignment+=' '
    content=l/len(a)
    content = content* 100
    content = str('%.2f' % content) + '%'
    print('Their similarity is ',content)
    print(a)
    print(alignment)
    return b

def getGrade(a,b):  # For each aa[i]. Find score and add it to a new vector. Sum scores
    global score
    score=0
    a=list(a)
    b=list(b)
    for i in range(len(a)):
        score+=grade[dic[a[i]],dic[b[1]]]

    return score
print("\nThe first sequence is DLX5_HUMAN (P56178), the second one is DLX5_MOUSE (P70396). Their score is ",getGrade(s1,s2))
print(getContent(s1,s2))
print('\nThe first sequence is DLX5_MOUSE (P70396), the second one is RandomSeq. Their score is ',getGrade(s2,s3))
print(getContent(s2,s3))
print('\nThe first sequence is DLX5_HUMAN (P56178), the second one is RandomSeq. Their score is ',getGrade(s1,s3))
print(getContent(s1,s3))
### meaning of sequencing method:
# It can present similarity between 2 sequences, and further their homology. This may offer good evidence to research on evolution history of different kinds of animals.
