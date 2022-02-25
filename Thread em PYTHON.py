from threading import Thread

def funcao(nome, contador , vetor):
    c = 1
    fat = 1
    vet_ite = []
    while c < vetor:
        fat = fat * c
        c+=1
        vet_ite.append(c)
##############  iTERAÇÃO ########################################
    k = len(vet_ite) - 1
    aux = 1
    print("INICIOU THREAD",contador+1)
        
        
    while k >= 0:
        p = aux * vet_ite[k]
        aux = p
        print("Thread",contador+1,'-',vet_ite[k],'calculo de iteração = ',aux )
############   RESULTADO ############################
        m = 0
        if k == 0:
            m = 1
        if m == 1:
            fat_2 = 1
            r = 1
            while r <= vetor:
                fat_2 = fat_2 * r
                resul = fat_2
                r+=1
            m = 3
            print("RESULTADO THREAD",contador+1,'=',resul)

        k-=1



def main():
    qtd = int(input("Quantas Fatoriais deseja calcular? :"))
    c = 1
    vetor = []
    while c <= qtd:
        fat = int(input("Diga O número..."))
        vetor.append(fat)
        c+=1
    for i in range(len(vetor)):
        fatorial = Thread(target= funcao, args=["Fatorial",i,vetor[i]])
        fatorial.start()
    input("")
main()
