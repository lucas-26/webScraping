vet = []
aux1 = []
aux2 = []
p = 0
h = 0
count = 0 
tamanho = 0
meio = 0
n = int(input("Digite o tamanho do vetor que deseja criar: "))
j = n - 1
while count <= j:
  count += 1
  vet.append(int(input("Digite um valor inteiro: ")))
a = int(input("Digite qual valor deseja buscar: "))
tamanho = len(vet)
meio = int(tamanho / 2)
l = meio
if a > vet[meio]:
  while len(vet) > l:
    aux1.append(vet[l])
    l += 1
  for encontre in aux1:
    print("comparando valor ", encontre, "com valor", a)
    if encontre == a:
      print("valor", encontre, "encontrado")
      break
else:
  l = 0
  while meio > l:
    aux2.append(vet[l])
    l += 1
  for encontre in aux2:
    print("comparando valor ", encontre, "com valor", a)
    if encontre == a:
      print("valor", encontre, "encontrado")
      break
      
    

