"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    file = open('clusters_report.txt', mode='r')
    bad_titles = file.readline().split("  ")

    for _ in range(3): file.readline()

    titles = []
    for bt in bad_titles:
        bt_strip = bt.strip()
        if bt_strip:
            if bt_strip[len(bt_strip)-2:] == 'de':
                bt_strip+=' palabras clave'
            titles.append(bt_strip.replace(' ', '_').lower())

    data_to_df = []
    row = []
    line = file.readline()
    while line:
        if line.count('%'):
            with_dspaces = line.strip().replace('%', '').replace('  ', ' ')
            while '  ' in with_dspaces:
                with_dspaces = with_dspaces.replace('  ',' ')
            row = with_dspaces.split(' ')
        elif line.strip() == '':
            data_to_df.append([
                int(row[0]),
                int(row[1]),
                float(row[2].replace(",",".")),
                " ".join(row[3:])
            ])
        else:
            with_dspaces = line.strip().replace(".","")
            while '  ' in with_dspaces:
                with_dspaces = with_dspaces.replace('  ',' ')
            row += with_dspaces.split(' ')
        line = file.readline()
    df = pd.DataFrame(data_to_df, columns=titles)
    return df