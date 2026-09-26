def load_data(filename: str)-> list[dict]:

    f = open(filename)
    contents = f.read()

    if '<table>' in contents.lower():
        return load_from_html(filename)

    try:
        return load_from_csv(filename)
    except ValueError:
        raise Exception('data must be in CSV or HTML format')

def load_from_html(filename: str) -> list[dict]:
    """
    reads a dataset in HTML format. converts numeric data to float.
    raises an AttributeError if the table rows do not all have the same number of values.
    :param filename: the file path of the html data to read
    :return: the dataset as a list of dictionaries - one dict per object in the file
            each dictionary should map column names to values
    """    
    with open(filename, 'r') as file:
        contents = file.read()
        all_rows = []

        head, body = contents.split('</thead>')

        # process the head first, pull out the column names
        head_parts = head.split('<td>')

        columns = []
        for column_name in head_parts[1:]:
            columns.append(
                column_name.replace('</td>', '').replace('</tr>', '').strip()
            )
        
        # strip off some unecessary tags
        body = body.replace('</tr>', '')
        body = body.replace('</tbody>\n</table>', '')

        # process the rest of the text: the table body
        rows_text = body.split('<tr>')
        for row_text in rows_text[1:]: # skip the first, which just has a <tbody> tag
            row_text = row_text.replace('</td>', '')
            values = row_text.split('<td>')
            values = values[1:]

            # check the row has the right number of values in it
            if len(values) != len(columns):
                raise Exception(f'wrong number of values in row: {row_text}')

            this_row_dict = dict()
            for i in range(len(columns)):
                this_column = columns[i]
                this_value = values[i].strip()

                # convert to float if the value is a number
                try:
                    this_value = float(this_value)
                except ValueError:
                    pass

                this_row_dict[this_column] = this_value
            
            all_rows.append(this_row_dict)
    
    return all_rows


def load_from_csv(filename: str) -> list[dict]:

    with open(filename, 'r') as file:
        lines = file.read()

    all_rows = []
    content = []

    for line in lines.split("\n"):
        if line.strip() != '':
            content.append(line)

    if len(content) < 1:
            raise ValueError("File is empty.")

    columns = []
    for c in content[0].split(','):
        columns.append(c.strip())

    for line in content[1:]:
        values = line.split(',')

        if len(values) != len(columns):
            raise AttributeError(f'wrong number of values in row: {line}')

    row_dict = {}

    for i in range(len(columns)):
        value = values[i].strip()
        try:
            value = float(value)
        except ValueError:
            pass
        row_dict[columns[i]] = value

    all_rows.append(row_dict)

    return all_rows
