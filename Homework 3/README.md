Download the files Influenza_inf_expr.txt that hold over 20 samples of expression profiles of human genes in human HBE cells that are infected by the Influenza H1N1 virus. In the second file Influenza_control_expr.txt you will find control samples of cells that are not infected. Both files hold gene names in the first column and expression gene expression values of the corresponding genes in the underlying samples.

Write a python code that:

allows you to find genes that are differentially overexpressed in the infected case using a t-test. Instead of programming such a test yourself, find such a function using packages such as scipy and calculate a P-value for each gene.
Since you will test many different genes, P-values need to be corrected. Apply a multiple testing correction method and determine a corrected P-value for each egene.
As a deliverable the code needs to print out all differential genes that meet the threshold of a corrected P-value of < 0.1.
You need submit a python code that runs using the datafile Influenza_inf_expr.txt and Influenza_control_expr.txt.
