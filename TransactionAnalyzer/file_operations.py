from TransactionAnalyzer.models import MoneyOperation
from csv import reader
from io import TextIOWrapper


def handle_uploaded_file(file, user):
    file = read_file(file)
    insert_into_database(list(file), user)
    

def read_file(file):
    file = TextIOWrapper(file, encoding='utf-8')
    file = reader(file)

    return file


def insert_into_database(file, user):
    base_data = file[0][7]
    base_data = base_data[:10]

    
    # Verificação 01 - O Arquivo está vazio?
    if empty_line(file):
        return None
    else:
        for line in file: # Verificação 02 - Tem linhas faltando?
            if empty_info(line):
                print('Elemento Vazio!')
                continue
            elif is_data_invalid(line[7], base_data): # Verificação 03 - A data é válida (Mesmo dia)?
                print('Data Inválida!')
                continue
            elif is_operation_in_database(line): # Verificação 04 - Já existe no banco de dados?
                continue
            else:
                operation = MoneyOperation(banco_origem = line[0], agencia_origem = line[1], 
                                           conta_origem = line[2], banco_destino = line[3], 
                                           agencia_destino = line[4], conta_destino = line[5], 
                                           valor = line[6], data_transacao = line[7], usuario=user)
                operation.save()


def empty_line(file):
    for line in file:
        if line == '':
            return True
    
    return False


def empty_info(line):
    for element in line:
        if element == '':
            return True
    
    return False


def is_data_invalid(data, base_data):
    if data[:10] != base_data:
        return True
    
    return False


def is_operation_in_database(line):
    query_set = MoneyOperation.objects.filter(banco_origem = line[0], agencia_origem = line[1], 
                                              conta_origem = line[2], banco_destino = line[3], 
                                              agencia_destino = line[4], conta_destino = line[5], 
                                              valor = line[6], data_transacao = line[7])  
    if len(query_set) > 0:
        return True
    
    return False