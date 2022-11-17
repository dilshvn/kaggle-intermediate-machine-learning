# Fill in the line below: How many rows are in the training data?
num_rows = X_train.shape[0]

# Fill in the line below: How many columns in the training data
# have missing values?
num_cols_with_missing = missing_val_count_by_column.shape[0]

# Fill in the line below: How many missing entries are contained in 
# all of the training data?
tot_missing = missing_val_count_by_column.sum()

# Check your answers
step_1.a.check()