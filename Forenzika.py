# -*-encoding:utf-8 -*-

dnaseq = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGG" \
         "GTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCG" \
         "CTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGC" \
         "AGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCT" \
         "CCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

Eva = ["female", "white", "blonde", "blue", "oval"]
Larisa = ["female", "white", "brown", "brown", "oval"]
Matej = ["male", "white", "black", "blue", "oval"]
Miha = ["male", "white", "brown", "green", "square"]

hrcol =   {"CCAGCAATCGC": "black", "GCCAGTGCCG": "brown", "TTAGCTATCGC": "blonde"}
fcshape = {"GCCACGG": "square", "ACCACAA": "round", "AGGCCTCA": "oval"}
eyecol =  {"TTGTGGTGGC": "blue", "GGGAGGTGGC": "green", "AAGTAGTGAC": "brown"}
gend =    {"TGAAGGACCTTC": "female", "TGCAGGAACTTC": "male"}
race =    {"AAAACCTCA": "white", "CGACTACAG": "black", "CGCGGGCCG": "asian"}

suspect = []

print "Telesne znaČilnosti osumljenca: "
for seq in hrcol:
    if seq in dnaseq:
        suspect.append(hrcol[seq])
        print "Barva las: " +hrcol[seq]

for seq in fcshape:
    if seq in dnaseq:
        suspect.append(fcshape[seq])
        print "Oblika obraza: " +fcshape[seq]

for seq in eyecol:
    if seq in dnaseq:
        suspect.append(eyecol[seq])
        print "Barva obraza: " +eyecol[seq]

for seq in gend:
    if seq in dnaseq:
        suspect.append(gend[seq])
        print "Spol: " +gend[seq]

for seq in race:
    if seq in dnaseq:
        suspect.append(race[seq])
        print "Rasa: " +race[seq]

print "_____________________________________________\n"

result1 = []
for feature in suspect:
    if feature in Eva:
        result1.append(feature)
        if len(result1) == len(suspect):
            print "Požeruh je Eva"
result2 = []
for feature in suspect:
    if feature in Larisa:
        result2.append(feature)
        if len(result2) == len(suspect):
            print "Požeruh je Larisa"
result3 = []
for feature in suspect:
    if feature in Matej:
        result3.append(feature)
        if len(result3) == len(suspect):
            print "Požeruh je Matej"
result4 = []
for feature in suspect:
    if feature in Miha:
        result4.append(feature)
        if len(result4) == len(suspect):
            print "Požeruh je Miha"