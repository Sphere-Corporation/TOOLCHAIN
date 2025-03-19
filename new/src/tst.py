def process_symbol_file(symbol_file):
    lines = []
    with open(symbol_file,'r') as f1:
        # reading each line from original symbol file and storing it in a list
        for line in f1.readlines():
            # Only store if a line does not begin with a number and does not have an asterisk in it
            if not line[0].isdigit()  and '*' not in line:
                lines.append(line)
    with open(symbol_file, 'w') as f2:
        for line in lines:
            f2.write(line.replace('\f',''))

x = process_symbol_file('SYMBOLS.SYM')