from Bio import SeqIO
import csv

def main():
    # Read ID, Synonyms and location of all protein-coding
    with open("protein-coding_gene.txt", "rU") as handle:
        csvreader = csv.DictReader(handle, delimiter="\t")
        protein_data = {"ID": [], "Synonyms": [], "Chromosome": []}
        for row in csvreader:
            protein_data["ID"].append(row["Approved Symbol"])
            protein_data["Synonyms"].append(row["Synonyms"])
            protein_data["Chromosome"].append(row["Chromosome"])
    
    # Read the human.fa file for ID and match it to protein-coding to find match and get synonyms and location  
    with open("human.fa", "rU") as input_handle, open("human_new.fa", "w") as output_handle:
        sequences = SeqIO.parse(input_handle, "fasta")
        for seq in sequences:
            try:
                idx = protein_data["ID"].index(seq.id)
                seq.description = seq.id+" | "+protein_data["Synonyms"][idx]+" | "+protein_data["Chromosome"][idx]
                count = SeqIO.write(seq, output_handle, "fasta")
            except:
                print(seq.id+" not found in "+"protein-coding_gene.txt")
        print("New fasta file with modified format: human_new.fa")
        
if __name__ == "__main__":
    main()
