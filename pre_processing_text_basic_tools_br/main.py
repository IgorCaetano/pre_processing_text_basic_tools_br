import unicodedata
import re
import string


string_com_caracteres_especiais_padrao = string.punctuation

caracteres_normais = string.printable + 'áàâãéèêíìîóòôõúùûüç' + 'áàâãéèêíìîóòôõúùûüç'.upper()

lista_com_palavras_de_escape_padrao_frequencia = ['a','à','as','às','ao','aos','da','das','na','nas','numa','numas',
                                       'o','os','ou','do','dos','no','nos',
                                       'de','e','é','ser','será','serão','são','está','estão','foi','em','num','nuns',
                                       'são','sem','mais','menos',
                                       'um','uma','uns','umas',
                                       'sua','suas','seu','seus',
                                       'nosso','nossos','nossa','nossas',
                                       'esse','esses','essa','essas',
                                       'só','tão','tem','tens','nem','isso','tá','ta','eu','isto','mas',
                                       'sempre','nunca',
                                       'pelo','também','já','você','vocês','vc','vcs',
                                       'ele','eles','ela','elas','nele','neles','nela','nelas',
                                       'se','te','que','por','pro','pros','pra','pras','para','com','como','sobre','sim','não']

lista_com_palavras_de_escape_padrao_tokenizacao = ['a','à','as','às','ao','aos','da','das','na','nas','numa','numas',
                                       'o','os','ou','do','dos','no','nos',
                                       'de','e','em','num','nuns','ser','será','seres',
                                       'se','te','que','por','com','sobre']

lista_de_pontos_finais_nas_frases_padrao = ['.','!','?',';',':']

digito_dia = r'(0?[1-9]|1[0-9]|2[0-9]|3[0-1])'
digito_mes = r'(0?[1-9]|1[0-2])'
digito_ano = r'\d{2,4}'
padrao_regex_data = r'\b{dia}\/{mes}\/{ano}\b|\b{ano}\/{mes}\/{dia}\b|\b{dia}\-{mes}\-{ano}\b|\b{ano}\-{mes}\-{dia}\b'.format(dia=digito_dia,mes=digito_mes,ano=digito_ano)

padrao_regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

ddd_pais = r'(\+(\s+)?)?\d{2,3}'
ddd_estado = r'(\((\s+)?)?\d{2}((\s+)?\))?'
ddd_celular = r'\d{4,5}([-\s])?\d{4}'
padrao_regex_telefone_celular = r'({pais})?({estado})({celular})|({pais}(\s+)?)?({estado}(\s+)?)({celular})'.format(pais=ddd_pais,estado=ddd_estado,celular=ddd_celular)

padrao_regex_links = r'https?://\S+'

padrao_regex_numeros = r'(\b)?\d+(\S+)?(,\d+)?(\b)?|(\b)?\d+(\S+)?(.\d+)?(\b)?'

padrao_regex_dinheiro = r'R\$(\s+)?\d+(\S+)?(,\d{2})?|\$(\s+)?\d+(\S+)?(\.\d{2})?'

def coletarTextoDeArquivoTxt(caminho_do_arquivo : str,
                             tipo_de_encoding : str = 'utf-8') -> str | None:
    try:
        with open(caminho_do_arquivo,'r',encoding=tipo_de_encoding) as f:
            return f.read()
    except Exception as e:
        erro = f'{e.__class__.__name__}: {str(e)}'
        print(f'Ocorreu um erro ao abrir o arquivo "{caminho_do_arquivo}".\n--> {erro}')
        return None

def removerCaracteresEspeciais(texto : str,                              
                               string_com_os_caracteres_especiais : str = string_com_caracteres_especiais_padrao,                               
                               remover_espacos_em_branco_que_sobrarem : bool = True,
                               remover_hifen_de_palavras : bool = False,
                               tratamento_personalizado : bool = True) -> str:
    """
    Esta função remove caracteres presentes na lista de caracteres para remoção fornecida 
    da string de texto fornecida.
    
    
    FALTA ATUALIZAR DOC STRING!!!!!!!!!!! (adc remover_hifen_de_palavras)
    

    Parâmetros
    ----------
    - :parâmetro texto: String que você quer limpar dos caracteres especiais.
    - :parâmetro string_com_os_caracteres_especiais: String contendo todos os 
    caracteres especiais que você quer remover da string de texto fornecida (o 
    padrão é a string "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~".

    Retornos
    --------
    - :retorno: String fornecida sem os caracteres especiais.
    """
    if not remover_hifen_de_palavras:
        string_com_os_caracteres_especiais = string_com_os_caracteres_especiais.replace('-','')
        texto = texto.replace(' -',' ').replace('- ',' ')
    if not tratamento_personalizado:
        texto = texto.translate(str.maketrans('','',string_com_os_caracteres_especiais))
    else:
        # string_com_os_caracteres_especiais_add_space = re.sub(r'\,\.\!|\#|\$|\%|\&\(|\)\+|\-|\?|\@\[|\]|\{|\||\}|\~','',string_com_os_caracteres_especiais)
        if remover_hifen_de_palavras:
            string_com_os_caracteres_especiais_add_space = r'\/\\\-'
        else:
            string_com_os_caracteres_especiais_add_space = r'\/\\'
        texto = texto.translate(str.maketrans(string_com_os_caracteres_especiais_add_space,' '*len(string_com_os_caracteres_especiais_add_space)))
        texto = texto.translate(str.maketrans('','',string_com_os_caracteres_especiais))
    if remover_espacos_em_branco_que_sobrarem:
        texto = removerEspacosEmBrancoExtras(texto)
    return texto

def removerCaracteresMaisQueEspeciais(texto : str) -> str:
    """
    Esta função passa por todos os caracteres presentes na string de texto 
    fornecida e, se o caracter não estiver dentro da string "caracteres_normais", 
    a qual é basicamente:
    "string.printable + 'áàâãéèêíìîóòôõúùûç' + 'áàâãéèêíìîóòôõúùûç'.upper()",
    remove-o da string original.

    Parâmetros
    ----------
    - :parâmetro texto: String contendo o texto que você quer limpar.

    Retornos
    --------
    - :retorno: String limpa dos caracteres "mais que especiais" (emojis, dígitos estranhos, 
    formas que não se encontram no teclado, etc).
    """
    for c in texto:
        if c not in caracteres_normais:
            texto = texto.replace(c,'')
    return texto

def removerEspacosEmBrancoExtras(texto : str) -> str:
    texto_transformado = re.sub(r'[^\S\n]+',' ',texto)
    return texto_transformado

def transformarTextoSubstituindoCaracteres(texto : str,
                                           caracteres : str | list[str],
                                           substituir_por : str = '',
                                           contagem : int = 0,
                                           considerar_maiusculas_e_minusculas_iguais : bool = False) -> str:
    """
    Esta função remove os caracteres específicos de sua escolha da string de texto fornecida, 
    com base nas regras que você define usando os parâmetros.

    Parâmetros
    ----------
    - :parâmetro texto: String contendo o texto que você quer transformar.
    - :parâmetro caracteres: String contendo o caracter (ou caracteres, se for uma palavra) que 
    você deseja substituir.
    - :parâmetro substituir_por: String contendo o caracter (ou os caracteres, se for uma palavra) 
    que você deseja botar no lugar dos caracteres que você deseja substituir.
    - :parâmetro contagem: Número de vezes referente à remoção do(s) caracter(es) escolhido(s) toda 
    vez que ele for encontrado na string de texto fornecida (o valor padrão é -1, que indica que 
    serão removidos todas as aparições, mas também poderá ser escolhido como contagem = 0 se você 
    quer que seja removido apenas a última aparição). A ordem da contagem é sempre do início para o 
    fim da string de texto.
    - :parâmetro considerar_maiusculas_e_minusculas_iguais: Bool que dirá se você quer considerar 
    as letras maiúscula e minúsculas como iguais (True) ou não (False).
    Retornos
    --------
    - :retorno: String fornecida sem os caracteres escolhidos.
    """
    if isinstance(caracteres,str):
        for c in caracteres:
            if c in string.punctuation:
                caracteres = caracteres.replace(c,r'\{x}'.format(x=c))
    if contagem == -1:        
        if isinstance(caracteres,str):
            if considerar_maiusculas_e_minusculas_iguais:
                texto_analisado = texto.lower()
                caracteres = caracteres.lower()
            else:
                texto_analisado = texto

            resultado = [indice.start() for indice in re.finditer(r'{}'.format(caracteres),texto_analisado)]
            if resultado:
                texto = texto[:resultado[-1]]+substituir_por+texto[resultado[-1]+1:]
            return texto
        
        elif isinstance(caracteres,list):
            padrao_regex_caracteres_na_lista = r''
            for caracter in caracteres:
                if caracter in string.punctuation:
                    caracter = r'\{x}'.format(x=caracter)
                padrao_regex_caracteres_na_lista += r'{x}|'.format(x=caracter)
            padrao_regex_caracteres_na_lista = padrao_regex_caracteres_na_lista[0:-1]
            if considerar_maiusculas_e_minusculas_iguais:
                resultado = [indice.start() for indice in re.finditer(padrao_regex_caracteres_na_lista,texto,flags=re.IGNORECASE)]
            else:
                resultado = [indice.start() for indice in re.finditer(padrao_regex_caracteres_na_lista,texto)]
            if resultado:
                texto = texto[:resultado[-1]]+substituir_por+texto[resultado[-1]+1:]
            return texto
    else:
        if isinstance(caracteres,str):
            if considerar_maiusculas_e_minusculas_iguais:
                return re.sub(r'{c}'.format(c=caracteres),substituir_por,string=texto,count=contagem,flags=re.IGNORECASE)
            else:
                return re.sub(r'{c}'.format(c=caracteres),substituir_por,string=texto,count=contagem)
        elif isinstance(caracteres,list):
            padrao_regex_caracteres_na_lista = r''
            for caracter in caracteres:
                if caracter in string.punctuation:
                    caracter = r'\{x}'.format(x=caracter)
                padrao_regex_caracteres_na_lista += r'{x}|'.format(x=caracter)
            padrao_regex_caracteres_na_lista = padrao_regex_caracteres_na_lista[0:-1]
            if considerar_maiusculas_e_minusculas_iguais:
                return re.sub(padrao_regex_caracteres_na_lista,substituir_por,string=texto,count=contagem,flags=re.IGNORECASE)
            else:
                return re.sub(padrao_regex_caracteres_na_lista,substituir_por,string=texto,count=contagem)

def verificarExistenciaDeElemento(texto : str,
                                  string_especifica : str | None = None,
                                  encontrar_datas : bool = False,                                  
                                  encontrar_emails : bool = False,
                                  encontrar_telefone_celular : bool = False,
                                  encontrar_links : bool = False,
                                  encontrar_numeros : bool = False,
                                  encontrar_dinheiro : bool = False,
                                  considerar_maiusculas_e_minusculas_iguais : bool = True) -> bool:
    
    if string_especifica:
        for c in string_especifica:
            if c in string_especifica:
                string_especifica.replace(c,r'\{x}'.format(x=c))
        if considerar_maiusculas_e_minusculas_iguais:
            if re.search(r'{x}'.format(x=string_especifica),texto,flags=re.IGNORECASE):
                return True
            else:
                return False
        else:
            if re.search(r'{x}'.format(x=string_especifica),texto):
                return True
            else:
                return False
    if encontrar_datas:
        if re.search(padrao_regex_data,texto):
            return True
        else:
            return False
    if encontrar_emails:
        if re.search(padrao_regex_email,texto):
            return True
        else:
            return False
    if encontrar_telefone_celular:
        if re.search(padrao_regex_telefone_celular,texto):
            return True
        else:
            return False
    if encontrar_links:
        if re.search(padrao_regex_links,texto):
            return True
        else:
            return False
    if encontrar_numeros:
        if re.search(padrao_regex_numeros,texto):
            return True
        else:
            return False
    if encontrar_dinheiro:
        if re.search(padrao_regex_dinheiro,texto):
            return True
        else:
            return False

def padronizarDatas(texto: str,
                    padrao_data : str = 'DATA') -> str:
    texto_transformado = re.sub(padrao_regex_data,padrao_data,texto)
    return texto_transformado

def padronizarEmails(texto : str,
                     padrao_email : str = 'EMAIL') -> str:
    texto_transformado = re.sub(padrao_regex_email,padrao_email,texto)
    return texto_transformado

def padronizarTelefoneCelular(texto : str,
                              padrao_tel : str = 'TEL') -> str:
    texto_transformado = re.sub(padrao_regex_telefone_celular,padrao_tel,texto)
    return texto_transformado

def padronizarLinks(texto : str,
                    padrao_link : str = 'LINK') -> str:    
    texto_transformado = re.sub(padrao_regex_links,padrao_link,texto)
    return texto_transformado

def padronizarNumeros(texto : str,
                      padrao_numeros : str = 'NUM') -> str:
    texto_transformado = re.sub(padrao_regex_numeros,padrao_numeros,texto)
    return texto_transformado

def padronizarDinheiros(texto : str,
                        padrao_dinheiro : str = '$') -> str:    
    texto_transformado = re.sub(padrao_regex_dinheiro,padrao_dinheiro,texto)
    return texto_transformado

def padronizarParaFormaCanonica(texto : str) -> str:
    return ''.join(c for c in (d for char in texto for d in unicodedata.normalize('NFD', char) if unicodedata.category(d) != 'Mn'))

def padronizarTextoParaMinuscula(texto : str) -> str:
    texto_transformado = texto.lower()
    return texto_transformado

# Função auxiliar da função de juntarTextoComQuebrasDeLinhas()
def verificarFinalDeLinha(primeira_linha : str,
                          segunda_linha : str,
                          lista_de_pontos_finais : list = lista_de_pontos_finais_nas_frases_padrao) -> tuple[bool, str]:
    for ptos_final in lista_de_pontos_finais:
        if primeira_linha.strip().endswith(ptos_final):
            return True, segunda_linha
    if primeira_linha.endswith('-') and not (segunda_linha.startswith(' ')):
        return False, primeira_linha+segunda_linha.strip()        
    else:
        return False, primeira_linha.strip()+' '+segunda_linha.strip()

def juntarTextoComQuebrasDeLinhas(texto_completo : str,
                                  retorno_tipo_lista : bool = False) -> str:
        
    textos_separados_por_quebra_de_linha = texto_completo.split('\n')
    frases_completas_por_linha = []
    
    if textos_separados_por_quebra_de_linha:
        frases_completas_por_linha.append(removerEspacosEmBrancoExtras(textos_separados_por_quebra_de_linha[0].strip()))    
        for linha in textos_separados_por_quebra_de_linha[1:]:
            if linha.strip() != '':
                linha = removerEspacosEmBrancoExtras(linha.strip())
                status_final_de_linha, resultado = verificarFinalDeLinha(primeira_linha=frases_completas_por_linha[-1],segunda_linha=linha)
                if status_final_de_linha:
                    frases_completas_por_linha.append(resultado)
                else:
                    frases_completas_por_linha[-1] = resultado
            else:
                if frases_completas_por_linha[-1].strip()[-1] not in ['.','!','?',';',':']:
                    frases_completas_por_linha[-1] = frases_completas_por_linha[-1].strip() +'.'
    if retorno_tipo_lista:
        return frases_completas_por_linha
    else:
        return ' '.join(frases_completas_por_linha)

def tokenizarTexto(texto : str | list,
                   dividir_as_frases : bool = False,
                   remover_palavras_de_escape : bool = False,
                   lista_com_palavras_de_escape : list = lista_com_palavras_de_escape_padrao_tokenizacao,
                   desconsiderar_acentuacao_nas_palavras_de_escape : bool = False,
                   tratamento_padrao : bool = True) -> list:
    if desconsiderar_acentuacao_nas_palavras_de_escape:
        lista_com_palavras_de_escape = [padronizarParaFormaCanonica(elemento) for elemento in lista_com_palavras_de_escape]

    if tratamento_padrao:
        if isinstance(texto,str):
            texto = removerCaracteresMaisQueEspeciais(texto)
            texto = removerCaracteresEspeciais(texto)
            texto = removerEspacosEmBrancoExtras(texto)
            texto = padronizarTextoParaMinuscula(texto)
        else:
            lista_de_frases = []
            for elemento in texto:
                if isinstance(elemento,str):
                    elemento = padronizarTextoParaMinuscula(elemento)
                    elemento = removerCaracteresMaisQueEspeciais(elemento)
                    elemento = removerCaracteresEspeciais(elemento)
                    elemento = removerEspacosEmBrancoExtras(elemento)
                    lista_de_frases.append(elemento)
                elif isinstance(elemento,list):                    
                    lista_secundaria_de_frases = []
                    for item in elemento:                        
                        if isinstance(item,str):
                            item = padronizarTextoParaMinuscula(item)
                            item = removerCaracteresMaisQueEspeciais(item)
                            item = removerCaracteresEspeciais(item)
                            item = removerEspacosEmBrancoExtras(item)
                            lista_secundaria_de_frases.append(item)                        
                    lista_de_frases.append(lista_secundaria_de_frases)
                
            texto = lista_de_frases

    if isinstance(texto,str):
        lista_de_tokens = []

        texto_separado = texto.split()
        if remover_palavras_de_escape:
            for token in texto_separado:
                if token not in lista_com_palavras_de_escape:
                    lista_de_tokens.append(token)
        else:
            for token in texto_separado:
                lista_de_tokens.append(token)

        return lista_de_tokens
    
    else:
        lista_de_frases_com_tokens = []

        for elemento in texto:
            if isinstance(elemento,str):
                lista_de_tokens = []
                texto_separado = elemento.split()
                if remover_palavras_de_escape:
                    for token in texto_separado:
                        if token not in lista_com_palavras_de_escape:
                            lista_de_tokens.append(token)
                else:
                    for token in texto_separado:
                        lista_de_tokens.append(token)
                lista_de_frases_com_tokens.append(lista_de_tokens)
            elif isinstance(elemento,list):
                if len(elemento) > 1:
                    lista_secundaria_de_frases_com_tokens = []
                    for item in elemento:
                        if isinstance(item,str):
                            lista_de_tokens = []
                            texto_separado = item.split()
                            if remover_palavras_de_escape:
                                for token in texto_separado:
                                    if token not in lista_com_palavras_de_escape:
                                        lista_de_tokens.append(token)
                            else:
                                for token in texto_separado:
                                    lista_de_tokens.append(token)                        
                            lista_secundaria_de_frases_com_tokens.append(lista_de_tokens)
                    lista_de_frases_com_tokens.append(lista_secundaria_de_frases_com_tokens)
                else:
                    for item in elemento:
                        if isinstance(item,str):
                            lista_de_tokens = []
                            texto_separado = item.split()
                            if remover_palavras_de_escape:
                                for token in texto_separado:
                                    if token not in lista_com_palavras_de_escape:
                                        lista_de_tokens.append(token)
                            else:
                                for token in texto_separado:
                                    lista_de_tokens.append(token)                        
                            lista_de_frases_com_tokens.append(lista_de_tokens) 

        return lista_de_frases_com_tokens

def contarFrequenciaDePalavras(texto : str | list,
                               palavras_especificas : list[str] | None = None,
                               n_top : int = -1,
                               remover_palavras_de_escape : bool = True,
                               lista_com_palavras_de_escape : list = lista_com_palavras_de_escape_padrao_frequencia,
                               tratamento_padrao : bool = True) -> list:    

    lista_tokenizada = tokenizarTexto(texto=texto,remover_palavras_de_escape=remover_palavras_de_escape,lista_com_palavras_de_escape=lista_com_palavras_de_escape,tratamento_padrao=tratamento_padrao)
    dic = {}
    if palavras_especificas:
        if isinstance(lista_tokenizada[0],str):
            for token in palavras_especificas:
                if token not in dic.keys():
                    dic[token] = lista_tokenizada.count(token)
        elif isinstance(lista_tokenizada[0],list):
            for frase in lista_tokenizada:
                tokens_usados = []
                for token in palavras_especificas:
                    if token not in tokens_usados:
                        if token not in dic.keys():
                            dic[token] = frase.count(token)
                    else:
                        dic[token] += frase.count(token)
    else:
        if lista_tokenizada:
            if isinstance(lista_tokenizada[0],str):
                for token in lista_tokenizada:
                    if token not in dic.keys():
                        dic[token] = lista_tokenizada.count(token)
            elif isinstance(lista_tokenizada[0],list):
                for frase in lista_tokenizada:
                    for token in frase:
                        if token not in dic.keys():
                            dic[token] = frase.count(token)                        
    lista_de_frequencias = []
    for token in dic.keys():
        frequencia_do_token = dic[token]
        lista_de_frequencias.append((token,frequencia_do_token))
    
    lista_de_frequencias = sorted(lista_de_frequencias, key=lambda x: x[1], reverse=True)

    if n_top != -1:
        lista_de_frequencias = lista_de_frequencias[:n_top]
    # sortar a lista para maior pra menor e depois ver se precisa restringir o resultado pros top

    return lista_de_frequencias

def formatarTexto(texto : str,
                  padronizar_texto_para_minuscula : bool = True,
                  remover_caracteres_mais_que_especiais : bool = True,
                  remover_caracteres_especiais : bool = True,
                  string_com_os_caracteres_especiais : str = string_com_caracteres_especiais_padrao,
                  remover_espacos_em_branco_em_excesso : bool = True,
                  padronizar_links : bool = False,
                  padrao_link : str = 'LINK',
                  padronizar_numeros : bool = False,
                  padrao_numero : str = 'NUM',
                  padronizar_dinheiros : bool = False,
                  padrao_dinheiro : str = '$',
                  padronizar_datas : bool = False,
                  padrao_data : str = 'DATA',
                  padronizar_emails : bool = False,
                  padrao_email : str = 'EMAIL',
                  padronizar_telefone_celular : bool = False,
                  padrao_tel : str = 'TEL',
                  padronizar_forma_canonica : bool = False) -> str:
    if remover_caracteres_mais_que_especiais:
        texto = removerCaracteresMaisQueEspeciais(texto)
    if padronizar_dinheiros:
        for caracter_padrao_dinheiro in padrao_dinheiro:
            if caracter_padrao_dinheiro in string_com_os_caracteres_especiais:
                caracteres_especiais_impacta_padrao_dinheiro = True
                texto = padronizarDinheiros(texto=texto,padrao_dinheiro='codpdintzzqaio')
                break
        else:
            caracteres_especiais_impacta_padrao_dinheiro = False
            texto = padronizarDinheiros(texto=texto,padrao_dinheiro=padrao_dinheiro)    
    if padronizar_links:
        for caracter_padrao_link in padrao_link:
            if caracter_padrao_link in string_com_os_caracteres_especiais:
                caracteres_especiais_impacta_padrao_link = True
                texto = padronizarLinks(texto=texto,padrao_link='codpltzzqaio')
                break
        else:
            caracteres_especiais_impacta_padrao_link = False
            texto = padronizarLinks(texto=texto,padrao_link=padrao_link)    
    if padronizar_datas:
        for caracter_padrao_data in padrao_data:
            if caracter_padrao_data in string_com_os_caracteres_especiais:
                caracteres_especiais_impacta_padrao_data = True
                texto = padronizarDatas(texto=texto,padrao_data='codpdttzzqaio')
                break
        else:
            caracteres_especiais_impacta_padrao_data = False
            texto = padronizarDatas(texto=texto,padrao_data=padrao_data)
    if padronizar_emails:
        for caracter_padrao_email in padrao_email:
            if caracter_padrao_email in string_com_os_caracteres_especiais:
                caracteres_especiais_impacta_padrao_email = True
                texto = padronizarEmails(texto=texto,padrao_email='codpemtzzqaio')
                break
        else:
            caracteres_especiais_impacta_padrao_email = False
            texto = padronizarEmails(texto=texto,padrao_email=padrao_email)
    if padronizar_telefone_celular:
        for caracter_padrao_tel in padrao_tel:
            if caracter_padrao_tel in string_com_os_caracteres_especiais:
                caracteres_especiais_impacta_padrao_tel = True
                texto = padronizarTelefoneCelular(texto=texto,padrao_tel='codptctzzqaio')
                break
        else:
            caracteres_especiais_impacta_padrao_tel = False
            texto = padronizarTelefoneCelular(texto=texto,padrao_tel=padrao_tel)
    if padronizar_numeros:
        for caracter_padrao_numero in padrao_numero:
            if caracter_padrao_numero in string_com_os_caracteres_especiais:
                caracteres_especiais_impacta_padrao_numero = True
                texto = padronizarNumeros(texto=texto,padrao_numeros='codpntzzqaio') 
                break
        else:
            caracteres_especiais_impacta_padrao_numero = False
            texto = padronizarNumeros(texto=texto,padrao_numeros=padrao_numero)

    if remover_caracteres_especiais:
        texto = removerCaracteresEspeciais(texto=texto,
                                           string_com_os_caracteres_especiais=string_com_os_caracteres_especiais)
    if padronizar_forma_canonica:
        texto = padronizarParaFormaCanonica(texto)
    if remover_espacos_em_branco_em_excesso:
        texto = removerEspacosEmBrancoExtras(texto)
    if padronizar_texto_para_minuscula:
        texto = padronizarTextoParaMinuscula(texto)
    if padronizar_dinheiros and caracteres_especiais_impacta_padrao_dinheiro:
        texto = transformarTextoSubstituindoCaracteres(texto=texto,caracteres='codpdintzzqaio',substituir_por=padrao_dinheiro)
    if padronizar_links and caracteres_especiais_impacta_padrao_link:
        texto = transformarTextoSubstituindoCaracteres(texto=texto,caracteres='codpltzzqaio',substituir_por=padrao_link)
    if padronizar_numeros and caracteres_especiais_impacta_padrao_numero: 
        texto = transformarTextoSubstituindoCaracteres(texto=texto,caracteres='codpntzzqaio',substituir_por=padrao_numero)
    if padronizar_datas and caracteres_especiais_impacta_padrao_data:
        texto = transformarTextoSubstituindoCaracteres(texto=texto,caracteres='codpdttzzqaio',substituir_por=padrao_data)
    if padronizar_emails and caracteres_especiais_impacta_padrao_email:
        texto = transformarTextoSubstituindoCaracteres(texto=texto,caracteres='codpemtzzqaio',substituir_por=padrao_email)
    if padronizar_telefone_celular and caracteres_especiais_impacta_padrao_tel:
        texto = transformarTextoSubstituindoCaracteres(texto=texto,caracteres='codptctzzqaio',substituir_por=padrao_tel)
    
    return texto
