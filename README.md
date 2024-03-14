
# Ferramentas básicas para Processamento de Linguagem Natural

Este pacote é um kit de ferramentas (variadas funções) para execução de processos básicos relacionados as etapas iniciais de processamento de linguagem natural.

<details>
  <summary><b>Versão em inglês  <i>(clique para expandir)</i></b></summary>
  <br><ul>
  <li><i><a href="https://pypi.org/project/pre-processing-text-basic-tools/">Pypi package english version</a></i></li>
  <li><i><a href="https://github.com/IgorCaetano/pre_processing_text_basic_tools">GitHub repository english version</a></i></li></ul>
</details>


## 🤩 Funcionalidades

- Limpeza e padronização de texto;
- Análise quantitativa de palavras no texto;
- Pré-processamento de texto (tokenização) para posterior inserção em modelos de treinamento de linguagem natural;
- Fácil integração com outros programas Python por meio da importação do(s) módulo(s) ou função desejada.


## 📦 Instalação

A instalação deste pacote se dá por meio do comando "*pip install*"

```bash
pip install pre-processing-text-basic-tools-br
```

Mais informações sobre o pacote no Pypi: <b><a href="https://pypi.org/project/pre-processing-text-basic-tools-br/">pre-processing-text-basic-tools-br pypi package</a></b>


## 📜 Uso/Exemplos

### ⚙️ Funções básicas ⚙️


<details>
  <summary>Removendo caractéres especiais do texto  <i>(clique para expandir)</i></summary>
  <br>
  
  ```python
  from pre_processing_text_basic_tools_br import removerCaracteresEspeciais
  
  texto = "Este é um $ exemplo, de texto? com caractéres# especiai.s. Quero limpá-lo!!!"
  
  texto_limpo = removerCaracteresEspeciais(texto)
  
  print(texto_limpo)
  
  
  
  >>>"Este é um exemplo de texto com caractéres especiais Quero limpá-lo"
  ```

  <details>
    <summary>Observação importante sobre palavras com hífen  <i>(clique para expandir)</i></summary>
    <br>
    É importante destacar que as funções foram pensadas para aplicações diretas para a língua portuguesa. Com isso, palavras com hífen, como sexta-feira, não tem seu caracter especial "-" removido por padrão, mas pode-se optar pela remoção dos hífens de tais palavras       usando o parâmetro <i>remover_hifen_de_palavras</i>, passando para <i>True</i>. Ainda, se quiser que os hífens não sejam substituídos por um espaço " ", pode-se passar o parâmetro <i>tratamento_personalizado</i> para <i>False</i>, o qual substitui caractéres "/",       "\" e "-" para " ".   
    <br><br>
    
  ```python
  from pre_processing_text_basic_tools_br import removerCaracteresEspeciais

  texto = '''Hoje é sexta-feira e dia 09/03/2024! Ou ainda 09-03-2024.'''


  texto_limpo = removerCaracteresEspeciais(texto,remover_hifen_de_palavras=True)

  print(texto_limpo)



  >>>"Hoje é sexta feira e dia 09 03 2024 Ou ainda 09 03 2024"
  ```
  </details>
</details>


<details>
  <summary>Formatação e padronização total do texto  <i>(clique para expandir)</i></summary>
  <br>
  
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
  
  
  
  >>>"este e um exemplo de texto que quero formatar e padronizar"
  ```
</details>

<details>
  <summary>Padronização de elementos específicos - aplicação de máscara  <i>(clique para expandir)</i></summary>
  <br>
  
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
  
  
  
  >>>"""se eu tiver um texto com e-mail tipo _email_ ou _email_ ou ate mesmo _email_
  alem disso terei tambem varios telefones do tipo _tel_ ou _tel_ e por que nao um fixo do tipo _tel_
  pode-se ter tambem datas como _data_ ou _data_ em variados tipos tipo _data_
  e se o texto tiver muito dinheiro envolvido falamos de $ ou $ ou ate com 
  a formatacao errada tipo $
  alem disso podemos simplesmente padronizar numeros como 0 ou 0 ou 0 ou ate mesmo 0"""
  ```
</details>

<details>
  <summary>Contagem de frequência de palavras no texto  <i>(clique para expandir)</i></summary>
  <br>
  
  Este kit de funções permite realizar a contagem de palavras em um texto. Por padrão, ele elimina da contagem as palavras contidas na lista de palavras de escape para calcular a frequência: <i>lista_com_palavras_de_escape_padrao_frequencia</i>. Caso queira desativar esta funcionalidade, basta passar como parâmetro "<i>remover_palavras_de_escape</i>=False". Abaixo temos um exemplo de um uso simples da função de contar a frequência de uma palavra numa determinada frase:

  ```python
  from pre_processing_text_basic_tools_br import contarFrequenciaDePalavras

  texto = '''Aqui vai mais um exemplo de texto de exemplo para uma 
  demonstração de contagem de palavras num texto de exemplo com 
  várias palavras.'''

  frequencias = contarFrequenciaDePalavras(texto=texto)

  for freq in frequencias:
      print(freq)
  
  
  >>>('exemplo', 3)
  ('texto', 2)
  ('palavras', 2)
  ('aqui', 1)
  ('vai', 1)
  ('demonstração', 1)
  ('contagem', 1)
  ('várias', 1)
  ```

  Podemos também selecionar palavras específicas para realização da contagem, passando a lista de palavras no parâmetro <i>palavras_especificas</i>:

  ```python
  from pre_processing_text_basic_tools_br import contarFrequenciaDePalavras

  texto = '''Aqui vai mais um exemplo de texto de exemplo para uma 
  demonstração de contagem de palavras num texto de exemplo com 
  várias palavras.'''

  frequencias = contarFrequenciaDePalavras(texto=texto,
                                           palavras_especificas=['aqui','vai','texto','exemplo','contagem'])

  for freq in frequencias:
      print(freq)

    
  >>>('exemplo', 3)
  ('texto', 2)
  ('aqui', 1)
  ('vai', 1)
  ('contagem', 1)
  ```

  Ainda, pode-se solicitar que seja retornado apenas um valor <i>x</i> de resultados do topo da listagem de frequências. No exemplo abaixo, queremos apenas os top 3 mais frequentes da listagem passada (caso a listagem de palavras específicas não seja passada, o valor n_top sera da listagem padrão de todas as palavras do texto).

  ```python
  from pre_processing_text_basic_tools_br import contarFrequenciaDePalavras

  texto = '''Aqui vai mais um exemplo de texto de exemplo para uma 
  demonstração de contagem de palavras num texto de exemplo com 
  várias palavras.'''

  frequencias = contarFrequenciaDePalavras(texto=texto,
                                           palavras_especificas=['aqui','vai','texto','exemplo','contagem'],
                                           n_top=3)

  for freq in frequencias:
      print(freq)


  >>>('exemplo', 3)
  ('texto', 2)
  ('aqui', 1)
  ```


</details>


### ⚙️ Funções mais complexas ⚙️

<details>
  <summary>Tokenização de textos  <i>(clique para expandir)</i></summary>
  <br> 
  
  ```python
  from pre_processing_text_basic_tools_br.main import tokenizarTexto
  
  texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
  especiais também @igorc.s e segue lá?!'''
  
  tokenizacao = tokenizarTexto(texto)
  
  print(tokenizacao)
  
  
  
  >>>['este', 'é', 'mais', 'um', 'texto', 'de', 'exemplo', 'para', 'a', 'tokenização', 'vamos', 'usar', 'caractéres', 'especiais', 'também', 'igorcs', 'e', 'segue', 'lá']
  ```

  <br>
  <details>
    <summary>Tokenização removendo palavras de escape/stopwords  <i>(clique para expandir)</i></summary>
    <br>
    Palavras de escape ou stopwords são palavras que não apresentam muito significado em frases, dessa forma algumas aplicações, a fim de otimizarem seu processamento e tempo de treinamento, removem tais palavras do corpus de texto. Alguns exemplos de stopwords               comuns       são artigos e preposições.
    <br><br>
          
  ```python
    from pre_processing_text_basic_tools_br import tokenizarTexto
  
    texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
    especiais também @igorc.s e segue lá?!'''
  
    tokenizacao = tokenizarTexto(texto,remover_palavras_de_escape=True)
  
    print(tokenizacao)
  
  
  
    >>>['este', 'é', 'mais', 'um', 'texto', 'exemplo', 'para', 'tokenização', 'vamos', 'usar', 'caractéres', 'especiais', 'também', 'igorcs', 'segue', 'lá']
  ```
  
  </details>
  
  <details>
    <summary>Tokenização removendo palavras de escape/stopwords com lista de stopwords personalizada  <i>(clique para expandir)</i></summary>
    <br>
    Podemos também selecionar uma lista de stopwords personalizada, adicionando ou removendo da lista padrão <i>lista_com_palavras_de_escape_padrao_tokenizacao</i> ou até mesmo criando uma lista totalmente única.
    <br><br>
  
  ```python
  from pre_processing_text_basic_tools_br import tokenizarTexto
  from pre_processing_text_basic_tools_br import lista_com_palavras_de_escape_padrao_tokenizacao

  texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
  especiais também @igorc.s e segue lá?!'''

  lista_stop_words_personalizada = lista_com_palavras_de_escape_padrao_tokenizacao + ['este','mais','um','para','também','lá']

  tokenizacao = tokenizarTexto(texto,remover_palavras_de_escape=True,lista_com_palavras_de_escape=lista_stop_words_personalizada)

  print(tokenizacao)



  >>>['este', 'é', 'texto', 'exemplo', 'tokenização', 'vamos', 'usar', 'caractéres', 'especiais', 'igorcs', 'segue']
  ```
  
  </details>
  
  <details>
    <summary>Tokenização mais completa  <i>(clique para expandir)</i></summary>
    <br>
    Pode-se também utilizar uma formatação prévia antes do processo de tokenização. No exemplo abaixo passa-se o texto para a forma canônica antes de tokenizá-lo. Ou seja, palavras como "coração" passam a ser "coracao", perdendo seus acentos, "ç", etc.
    <br><br>
      
  ```python
  from pre_processing_text_basic_tools_br import tokenizarTexto
  from pre_processing_text_basic_tools_br import lista_com_palavras_de_escape_padrao_tokenizacao

  texto = '''Este é mais um texto de exemplo para a tokenização!!! Vamos usar caractéres, 
  especiais também @igorc.s e segue lá?!'''

  lista_stop_words_personalizada = lista_com_palavras_de_escape_padrao_tokenizacao + ['este','mais','um','para','também','lá']

  texto = formatacaoTotalDeTexto(texto,padronizar_forma_canonica=True)

  tokenizacao = tokenizarTexto(texto=texto,
                               remover_palavras_de_escape=True,
                               lista_com_palavras_de_escape=lista_stop_words_personalizada,
                               desconsiderar_acentuacao_nas_palavras_de_escape=True)

  print(tokenizacao)



  >>>['texto', 'exemplo', 'tokenizacao', 'vamos', 'usar', 'caracteres', 'especiais', 'igorcs', 'segue']
  ```
  
  </details>
  
</details>




## 😁 Autores

- [@IgorCaetano](https://github.com/IgorCaetano)


## 🤝 Usado por



- Esse projeto é usado na etapa de pré-processamento de textos no projeto **[WOKE](https://github.com/iaehistoriaUFSC/Repositorio_UFSC)** do Grupo de Estudos e Pesquisa em IA e História da UFSC.
