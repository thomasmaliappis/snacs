import os

data_files = {
    'aarhus': {
        'name': 'aarhus',
        'nodes': 61,
        'layers': 5
    },
    'ecoil_all_conditions': {
        'name': 'ecoil_all_conditions',
        'nodes': 1428,
        'layers': 5
    },
    'ecoil_cold': {
        'name': 'ecoil_cold',
        'nodes': 1373,
        'layers': 5
    },
    'ecoil_control': {
        'name': 'ecoil_control',
        'nodes': 1340,
        'layers': 5
    },
    'ecoil_heat': {
        'name': 'ecoil_heat',
        'nodes': 1375,
        'layers': 5
    },
    'ecoil_lactose': {
        'name': 'ecoil_lactose',
        'nodes': 1542,
        'layers': 5
    },
    'ecoil_oxidative': {
        'name': 'ecoil_oxidative',
        'nodes': 1527,
        'layers': 5
    },
    'eu airlines': {
        'name': 'eu airlines',
        'nodes': 450,
        'layers': 37
    },
    'law': {
        'name': 'law',
        'nodes': 71,
        'layers': 3
    },
    'london transport': {
        'name': 'london transport',
        'nodes': 369,
        'layers': 3
    },
    'paper network': {
        'name': 'paper network',
        'nodes': 10,
        'layers': 3
    }
}

threshold = 0.6

for data_file in data_files.keys():
    for motif_type in range(1, 5):
        for f_measure in range(1, 4):
            nodes = data_files[data_file]['nodes']
            layers = data_files[data_file]['layers']
            input_file = data_files[data_file]['name']
            output_file = './results/{}_{}_{}.txt'.format(data_files[data_file]['name'], motif_type, f_measure)
            command = './motif {} {} {} "../Real_networks/{}" {} {} "{}"'.format(motif_type, layers, nodes, input_file, threshold, f_measure, output_file)
            print(command)
            os.system(command)
