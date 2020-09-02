vet = []
count = 0 
w = 0
n = int(input("Digite o tamanho do vetor que deseja criar: "))
j = n - 1
while count <= j:
  count += 1
  vet.append(int(input("Digite um valor inteiro: ")))

a = int(input("Digite qual valor deseja buscar: "))
for valor in vet:
  w += 1
  if valor == a:
    print("valor",a,"encontrado econtrado na posicao",w)