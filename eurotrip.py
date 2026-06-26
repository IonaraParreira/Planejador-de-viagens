# 1. Planejamento da Eurotrip( Lista de Tuplas: (País/Cidade,Dias, Custo Estimado por Dia em Reais))
# Usando conteúdo aprendido - estruturas com tuplas ( )
roteiro_europa = [
    ("França (Paris)", 5, 650.0),
    ("Itália (Roma)",5, 500.0),
    ("Portugal (Lisboa)", 4, 450.0)
]
print()
print("--------- Meu Planejador de Viagem: Europa ---------")
print()
# 2. Usando conteúdo aprendido - operador 'in' e métodos de lista
# Para adicionar + países
novos_destinos = [("Espanha (Madri)", 4, 480.0), ("França (Paris)",5,650.0)]

for destino in novos_destinos:
    pais_cidade, dias, custo = destino
    destinos_atuais = [item[0] for item in roteiro_europa]

# 3. Usando o pop() para retirar o último item da lista de novos destinos para analisar separado
destino_suspenso = novos_destinos.pop()
print(f"🧹 {destino_suspenso[0]} país repetido não foi adicionado da lista de novos destinos.")

# 4. Usando o remove() caso eu mude de ideia sobre algum país específico
# Removendo ex: Espanha(Madri) para teste
for item in novos_destinos:
    if item[0] == "Espanha (Madri)":
        novos_destinos.remove(item)
        print(f"❌ {item[0]} foi retirado da lista.")
        break

    # Impede destinos duplicados usando o operador 'in'
    if pais_cidade not in destinos_atuais:
        # Usando append() para adicionar ao fim da jornada
        roteiro_europa.append(destino)
        print()
        print(f"✈️  {pais_cidade} adicionado com sucesso ao roteiro!")

# 5. Organizando os destinos por custo usando 'sort()'
# Ordenando o começo da viagem pelos países onde o custo diário é menor
roteiro_europa.sort(key=lambda x: x[2])

# 6. Loops,Desempacotamento de Tuplas e Cálculo do Custo Total
custo_total_eurotrip = 0
total_dias = 0
print("--------------------------------------------------------")
print("🗺️  ROTEIRO PREVISTO PARA A EUROPA")
print()
for parada in roteiro_europa:
    # Desempacotamento de tuplas
    local, dias, custo_diario = parada
    custo_local = dias * custo_diario
    custo_total_eurotrip += custo_local
    total_dias += dias

    print(f"🏰 {local:<18} | {dias} dias | Diária: R$ {custo_diario:.2f} | Total: R$ {custo_local:.2f}")

# Adicionando uma estimativa para as passagens aéreas internacionais
custo_passagens = 5000.0
meta_financeira_total = custo_total_eurotrip + custo_passagens

print("------------------------------------------------------")
print(f"🎫 Estimativa de Passagens Aéreas: R$ {custo_passagens:.2f}")
print(f"💰 Custo Total Estimado da Viagem: R$ {meta_financeira_total:.2f}")
print(f"📅 Duração da Eurotrip: {total_dias} dias")
print("==============================================")

# 5. Novo: Sistema de Metas e Simulação de Economia Mensal
print("\n ==============================================")
print("📊 Plano Financeiro para Realização do Sonho")
print("================================================")

# Definindo aqui quanto consigo guardar por mês 
guardado_por_mes = 600.0
total_poupado = 0
meses = 0

print(f"🎯 Meta Financeira: R$ {meta_financeira_total:.2f}")
print(f"💵 Guardando mensalmente: R$ {guardado_por_mes:.2f}")
print("\n📈 Projeção de evolução do seu fundo de viagem:")

# Loop para calcular o progresso mês a mês até atingir o objetivo
while total_poupado < meta_financeira_total:
    meses += 1
    total_poupado += guardado_por_mes

    #Exibe o progresso a cada 6 meses para o relatório não ficar gigante
    if meses % 6 == 0 or total_poupado >= meta_financeira_total:
        print(f" -> Mês {meses:02d}: Você já terá R$ {total_poupado:.2f}")

# Convertendo o total de meses para anos e meses
anos_necessarios = meses // 12
meses_restantes = meses % 12

print("-----------------------------------------------")
print(f"🎉 Objetivo alcançado em {meses} meses!")
if anos_necessarios > 0:
    print(f"⏳ Tempo estimado: {anos_necessarios} ano(s) e {meses_restantes} mês(es) de foco.")
else:
    print(f"⏳ Tempo estimado: {meses_restantes} meses de foco.")
print("================================================")    