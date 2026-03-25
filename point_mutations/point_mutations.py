import random
from collections import defaultdict

#input data
dna_seq_in = 'ATGCGTACGTTAGCCTAGCTAGGCTAATGCGTACGTTAGCCTAGCTAGGCTAATGCGTACGTTAGCCTAGCTAGGCTA'

#parameters
num_generations = 1000
mutation_prob = 0.001

#prepare nucelotide sets - othere than the current one
nucleotides = ['A', 'T', 'G', 'C']
nucleotides_excl_A = ['T', 'G', 'C']
nucleotides_excl_T = ['A', 'G', 'C']
nucleotides_excl_G = ['A', 'T', 'C']
nucleotides_excl_C = ['A', 'T', 'G']

nucleotides_excl = defaultdict(list)

for x in nucleotides:
    # print('Nucleotide: ' + str(x))
    for y in nucleotides:
        if x != y:
            nucleotides_excl[x].append(y)
    
# for x, y in nucleotides_excl.items():
    # print('Nucleotide excluded: ' + str(x) + ' | included: ' + str(y))


# simulation
print('Number of generations ' + str(num_generations))
print('Mutation probability: ' + str(mutation_prob))


dna_seq_in_list = list(dna_seq_in)
dna_seq_out_list = list(dna_seq_in)

for g in range(num_generations):
    # print('Generation nr: ' + str(g+1))
    nucleotide_index = 0
    for n in dna_seq_in:        
        # print('Nucleotide: ' + str(nucleotide_cnt) + ' ' + str(n))
        if random.random() < mutation_prob:
            random_n = random.choice(nucleotides_excl[n])
            dna_seq_out_list[nucleotide_index] = random_n
        nucleotide_index = nucleotide_index + 1
        
dna_seq_out = "".join(dna_seq_out_list)

# results
      
print('Input/Output')      
print(dna_seq_in)
print(dna_seq_out)

# metrics

nucleotide_index = 0
nucleotide_total_cnt = 0
nucleotide_changes_cnt = 0

for x in dna_seq_in_list:
    nucleotide_total_cnt = nucleotide_total_cnt + 1
    # print('In: ' + dna_seq_in_list[nucleotide_index] + ' | Out: ' + dna_seq_out_list[nucleotide_index]  )
    if dna_seq_in_list[nucleotide_index] != dna_seq_out_list[nucleotide_index]:
        nucleotide_changes_cnt = nucleotide_changes_cnt + 1
    nucleotide_index = nucleotide_index + 1
    
print('Total nucleotides: ' + str(nucleotide_total_cnt))
print('Changed nucleotides: ' + str(nucleotide_changes_cnt))
print('Percentage of changed nucleotides: ' + str(nucleotide_changes_cnt/nucleotide_total_cnt*100) + '%')
    