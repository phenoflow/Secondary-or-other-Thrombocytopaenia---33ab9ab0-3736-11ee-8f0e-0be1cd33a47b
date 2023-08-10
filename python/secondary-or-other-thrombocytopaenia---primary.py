# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"C391200","system":"readv2"},{"code":"107488.0","system":"med"},{"code":"108345.0","system":"med"},{"code":"20181.0","system":"med"},{"code":"21697.0","system":"med"},{"code":"31322.0","system":"med"},{"code":"38137.0","system":"med"},{"code":"4006.0","system":"med"},{"code":"42439.0","system":"med"},{"code":"47751.0","system":"med"},{"code":"63910.0","system":"med"},{"code":"68333.0","system":"med"},{"code":"880.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('secondary-or-other-thrombocytopaenia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["secondary-or-other-thrombocytopaenia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["secondary-or-other-thrombocytopaenia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["secondary-or-other-thrombocytopaenia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
