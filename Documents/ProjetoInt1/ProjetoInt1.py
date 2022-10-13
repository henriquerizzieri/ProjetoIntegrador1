#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyodbc

dados_conexao = ("Driver={Oracle in XE};"
            "Server=LAPTOP-TUITDDS2;"
            "Database=ALIMENTOS_TACO;"
            "UID=system;"
            "PWD=280599;")

#caso precisasse de login e senha:
#dados_conexao = ("Driver={SQL Server Native Client 11.0};"
#            "Server=UKXXX00123,45600;"
#            "Database=DB01;"
#            "UID=Login;"
#            "PWD=Senha;")


conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem sucedida')
def DadosUser():
    tentar_dnv = False
    while not tentar_dnv:
        try:
            altura = float(input("Digite sua altura em centimetros:"))
            peso = float(input("Digite seu peso em kg:"))
            idade = int(input("Digite sua idade"))
            sexo = input('Informe o seu Sexo [M ou F]: ').upper()
            faf_l=int(input("1=(Leve), 2=(Moderada) ou 3=(Intensa): "))
            
            if altura >= 150 and altura <=300 and peso > 50 and peso < 200 and idade >= 18:
                if sexo=='M' or sexo=='F': 
                    if faf_l ==1 or faf_l == 2 or faf_l == 3:
                        tentar_dnv = True
                    else:
                        print('Preencha corretamente os campos_')
                else:
                        print('Preencha corretamente os campos_')
            else:
                        print('Preencha corretamente os campos_')


            
        except ValueError:
            print("Preencha corretamente os campos")
    return altura, peso, idade, sexo, faf_l


# In[ ]:


print('Este programa foi feito para atender homens e mulheres de 18 a "x" Anos de idade')
print("\n\n")

altura, peso, idade, sexo, faf_l = DadosUser()

altura=altura/100

imc=peso/altura**2

print("Seu IMC é %.1f"% (imc))
print("\n")

if imc<18.5:
    print("IMC menor que 18,5")
    print("Abaixo do Peso")
elif imc >=18.5 and imc<=24.9:
    print("IMC entre 18,5 e 24,9")
    print("Peso Normal")
elif imc>=25 and imc<=29.9:
    print("IMC entre 25 e 29,9")
    print("Sobrepeso ")
elif imc>=30 and imc<=34.9:
    print("IMC entre 30 e 34,9")
    print("Obesidade Grau I")
elif imc>=35 and imc<=39.9:
    print("IMC entre 35 e 39,9")
    print("Obesidade Grau II")
elif imc>=40:
    print("IMC Maior que 40")
    print("Obesidade Grau III")

print("\n\n")
print ("Calculo Gasto de calorias diarias")
print("\n")

#trimestre=(1,2,3)
#lactante=(1,2)
#v_f=(1,2)
#gestante=(1,2)

#Pergunta para mulheres até 60 anos se esta gestante ou lactante
if sexo=="F" and idade<60:
    gestante=int(input("Gestante: 1=(SIM) 2=(NÃO)"))
    if gestante==1:
        trimestre=int(input("1=(1ºTrimestre Gestação), 2=(2ºTrimestre Gestação), 3=(3ºTrimestre Gestação)"))#Pergunta em qual trimestre de gestação está
        if idade>=18 and idade<30 and faf_l==1 and trimestre==1:
            fom_basal=(13.3*peso)+(334*altura)+35+150 #Adicional de 150 calorias para 1º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))

        elif idade>=18 and idade<30 and faf_l==1 and trimestre==2:
            fom_basal=(13.3*peso)+(334*altura)+35+350 #Adicional de 350 calorias para 2º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))

        elif idade>=18 and idade<30 and faf_l==1 and trimestre==3:
            fom_basal=(13.3*peso)+(334*altura)+35+350 #Adicional de 350 calorias para 3º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))
        elif idade>=18 and idade<30 and faf_l==2 and trimestre==1:
            fom_basal=(13.3*peso)+(334*altura)+35+150 #Adicional de 150 calorias para 1º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))

        elif idade>=18 and idade<30 and faf_l==2 and trimestre==2:
            fom_basal=(13.3*peso)+(334*altura)+35+350 #Adicional de 350 calorias para 2º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"%(fom_basal*1.78))

        elif idade>=18 and idade<30 and faf_l==2 and trimestre==3:
            fom_basal=(13.3*peso)+(334*altura)+35+350 #Adicional de 350 calorias para 3º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))
        #
        elif idade>=18 and idade<30 and faf_l==3 and trimestre==1:
            fom_basal=(13.3*peso)+(334*altura)+35+150 #Adicional de 150 calorias para 1º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))

        elif idade>=18 and idade<30 and faf_l==3 and trimestre==2:
            fom_basal=(13.3*peso)+(334*altura)+35+350 #Adicional de 350 calorias para 2º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))

        elif idade>=18 and idade<30 and faf_l==3 and trimestre==3:
            fom_basal=(13.3*peso)+(334*altura)+35+350 #Adicional de 350 calorias para 3º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))
        #
        elif idade>=30 and idade<60 and faf_l==1 and trimestre==1:
            fom_basal=(8.7*peso)-(25*altura)+865+150 #Adicional de 150 calorias para 1º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))

        elif idade>=30 and idade<60 and faf_l==1 and trimestre==2:
            fom_basal=(8.7*peso)-(25*altura)+865+350 #Adicional de 350 calorias para 2º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))

        elif idade>=30 and idade<60 and faf_l==1 and trimestre==3:
            fom_basal=(8.7*peso)-(25*altura)+865+350 #Adicional de 350 calorias para 3º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))
        #
        elif idade>=30 and idade<60 and faf_l==2 and trimestre==1:
            fom_basal=(8.7*peso)-(25*altura)+865+150 #Adicional de 150 calorias para 1º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))

        elif idade>=30 and idade<60 and faf_l==2 and trimestre==2:
            fom_basal=(8.7*peso)-(25*altura)+865+350 #Adicional de 350 calorias para 2º  trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))

        elif idade>=30 and idade<60 and faf_l==2 and trimestre==3:
            fom_basal=(8.7*peso)-(25*altura)+865+350 #Adicional de 350 calorias para  3º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))
        elif idade>=30 and idade<60 and faf_l==3 and trimestre==1:
            fom_basal=(8.7*peso)-(25*altura)+865+150 #Adicional de 150 calorias para 1º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))

        elif idade>=30 and idade<60 and faf_l==3 and trimestre==2:
            fom_basal=(8.7*peso)-(25*altura)+865+350 #Adicional de 350 calorias para 2º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))

        elif idade>=30 and idade<60 and faf_l==3 and trimestre==3:
            fom_basal=(8.7*peso)-(25*altura)+865+350 #Adicional de 350 calorias para 3º trimestre de gestação
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))
        



        print ("\n")
if sexo=="F" and idade<60:
    v_f=int(input("Lactante: 1=(SIM) 2=(NÃO)"))
    if v_f==1:
        lactante=int(input("Lactante: 1=(1ºSemetre pós-parto) 2=(2ºSemetre pós-parto)"))
        if idade>=18 and idade<30 and faf_l==1 and lactante==1 or lactante==2:
            fom_basal=(13.3*peso)+(334*altura)+35+500 #Adicional de 500 calorias para 1º e 2º semestre de lactante
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))
        elif idade>=18 and idade<30 and faf_l==2 and lactante==1 or lactante==2:
            fom_basal=(13.3*peso)+(334*altura)+35+500 #Adicional de 500 calorias para 1º e 2º semestre de lactante
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))
        elif idade>=18 and idade<30 and faf_l==3 and lactante==1 or lactante==2:
            fom_basal=(13.3*peso)+(334*altura)+35+500 #Adicional de 500 calorias para 1º e 2º semestre de lactante
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))
        elif idade>=30 and idade<60 and faf_l==1 and lactante==1 or lactante==2:
            fom_basal=(8.7*peso)-(25*altura)+865+500 #Adicional de 500 calorias para 1º e 2º semestre de lactante
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))
        elif idade>=30 and idade<60 and faf_l==2 and lactante==1 or lactante==2:
            fom_basal=(8.7*peso)-(25*altura)+865+500 #Adicional de 500 calorias para 1º e 2º semestre de lactante
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))
        elif idade>=30 and idade<60 and faf_l==3 and lactante==1 or lactante==2:
            fom_basal=(8.7*peso)-(25*altura)+865+500 #Adicional de 500 calorias para 1º e 2º semestre de lactante
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))
    else:
        if idade>=18 and idade<30 and faf_l==1 and gestante==2 and v_f==2:
            fom_basal=(13.3*peso)+(334*altura)+35
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))
        elif idade>=18 and idade<30 and faf_l==2  and gestante==2 and v_f==2:
            fom_basal=(13.3*peso)+(334*altura)+35
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))
        elif idade>=18 and idade<30 and faf_l==3 and gestante==2 and v_f==2:
            fom_basal=(13.3*peso)+(334*altura)+35
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))
        elif idade>=30 and idade<60 and faf_l==1  and gestante==2 and v_f==2:
            fom_basal=(8.7*peso)-(25*altura) + 865
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))
        elif idade>=30 and idade<60 and faf_l==2 and gestante==2 and v_f==2:
            fom_basal=(8.7*peso)-(25*altura)+865
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))
        elif idade>=30 and idade<60 and faf_l==3 and gestante==2 and v_f==2:
            fom_basal=(8.7*peso)-(25*altura) + 865
            print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))
        

# Abaixo mulheres acima dos 60 anos com fator de atividade fisica (faf_l) leve, moderado e intenso
elif idade>=60 and faf_l==1 and sexo == 'F':
    fom_basal=(9.2*peso)+(637*altura) + 302
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))

elif idade>=60 and faf_l==2 and sexo == 'F':
    fom_basal=(9.2*peso)+(637*altura) + 302
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*178))

elif idade>=60 and faf_l==3 and sexo == 'F':
    fom_basal=(9.2*peso)+(637*altura) + 302
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.82))


# Abaixo homens de 18 a 29 com fator de atividade fisica (faf_l) leve, moderado e intenso
if sexo=="M" and idade>=18 and idade<30 and faf_l==1:
    fom_basal=(15.4*peso)-(27*altura) + 717
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))#leve

elif sexo=="M" and idade>=18 and idade<30 and faf_l==2:
    fom_basal=(15.4*peso)-(27*altura) + 717
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))#moderado

elif sexo=="M" and idade>=18 and idade<30 and faf_l==2:
    fom_basal=(15.4*peso)-(27*altura) + 717
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*2.10))#intenso


# Abaixo homens de 30 a 59 com fator de atividade fisica (faf_l) leve, moderado e intenso
elif sexo=="M" and idade>=30 and idade<60 and faf_l==1:
    fom_basal=(11.3*peso)+(16*altura) + 901
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))#leve

elif sexo=="M" and idade>=30 and idade<60 and faf_l==2:
    fom_basal=(11.3*peso)+(16*altura) + 901
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))#moderado

elif sexo=="M" and idade>=30 and idade<60 and faf_l==3:
    fom_basal=(11.3*peso)+(16*altura) + 901
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*2.10))#intenso
    

# Abaixo homens acima de 60 anos com fator de atividade fisica (faf_l) leve, moderado e intenso
elif sexo=="M" and idade>=60 and faf_l==1:
    fom_basal=(8.8*peso)+(1128*altura) - 1071 
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.56))#leve

elif sexo=="M" and idade>=60 and faf_l==2:
    fom_basal=(8.8*peso)+(1128*altura) - 1071 
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal*1.78))#moderado

elif sexo=="M" and idade>=60 and faf_l==3:
    fom_basal=((8.8*peso)+(1128*altura) - 1071) * 2.1 
    print (f"Seu gasto energético diario é de: %.0f"% (fom_basal))#intenso
    
import pandas as pd
alimentos = pd.read_sql('SELECT * FROM ALIMENTOS_TACO', conexao)
alimentos = alimentos.rename(columns={'COLUMN2': 'Alimento', 'COLUMN4' : 'Cal_100'})

vetor_alimentos = list(alimentos['Alimento'].values)
vetor_cal_100 = list(alimentos['Cal_100'].values)
tentar_dnv = True
energia_consumida = 0

while tentar_dnv:
    try:
        comida = input('digite a comida')
        qtde = float(input('digite a quantidade em gramas'))
        energia_consumida = 0

        if comida in vetor_alimentos:
            i= vetor_alimentos.index(comida) 
            energia_alimento = (qtde * float(vetor_cal_100[i])) /100
            energia_consumida += energia_alimento
        else:
            print ('Esse alimento nao esta na lista')
        tentar_dnv = input ('Voce quer colocar outro alimentos? (S) ou (N)').upper()
        if tentar_dnv == 'N':
            tentar_dnv = False
    except ValueError:
        print ('somente numeros em quantidade consumida')

if energia_consumida > fom_basal:
    print ('Você está consumindo mais calorias que você gasta.Seu gasto energetico foi de {} kcal, e você consumiu {} kcal '.format(fom_basal,energia_consumida))

elif energia_consumida < fom_basal:
    print ('Você está consumindo menos calorias que você gasta.Seu gasto energetico foi de {} kcal, e você consumiu {} kcal '.format(fom_basal,energia_consumida))
    
else:
    print ('Você está consumindo a quantidade ideal.Seu gasto energetico foi de {} kcal, e você consumiu {} kcal '.format(fom_basal,energia_consumida))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:




