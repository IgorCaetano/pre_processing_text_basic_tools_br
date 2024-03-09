
# Ferramentas básicas para Processamento de Linguagem Natural

Este pacote é um kit de ferramentas (variadas funções) para execução de processos básicos relacionados ao processamento de linguagem natural, muito utilizados para limpeza / pré-processamento de texto antes de inserir os corpus de textos num modelo de treinamento.




## Funcionalidades

- Limpeza de texto;
- Análise de texto;
- Pré-processamento de texto para posterior inserção em modelos de treinamento de linguagem natural;
- Fácil integração com outros programas Python por meio da importação do(s) módulo(s) ou função desejada.


## Instalação

A instalação deste pacote se dá por meio do comando "*pip install*"

```bash
pip install pre-processing-text-basic-tools-br
```

## Uso/Exemplos

### Removendo caractéres especiais

```python
from pre_processing_text_basic_tools_br import removerCaracteresEspeciais

texto = "Este é um $ exemplo, de texto? com caractéres# especiai.s. Quero limpá-lo!!!"

texto_limpo = removerCaracteresEspeciais(texto)

print(texto_limpo)



>>>Este é um exemplo de texto com caractéres especiais Quero limpá-lo
```

É importante destacar que as funções foram pensadas para aplicações para a língua portuguesa. Com isso, palavras com hífen, como sexta-feira, não tem seu caracter especial "-" removido por padrão, mas pode-se escolher pela remoção dos hífens de tais palavras usando o parâmetro *remover_hifen_de_palavras*, passando para *True*.

```python
texto_limpo = removerCaracteresEspeciais(texto,remover_hifen_de_palavras=True)

print(texto_limpo)



>>>Este é um exemplo de texto com caractéres especiais Quero limpálo
```

### Formatação e padronização total do texto

```python
from pre_processing_text_basic_tools_br import formatacaoTotalDeTexto

texto = "Este é um $ exemplo, de texto? que/ que.ro# formatar e&*. padronizar!?"

texto_formatado = formatacaoTotalDeTexto(texto=texto,
                                         padronizar_texto_para_minuscula=True,
                                         remover_caracteres_especiais=True,
                                         remover_caracteres_mais_que_especiais=True,
                                         remover_espacos_em_branco_em_excesso=True,
                                         padronizar_com_unidecode=True)

print(texto_formatado)



>>>este e um exemplo de texto que quero formatar e padronizar
```

### Padronização de elementos diversos

```python
from pre_processing_text_basic_tools_br import formatacaoTotalDeTexto

texto = '''Se eu tiver um texto com e-mail tipo esteehumemail@gmail.com ou 
noreply@hotmail.com ou até mesmo emaildeteste@yahoo.com.br.
Além disso terei também vários telefones do tipo +55 48 911223344 ou 
4890011-2233 e por que não um fixo do tipo 48 0011-2233?
Pode-se ter também datas como 12/12/2024 ou 2023-06-12 em variados tipos 
tipo 1/2/24
E se o texto tiver muito dinheiro envolvido? Falamos de R$ 200.000,00 ou 
R$200,00 ou até com 
a formatação errada tipo R$   2500!
Além disso podemos simplesmente padronizar números como 123123 ou 24 ou 
129381233 ou até mesmo 1.200.234!'''

texto_formatado = formatacaoTotalDeTexto(texto=texto,                                        
                                         padronizar_com_unidecode=True,
                                         padronizar_datas=True,
                                         padrao_data='_data_',
                                         padronizar_dinheiros=True,
                                         padrao_dinheiro='$',
                                         padronizar_emails=True,
                                         padrao_email='_email_',
                                         padronizar_telefone_celular=True,
                                         padrao_tel='_tel_',
                                         padronizar_numeros=True,
                                         padrao_numero='0',
                                         padronizar_texto_para_minuscula=True)

print(texto_formatado)



>>>se eu tiver um texto com e-mail tipo _email_ ou _email_ ou ate mesmo _email_
alem disso terei tambem varios telefones do tipo _tel_ ou _tel_ e por que nao um fixo do tipo _tel_
pode-se ter tambem datas como _data_ ou _data_ em variados tipos tipo _data_
e se o texto tiver muito dinheiro envolvido falamos de $ ou $ ou ate com 
a formatacao errada tipo $
alem disso podemos simplesmente padronizar numeros como 0 ou 0 ou 0 ou ate mesmo 0
```

### Tokenização de textos

Aplicação 1
```python
from pre_processing_text_basic_tools_br.main import tokenizarTexto

texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
especiais também @igorc.s e segue lá?!'''

tokenizacao = tokenizarTexto(texto)

print(tokenizacao)



>>>['este', 'é', 'mais', 'um', 'texto', 'de', 'exemplo', 'para', 'a', 'tokenização', 'vamos', 'usar', 'caractéres', 'especiais', 'também', 'igorcs', 'e', 'segue', 'lá']
```

Aplicação 2
```python
from pre_processing_text_basic_tools_br.main import tokenizarTexto

texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
especiais também @igorc.s e segue lá?!'''

tokenizacao = tokenizarTexto(texto,remover_palavras_de_escape=True)

print(tokenizacao)



>>>['este', 'é', 'mais', 'um', 'texto', 'exemplo', 'para', 'tokenização', 'vamos', 'usar', 'caractéres', 'especiais', 'também', 'igorcs', 'segue', 'lá']
```

Aplicação 3
```python
from pre_processing_text_basic_tools_br.main import tokenizarTexto
from pre_processing_text_basic_tools_br import lista_com_palavras_de_escape_padrao_tokenizacao

texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
especiais também @igorc.s e segue lá?!'''

lista_stop_words_personalizada = lista_com_palavras_de_escape_padrao_tokenizacao + ['este','mais','um','para','também','lá']

tokenizacao = tokenizarTexto(texto,remover_palavras_de_escape=True,lista_com_palavras_de_escape=lista_stop_words_personalizada)

print(tokenizacao)



>>>['este', 'é', 'texto', 'exemplo', 'tokenização', 'vamos', 'usar', 'caractéres', 'especiais', 'igorcs', 'segue']
```

# 

<details>
  <summary>Com mais complexidade  <i>(clique para expandir)</i></summary>
    
  Aplicação 4

    
  ```python
  from pre_processing_text_basic_tools_br.main import tokenizarTexto
  from pre_processing_text_basic_tools_br import lista_com_palavras_de_escape_padrao_tokenizacao

  texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
  especiais também @igorc.s e segue lá?!'''

  texto = formatacaoTotalDeTexto(texto,padronizar_forma_canonica=True)

  tokenizacao = tokenizarTexto(texto=texto,
                               remover_palavras_de_escape=True,
                               lista_com_palavras_de_escape=lista_stop_words_personalizada,
                               desconsiderar_acentuacao_nas_palavras_de_escape=True)

  print(tokenizacao)



  >>>['texto', 'exemplo', 'tokenizacao', 'vamos', 'usar', 'caracteres', 'especiais', 'igorcs', 'segue']
  ```

</details>




## Autores

- [@IgorCaetano](https://github.com/IgorCaetano)


## Usado por

Esse projeto é usado na etapa de pré-processamento de textos no projeto **WOKE** do Grupo de Estudos e Pesquisa em IA e História da UFSC:

- [WOKE - UFSC](https://github.com/iaehistoriaUFSC/Repositorio_UFSC)

