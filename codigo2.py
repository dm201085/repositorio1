# 


# n1 = int(input("digite uma nota"))
# n2 = int(input("digite mais uma nota"))
# n3 = int(input("digite outra nota"))

# média = ((n1+n2+n3)/3)

# if média >= 7:
#     print("aprovado")
# else:
#     print("reprovado")



totalvogais = 0
 palavra = input(Digite uma palavra)
vogais =[a,e,i,o,u,A,E,I,O,U]
for carecte in palavra:
    if carecte in vogais:
        totalvogais +=1
print(f"a{palavra} tem {totalvogais} vogais")
