# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"42P2.00","system":"readv2"},{"code":"42P8.00","system":"readv2"},{"code":"C391211","system":"readv2"},{"code":"D314.00","system":"readv2"},{"code":"D314100","system":"readv2"},{"code":"D314200","system":"readv2"},{"code":"D314300","system":"readv2"},{"code":"D314y00","system":"readv2"},{"code":"D314z00","system":"readv2"},{"code":"D315.00","system":"readv2"},{"code":"G756100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('secondary-or-other-thrombocytopaenia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["thrombocytopenic-secondary-or-other-thrombocytopaenia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["thrombocytopenic-secondary-or-other-thrombocytopaenia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["thrombocytopenic-secondary-or-other-thrombocytopaenia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
