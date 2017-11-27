#the data of cancer patient is already present
prob_pos_cancer=0.008
prob_neg_cancer=0.992
prob_pos_given_cancer=0.98#disease actually present
prob_neg_given_cancer=0.02
prob_neg_given_negcancer=0.97#disease actually not present
prob_pos_given_negcancer=0.03

#finding maximum posterior hypothesis
map_pos=prob_pos_given_cancer*prob_pos_cancer
map_neg=prob_pos_given_negcancer*prob_neg_cancer

#normalizing results
total_map_pos=map_pos/(map_pos+map_neg)
total_map_neg=map_neg/(map_pos+map_neg)

print ("The exact posterior probability of positive is:",total_map_pos)
print ("The exact posterior probability of negative is:",total_map_neg)

k=max(total_map_neg,total_map_pos)
if k==total_map_pos:
    print ("The result is positive with posterior probability",total_map_pos)
else:
    print ("The result is negative with posterior probability",total_map_neg)
