import csv

def read_csv(filename, data_type):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        ret = []
        # skip header
        reader.next()
        for row in reader:
            ret.append(data_type(row))

        return ret

def main():
    import raw_data
    a = read_csv('data/v1_original/key/Key_1.csv', raw_data.KeyData)
    print a

if __name__ == "__main__":
    main()
