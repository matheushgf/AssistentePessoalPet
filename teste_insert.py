from AssistentePessoalPet import crud

nome = "William"
endereco = "Rua Antoniazzi"
telefone = "1233445566"

nome_tabela = 'dono_pet'

dados = {'nome_dono': nome, 'endereço_dono': endereco, 'telefone_dono': telefone}

crud.insert(nome_tabela, dados)