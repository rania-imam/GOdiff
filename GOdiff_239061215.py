#GOdiff script to identify significantly differentially expressed genes involved in glycolysis
#output to output.tsv and print out gene with lowest p-value
#By Rania Imam - 31/10/2026
significant = {}    #created a dict called significant to store the gene names and their respective p-values
with open ("SRP123625_differential_expression_results_vs3.tsv") as file:    #opened the differential gene expression dataset using the with open command so it closes itself
        lines = file.readlines()[1:]    #processed the file using readlines so the file is read into a list of strings starting from the second element and skipping the header
for line in lines:  #processed the file line by line
    expression_results = line.rstrip("\n").split("\t")      #removed the newline character and split each tab seperated column into a list
    p_value = 0.05  #created a variable named p-value and defined it as 0.05
    expression_results[5] = float(expression_results[5])    #the p_value is floated to compare a string with a decimal
    if expression_results[5] < p_value:         #compares each p_value in the column to the p_value cutoff
        significant[expression_results[0]] = expression_results[5]          #the gene name and their respective p_value is added to the dict significant

trimmed = {}        #created another dict named trimmed
with open ("MOUSE-mod_trimmed.gaf") as file1:       #opened the annotation file with the command with open so it closes automatically
    with open ("GOdiff_239061215.out", "w") as output:        #opened the output file for writing using the with open command
        header = "Gene Name" + "\t" + "Gene Description" + "\t" + "P-value" + "\n"      #listed out the different headings to be included in the header
        output.write(header)        #wrote the header into the output file
        for line in file1:      #process the annotation file line by line
            mod = line.rstrip("\n").split("\t")     #removed the newline character and split each tab seperated column into a list
            GO = "GO:0006096"       #created a variable for the GO term
            GO_terms = mod[4]       #created a variable for the GO terms column
            if GO_terms == GO and mod[2] in significant and mod[2] not in trimmed:    #i used the if command to filter out genes that match the given GO term, was in the significant dict and also had not already been written in the trimmed dict (some genes were repeated)
                results = mod[2] + "\t" + mod[9] + "\t" + str(significant.get(mod[2])) + "\n"       #i defined what results was as what i wanted to include in the output table in tab seperated columns
                output.write(results)       #results were added to the output file
                trimmed[mod[2]] = significant[mod[2]]       #i added to the trimmed dict, the gene name acted as the key and the p_value was its corresponding value


lowest_pvalue = list(trimmed.values())      #i created a list from the values in the trimmed dict called lowest_pvalues
lowest_pvalue.sort()        #i sorted the list in ascending order

for key in trimmed.keys():      #i started a for loop for the keys in the trimmed dict
    value = trimmed.get(key)        #i created a variable called value which corresponded to the values of the keys in trimmed
    if trimmed[key] == lowest_pvalue[0]:        #i filtered out the key which corresponded to the first value on the list
        print(key, value)       #i printed the lowest p_value with its gene name into the terminal

