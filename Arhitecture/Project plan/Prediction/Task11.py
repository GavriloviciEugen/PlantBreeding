import time

#check runtime
start_time = time.time()

#create dictionaries
aa = dict()
genes = dict()
aa["TTT"] = "phe"
aa["TTC"] = "phe"
genes["phe"] = 0
aa["TTA"] = "leu"
aa["TTG"] = "leu"
aa["CTT"] = "leu"
aa["CTC"] = "leu"
aa["CTA"] = "leu"
aa["CTG"] = "leu"
genes["leu"] = 0
aa["TCT"] = "ser"
aa["TCC"] = "ser"
aa["TCA"] = "ser"
aa["TCG"] = "ser"
aa["AGT"] = "ser"
aa["AGC"] = "ser"
genes["ser"] = 0
aa["TAT"] = "tyr"
aa["TAC"] = "tyr"
genes["tyr"] = 0
aa["TGT"] = "cys"
aa["TGC"] = "cys"
genes["cys"] = 0
aa["TGG"] = "trp"
genes["trp"] = 0
aa["CCT"] = "pro"
aa["CCC"] = "pro"
aa["CCA"] = "pro"
aa["CCG"] = "pro"
genes["pro"] = 0
aa["CAT"] = "his"
aa["CAC"] = "his"
genes["his"] = 0
aa["CAA"] = "gln"
aa["CAG"] = "gln"
genes["gln"] = 0
aa["CGT"] = "arg"
aa["CGC"] = "arg"
aa["CGA"] = "arg"
aa["CGG"] = "arg"
aa["AGA"] = "arg"
aa["AGG"] = "arg"
genes["arg"] = 0
aa["ATT"] = "ile"
aa["ATC"] = "ile"
aa["ATA"] = "ile"
genes["ile"] = 0
aa["ACT"] = "thr"
aa["ACC"] = "thr"
aa["ACA"] = "thr"
aa["ACG"] = "thr"
genes["thr"] = 0
aa["AAT"] = "asn"
aa["AAC"] = "asn"
genes["asn"] = 0
aa["AAA"] = "lys"
aa["AAG"] = "lys"
genes["lys"] = 0
aa["GTT"] = "val"
aa["GTC"] = "val"
aa["GTA"] = "val"
aa["GTG"] = "val"
genes["val"] = 0
aa["GCT"] = "ala"
aa["GCC"] = "ala"
aa["GCA"] = "ala"
aa["GCG"] = "ala"
genes["ala"] = 0
aa["GAT"] = "asp"
aa["GAC"] = "asp"
genes["asp"] = 0
aa["GAA"] = "glu"
aa["GAG"] = "glu"
genes["glu"] = 0
aa["GGT"] = "gly"
aa["GGC"] = "gly"
aa["GGA"] = "gly"
aa["GGG"] = "gly"
genes["gly"] = 0
aa["ATG"] = "met"
genes["met"] = 0
aa["TAA"] = "stop"
aa["TAG"] = "stop"
aa["TGA"] = "stop"
genes["stop"] = 0


def main():
    # in order to not crash change the file input/output
    file_input = open("input.txt", "r")
    file_output = open("output.txt","w")
    file_output.write("Fiecare linie reprezinta numele genei si numarul de aminoacizi: \n")
    file_output.write("Numele genei NoOfAphe NoOfAleu NoOfAser NoOfAtyr NoOfAcys NoOfAtrp NoOfApro NoOfAhis NoOfAgln "
                      "NoOfAarg NoOfAile NoOfAthr NoOfAasn NoOfAlys NoOfAval NoOfAala NoOfAasp NoOfAglu NoOfAgly start stop \n")
    #for each line
    for line in file_input:
        #check with what the line begins with
        if line[0] == ">":
            #write to txt, first line will be zeros
            for value in genes.values():
               file_output.write(str(value) + ' ')
            file_output.write('\n')
            # gene name
            file_output.write(line.split(' ', 1)[0][1:] + ' ')
            #restore values to zero
            for aa_name in ["phe", "leu", "ser", "tyr", "cys", "trp", "pro", "his", "gln", "arg",
                            "ile", "thr", "asn", "lys", "val", "ala", "asp", "glu", "gly", "met",
                            "stop"]: genes[aa_name] = 0
        else:
            #create a list for each line and split it in parts of 3
            #each line is divizible by 3
            result_list = [line[i:i + 3] for i in range(0, len(line), 3)]
            #add increment to gene dict every aparition in list of a amino in aa
            for i in range(0, len(result_list)):
                if result_list[i] in aa:
                    genes[aa[result_list[i]]] += 1

    #add last dictonary to txt
    for value in genes.values():
        file_output.write(str(value) + ' ')
    file_output.write('\n')

    #prints
    #file_output.write("Asa arata dictionarul \n" + str(genes))
    print("--- %s seconds ---" % (time.time() - start_time))
    file_input.close()
    file_output.close()

#call
main()