# Version: Python 3.13.0

class No :

    def __init__(self, letra):
        self.letra = letra
        self.nodeFilho = [None] * 26
        self.final = False
        self.contador = 0

class Trie :

    def __init__(self):
        self.raiz = No(" ")  
        self.haTrie = False

    def insere(self, palavra) :
        consulta = self.palavraExiste(palavra)
        if consulta :
            print(f"palavra ja existente: {palavra}")
            return
        atual = self.raiz
        for letra in palavra: 
            indice = ord(letra) - ord('a')    
            if not atual.nodeFilho[indice] :    
                atual.nodeFilho[indice] = No(letra)   
            atual = atual.nodeFilho[indice]
        atual.final = True
        self.haTrie = True

        print(f"palavra inserida: {palavra}")

    def consulta(self, palavra) :
        no = self.palavraExiste(palavra)
        if no is not None: 
            no.contador += 1
            print(f"palavra existente: {palavra} {no.contador}")
        else : 
            print(f"palavra inexistente: {palavra}")

    def palavraExiste(self, palavra) : 
        atual = self.raiz
        for letra in palavra: 
            indice = ord(letra) - ord('a')
            if atual.nodeFilho[indice] == None:
                return None   
            atual = atual.nodeFilho[indice]
        if atual.final :
            return atual
        return None 
    
    def palavraMaisConsultada(self) :
        if not self.haTrie : 
            print("trie vazia")
            return
        maiorContagem = 0
        palavras = []
        def dfs(atual, palavraAtual):
            nonlocal maiorContagem, palavras 
            
            if atual.final:
                if atual.contador > maiorContagem:
                    maiorContagem = atual.contador
                    palavras = [palavraAtual]   
                elif atual.contador == maiorContagem:
                    palavras.append(palavraAtual)

            for filho in atual.nodeFilho:  
                if filho is not None:
                     dfs(filho, palavraAtual + filho.letra)  

        dfs(self.raiz, "")

        palavras = self.ordenar(palavras)

        print("palavras mais consultadas:")
        for palavra in palavras:
            print(palavra)
        print(f"numero de acessos: {maiorContagem}")
        
    def imprime(self) :
        if not self.haTrie : 
            print("trie vazia")
            return
        
        atual = self.raiz
        filhos = []
        for filho in atual.nodeFilho :
            if filho is not None : 
                filhos.append(filho.letra)   
        filhos = self.ordenar(filhos) 
        print(f"letra: raiz - {' '.join(filhos)}") 
        
        def dfs(atual, caminho) :

            if caminho != "" :
                filhos = [] 
                for filho in atual.nodeFilho :
                    if filho is not None : 
                        filhos.append(filho.letra)
                filhos = self.ordenar(filhos)
                if atual.final :
                    print(f"letra: {atual.letra} - * {" ".join(filhos)}")
                    print("letra: *")                    
                else :
                    print(f"letra: {atual.letra} - {" ".join(filhos)}")
            

            for filho in atual.nodeFilho :
                if filho is not None :
                    dfs(filho, caminho + filho.letra)

        dfs(self.raiz, "") 
    

    def ordenar(self, lista) :
        for i in range(1, len(lista)) :
            elemento = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > elemento :
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = elemento
        return lista

trie = Trie()

while True :

    operacao = str(input())
    if operacao == 'i' :   
        palavra = str(input())
        trie.insere(palavra)

    elif operacao == 'c' :  
        palavra = str(input())
        trie.consulta(palavra)

    elif operacao == 'f' :   
        trie.palavraMaisConsultada()

    elif operacao == 'p' :   
        trie.imprime()

    elif operacao == 'e' :
        break
