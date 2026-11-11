# GOdiff

Python script that combines RNAseq differential expression results with
GO annotations to find significantly differentially expressed genes
involved in glycolysis (GO:0006096).

## What it does
- Reads genes with adjusted p-value < 0.05 from the differential expression file
- Keeps genes annotated with GO:0006096 in the mouse GAF file
- Writes gene name, description and p-value to an output file
- Prints the gene with the lowest p-value (Gpi1, 2.34e-06)

## Files
- `GOdiff_239061215.py` - the script
- `GOdiff_239061215.txt` - the plan written before coding

## Usage
Place `SRP123625_differential_expression_results_vs3.tsv` and
`MOUSE-mod_trimmed.gaf` in the working directory, then run:

    python3 GOdiff_239061215.py
