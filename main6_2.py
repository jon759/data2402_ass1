from file_IO_2 import load_from_html, load_from_csv, load_data, save_to_json
from data_processing_2 import print_stats


filename = './data/student_dataset.txt'
filename_corr = './data/student_dataset_corrupted.txt'
table_html = load_data(filename)
table_csv2 = load_data('./data/census_subset.txt') 


# print table statistics
print_stats(table_html)
print_stats(table_csv2)

save_to_json('student_data_json.txt', table_html)
save_to_json('census_subset_json.txt', table_csv2)