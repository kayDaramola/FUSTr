sequence = "ATGTTCCTCCACAGAGCTATGAGGTATTACAGGCTGTGGATCTACTCATGCAACCTGGTTCTGCTGGTAAGCGTGGTGGCGTTCGTGTCGCTGGCGGGCTGGATCGCGTCCGACTTCCGTCTGTCGCTCTTCCCGTCGGTGGACTTCCGGCACCCCAGCCTGCTGTACGCCTACTTGGCGCTGGCGCTGCAAGGGGGCGTGCTGCAGGCCATCGGCTGCCTGGGGGCGGTGCGCATGAGCGAGCGCCTGCTCAACGCCTACTGGAGCCTCATGCTGCTGCTGCTGTGCGGCGACGCGGTGCTGAGCGCGTGGAAGCGGAAGAGCCAGACGGCG"
original = "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------R-------------------------------------------------------------------------------------------IHT-----------------------------GEKPFL--------CSFCNK----------------------AFRF---------------------------KNSLQ----------------------------THLRIHT--DG-------------------------------------------------------KQYKCDH--CTKAFN--DKRSLN--------------------------------------------------------VH-LRIHT------------------------------------------------------------------------------------------------------------------------------------------------------------GE---------KP--------------------------F----LCSF--CN--------------------------------------------------------------------------------------KAFRVMNT-----------------------------------------------------LKTH--------LRY-H-----------------T-------------------------------------------GE------------------------------------------------------------KP-------------------------------------------Y-----------------------------------------------------------------------------------------------------------------ECE----HCNT---------------------------VF-ND-------------------------------------------------------------------------------------------K-----------RS----------------M----------------------------NRH-L-R-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------IH-------------------------T--------------------------------------------GE--------------------K---------P----------------------------------------------------FL------------------------C--SF----------------------------C----NK------------------------------------------------------------------------------------------------------------------------------------------AYSD----------------------------QSNL---------------------------K---------------------------------------------KH--------L-L----------------------------I-H----T--------------------------------E------------------------------------------------------------------------------------E--------------------------------------------------------------------------------------------------------------------------------KP-----A---V------------------------------------------------------------CSF--C-----N-------------------------------------------------KA-----------FKCSIG------------------------L----------------------------KKHL-----------------------------------------------------------------------------VIHTD-------------------------------------------EKPF----------------------------QCN---ICNKA--------------------------------------------------------YRD-----------------------------------------------------------PNSLKAHLF-SHS----------------------------------------------GEKPFLC--GTCNKGF----SFQNSLRRH-LII----------------------------------------------------------------------------------------------------------------HS---------------------------------------------------------------------------------------------GEKPNKCDHCNK----------------------------------------------------------------------------------------------------------------------------------AFSDKRSLAVHLRIHTGEKPFICSFCNKAH--------------------------------------------------------RDQSNLRRH-----------IRIHTG---------------------------------------------------------------------------"
cut = [1114, 1115, 1176, 1177, 1221, 1335, 1336, 1337, 1342, 1343, 1344, 1345, 1373, 1374, 1376, 1377, 1469, 1481, 1482, 1499, 1528, 1529, 1530, 1532, 1534, 1732, 1733, 1759, 1804, 1805, 1826, 1836, 1889, 1890, 1915, 1918, 1919, 1948, 1953, 1954, 2093, 2094, 2095, 2096, 2125, 2126, 2127, 2128, 2156, 2202, 2203, 2212, 2214, 2243, 2245, 2250, 2283, 2368, 2497, 2498, 2504, 2508, 2569, 2570, 2571, 2574, 2580, 2630, 2631, 2643]
CodonPos={}
position=0
codon=""
number=1
for i in sequence:

    codon +=i
    if position%3==2:
        CodonPos[number]=codon
        number+=1
    position +=1

    if position%3==0:
        codon=""
aaPos=0
firstAA=True
alnPos=0
prot=""
trimmed=""

for i in original:
    if i!="-":
        aaPos+=1

    if alnPos in cut:
        prot+=i
        if i != "-":
            print(aaPos,CodonPos[aaPos])
            trimmed+=CodonPos[aaPos]
        else:
            trimmed+="---"
    alnPos+=1

print(CodonPos)