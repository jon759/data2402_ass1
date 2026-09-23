from file_IO import load_from_html, load_from_csv
from data_processing import print_stats


# load data
filename = './data/student_dataset.txt'
filename_corr = './data/student_dataset_corrupted.txt'
table_csv = load_from_csv('./data/census_dataset.txt')
table = load_from_html(filename)

# print table statistics
print_stats(table)
print_stats(table_csv)

table = load_from_html(filename_corr)