from file_IO import load_from_html, load_from_csv, load_from_data, save_to_json
from data_processing import print_stats


# load data
filename = './data/student_dataset.txt'
filename_corr = './data/student_dataset_corrupted.txt'
table_html = load_from_data(filename)
table_csv2 = load_from_data('./data/census_dataset.txt') 
# table_csv = load_from_csv('./data/census_dataset.txt')
# table = load_from_html(filename)

# print table statistics
print_stats(table_html)
print_stats(table_csv2)

# table = load_from_html(filename_corr)
save_to_json('student_data_json.txt', table_html)
save_to_json('census_data_json.txt', table_csv2)