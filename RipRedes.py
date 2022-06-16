def adicionarLan(x):
    print(f"\n{x}º Rede LAN")
    x = str(x)
    lan = "L"+x
    roteadorLan = input(f"Roteador: ").upper()
    interfaceLan = input(f"Interface: ").upper()
    ativado = True
    return lan, roteadorLan, interfaceLan, ativado


print("ALGORITIMO RIP REDES\n")
dicAux = {}
print("- Adição dos roteadores\n")
numRoteadores = int(input("Quantos roteadores deseja colocar na rede? "))
roteadores = {}
for i in range(numRoteadores):
    x = str(i + 1)
    nomeRoteador = "R"+x
    ativado = True
    roteadores[nomeRoteador] = ativado

print("\nRoteadores adicionados")
print(roteadores)

# mudar lógica
print("\n- Criação das LANs")
lans = {}
resp = input("Deseja adicionar uma rede Lan? ").lower()
x = 1
while resp != "nao":
    lan = adicionarLan(x)
    lans[lan[0]] = (lan[1], lan[2], lan[3])
    resp = input("Deseja adicionar outra uma rede Lan? ").lower()
    x += 1

print("\n- Criação das WANs")
wans = {}

print("Roteadores disponiveis: ")
for i in roteadores:
    print(i)

for i in range(numRoteadores-1):
    print(f"\n{i+1}º Rede WAN")
    x = str(i+1)
    wan = "W"+x
    r1Wan = input("Roteador 1: ").upper()
    r1Interface = input("Interface: ").upper()
    r2Wan = input("Roteador 2: ").upper()
    r2Interface = input("Interface: ").upper()
    ativado = True
    wans[wan] = ((r1Wan, r1Interface), (r2Wan, r2Interface), ativado)

print("\n- Endereçamento de LANs e WANs")
enderecos = {}

for lan in lans:
    enderecos[lan] = input(f"\nEndereço de rede para LAN '{lan}': ")

for wan in wans:
    enderecos[wan] = input(f"\nEndereço de rede para WAN '{wan}': ")

lw = {}
lw = lans | wans

print(f"\nEndereços: {enderecos}")
print(f"Roteadores: {roteadores}")
print(f"LANs: {lans}")
print(f"WANs: {wans}")
print(f"Junção de lans e wans: {lw}")


dic1 = {}
dic2 = {}
dic3 = {}
dic4 = {}


# associando roteadores as lans
for i in enderecos:
    for x in lans:
        if i == x:
            dic1[lans.get(x)[0]] = x

# associando roteadores as wans
a = 0
for i in roteadores:
    for x in wans:
        if i == wans.get(x)[a][0]:
            dic2[i] = x
        a = +1
print(f"Dic1: {dic1}")

print(f"Dic2: {dic2}")

# associando roteadores as lans e ips
for i in enderecos:
    for x in dic1:
        if i == dic1.get(x):
            dic3[x] = dic1.get(x), enderecos.get(i)


print(f"Dic3: {dic3}")

a = 0
# associando roteadores wans e ips
for i in enderecos:
    for x in wans:
        if i == x:
            dic4[wans.get(x)[0][0]] = i, enderecos.get(i)

print(f"Dic4: {dic4}")

tabelaDeRoteamento = {}
for i in dic3:
    for j in dic3:
        if i == j:
            tabelaDeRoteamento[j] = j.get()[1], 0
        else:
            tabelaDeRoteamento[j] = j.get()[1], 0
