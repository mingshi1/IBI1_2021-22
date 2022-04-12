# input seq
# find the number of 'GAATTC'
# add 1 to the number of 'GAATTC'
import re
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
Fn=len(re.findall(r'GAATTC',seq))+1   # Fn means the number of fragments
print('The total number of fragments is ',Fn,' if we applied the EcoRI enzyme to it.')


