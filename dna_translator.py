import requests
from Bio.Data import CodonTable
from collections import defaultdict

def get_pdb(pdb_id):
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    pdb_data = ''
    if response.status_code == 200:
        pdb_data = response.text        
    return pdb_data
    
def get_fasta(pdb_id):
    url = f"https://files.rcsb.org/download/.pdb"
    url = f"https://www.rcsb.org/fasta/entry/{pdb_id}/display"
    response = requests.get(url)
    pdb_data = ''
    if response.status_code == 200:
        pdb_data = response.text        
    return pdb_data    

def aa_seq_list(fasta):
    aa_seq = list()
    for line in fasta.splitlines():
        if not line.startswith('>'):
            aa_seq.append(line)
    return aa_seq
    
def aa_seq_to_rna_default(aa_seq):
    back_table = CodonTable.unambiguous_dna_by_id[1].back_table
    rna_string = ""
    for x in aa_seq:
        codon = back_table.get(x, 'NNN')
        codon = codon.replace('T', 'U')
        rna_string += codon
    return rna_string
    
def rna_to_dna(rna):
    dna = rna.replace('U','T')
    return dna
    
def aa_seq_to_rna_all(aa_seq):
    forward_table = CodonTable.unambiguous_dna_by_id[1].forward_table
    forward_table_reverse = defaultdict(list)

    for k,v in forward_table.items():
        forward_table_reverse[v].append(k)
        # print('key: ' + k + ' value: '  + v)

    rna_codon_list = []
    for x in aa_seq:
        aa_codon_list = forward_table_reverse.get(x, 'NNN')
        rna_codon_list.append(aa_codon_list)
    
    return rna_codon_list
    
def aa_seq_to_dna_all(aa_seq):
    forward_table = CodonTable.unambiguous_dna_by_id[1].forward_table
    forward_table_reverse = defaultdict(list)

    for k,v in forward_table.items():
        forward_table_reverse[v].append(k)
        # print('key: ' + k + ' value: '  + v)

    dna_codon_list = []
    for x in aa_seq:
        aa_codon_list = forward_table_reverse.get(x, 'NNN')
        dna_codon_list.append(aa_codon_list)
    
    return dna_codon_list    


protein = '3e7y'    
fasta = get_fasta(protein)
aa_seq_list = aa_seq_list(fasta)
aa_seq = "".join(aa_seq_list)

rna = aa_seq_to_rna_default(aa_seq)
dna = rna_to_dna(rna)
rna_all = aa_seq_to_rna_all(aa_seq)
dna_all = aa_seq_to_dna_all(aa_seq)

print('PDB: ' + protein) 
print('AA1: ' + aa_seq)    
print('RNA DEFAULT: ' + rna)    
print('DNA DEFAULT: ' + dna)    
print('DNA ALL: ')

for x in dna_all:
    print(x)