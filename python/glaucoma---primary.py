# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"F4H1400","system":"readv2"},{"code":"F45..00","system":"readv2"},{"code":"F45z.00","system":"readv2"},{"code":"F404211","system":"readv2"},{"code":"F452500","system":"readv2"},{"code":"F463100","system":"readv2"},{"code":"7275.00","system":"readv2"},{"code":"FyuG.00","system":"readv2"},{"code":"107407.0","system":"readv2"},{"code":"39120.0","system":"readv2"},{"code":"44817.0","system":"readv2"},{"code":"11059.0","system":"readv2"},{"code":"2074.0","system":"readv2"},{"code":"8001.0","system":"readv2"},{"code":"28536.0","system":"readv2"},{"code":"89934.0","system":"readv2"},{"code":"20520.0","system":"readv2"},{"code":"30649.0","system":"readv2"},{"code":"46069.0","system":"readv2"},{"code":"52888.0","system":"readv2"},{"code":"53879.0","system":"readv2"},{"code":"4581.0","system":"readv2"},{"code":"6315.0","system":"readv2"},{"code":"88142.0","system":"readv2"},{"code":"1798.0","system":"readv2"},{"code":"72394.0","system":"readv2"},{"code":"67413.0","system":"readv2"},{"code":"91442.0","system":"readv2"},{"code":"8132.0","system":"readv2"},{"code":"28189.0","system":"readv2"},{"code":"93967.0","system":"readv2"},{"code":"28505.0","system":"readv2"},{"code":"9469.0","system":"readv2"},{"code":"44295.0","system":"readv2"},{"code":"2823.0","system":"readv2"},{"code":"88595.0","system":"readv2"},{"code":"44338.0","system":"readv2"},{"code":"95852.0","system":"readv2"},{"code":"35446.0","system":"readv2"},{"code":"42447.0","system":"readv2"},{"code":"65079.0","system":"readv2"},{"code":"107168.0","system":"readv2"},{"code":"10070.0","system":"readv2"},{"code":"20230.0","system":"readv2"},{"code":"C60.4","system":"readv2"},{"code":"C60.2","system":"readv2"},{"code":"C60.3","system":"readv2"},{"code":"C62.4","system":"readv2"},{"code":"C60.5","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('glaucoma-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["glaucoma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["glaucoma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["glaucoma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
