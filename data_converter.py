import csv


def eu_airlines_edges():
    # layers = {1: 'Lufthansa', 2: 'Ryanair', 3: 'Easyjet', 4: 'British_Airways', 5: 'Turkish_Airlines', 6: 'Air_Berlin', 7: 'Air_France', 8: 'Scandinavian_Airlines', 9: 'KLM', 10: 'Alitalia', 11: 'Swiss_International_Air_Lines', 12: 'Iberia', 13: 'Norwegian_Air_Shuttle', 14: 'Austrian_Airlines', 15: 'Flybe', 16: 'Wizz_Air', 17: 'TAP_Portugal', 18: 'Brussels_Airlines', 19: 'Finnair', 20: 'LOT_Polish_Airlines', 21: 'Vueling_Airlines', 22: 'Air_Nostrum', 23: 'Air_Lingus', 24: 'Germanwings', 25: 'Panagra_Airways', 26: 'Netjets', 27: 'Transavia_Holland', 28: 'Niki', 29: 'SunExpress', 30: 'Aegean_Airlines', 31: 'Czech_Airlines', 32: 'European_Air_Transport', 33: 'Malev_Hungarian_Airlines', 34: 'Air_Baltic', 35: 'Wideroe', 36: 'TNT_Airways', 37: 'Olympic_Air'}

    with open('data/transportation/eu airlines/edges.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        layers_details = {}
        for row in csv_reader:
            if line_count != 0:
                layer = int(row[' layer'])
                if layer not in layers_details.keys():
                    layers_details[layer] = {
                        'sources': [row['# source']],
                        'targets': [row[' target']],
                    }
                else:
                    layers_details[layer]['sources'].append(row['# source'])
                    layers_details[layer]['targets'].append(row[' target'])
            line_count += 1

    layers_details = dict(sorted(layers_details.items()))
    with open('data/raw/eu airlines.txt', 'w') as file:
        for layer in layers_details.keys():
            for i in range(len(layers_details[layer]['sources'])):
                file.write('{}\t{}\n'.format(layers_details[layer]['sources'][i], layers_details[layer]['targets'][i]))
            if layer != list(layers_details.keys())[-1]:
                file.write('-----------\n')


def london_transport_edges():
    # layers = {1: 'Tube', 2: 'Overground', 3: 'DLR'}

    with open('data/transportation/london transport/edges.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        layers_details = {}
        for row in csv_reader:
            if line_count != 0:
                layer = int(row[' layer'])
                if layer not in layers_details.keys():
                    layers_details[layer] = {
                        'sources': [row['# source']],
                        'targets': [row[' target']],
                    }
                else:
                    layers_details[layer]['sources'].append(row['# source'])
                    layers_details[layer]['targets'].append(row[' target'])
            line_count += 1

    layers_details = dict(sorted(layers_details.items()))
    with open('data/raw/london transport.txt', 'w') as file:
        for layer in layers_details.keys():
            for i in range(len(layers_details[layer]['sources'])):
                file.write('{}\t{}\n'.format(layers_details[layer]['sources'][i], layers_details[layer]['targets'][i]))
            if layer != list(layers_details.keys())[-1]:
                file.write('-----------\n')


def aarhus_edges():
    # layers = {1: 'lunch', 2: 'facebook', 3: 'coauthor', 4: 'leisure', 5: 'work'}

    with open('data/social/aarhus/edges.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        layers_details = {}
        for row in csv_reader:
            if line_count != 0:
                layer = int(row[' layer'])
                if layer not in layers_details.keys():
                    layers_details[layer] = {
                        'sources': [row['# source']],
                        'targets': [row[' target']],
                    }
                else:
                    layers_details[layer]['sources'].append(row['# source'])
                    layers_details[layer]['targets'].append(row[' target'])
            line_count += 1

    layers_details = dict(sorted(layers_details.items()))
    with open('data/raw/aarhus.txt', 'w') as file:
        for layer in layers_details.keys():
            for i in range(len(layers_details[layer]['sources'])):
                file.write('{}\t{}\n'.format(layers_details[layer]['sources'][i], layers_details[layer]['targets'][i]))
            if layer != list(layers_details.keys())[-1]:
                file.write('-----------\n')

def law_edges():
    # layers = {1: 'advice', 2: 'friendship', 3: 'co-work'}

    with open('data/social/law/edges.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        layers_details = {}
        for row in csv_reader:
            if line_count != 0:
                layer = int(row[' layer'])
                if layer not in layers_details.keys():
                    layers_details[layer] = {
                        'sources': [row['# source']],
                        'targets': [row[' target']],
                    }
                else:
                    layers_details[layer]['sources'].append(row['# source'])
                    layers_details[layer]['targets'].append(row[' target'])
            line_count += 1

    layers_details = dict(sorted(layers_details.items()))
    with open('data/raw/law.txt', 'w') as file:
        for layer in layers_details.keys():
            for i in range(len(layers_details[layer]['sources'])):
                file.write('{}\t{}\n'.format(layers_details[layer]['sources'][i], layers_details[layer]['targets'][i]))
            if layer != list(layers_details.keys())[-1]:
                file.write('-----------\n')

if __name__ == '__main__':
    eu_airlines_edges()
    london_transport_edges()
    aarhus_edges()
    law_edges()
