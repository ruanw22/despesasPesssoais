import pandas as pd

def criar_dataframe():
    colunas = ['Data', 'Categoria', 'Descrição', 'Valor']
    return pd.DataFrame(columns=colunas)

def adicionar_despesa(df, data, categoria, descricao, valor):
    nova_despesa = pd.DataFrame([[data, categoria, descricao, valor]], columns=df.columns)
    
    if df.empty:
        df = nova_despesa
    else:
        df = pd.concat([df, nova_despesa], ignore_index=True)
    
    return df

def relatorio_por_categoria(df):
    relatorio = df.groupby('Categoria').sum()['Valor']
    return relatorio

def relatorio_mensal(df):
    df['Data'] = pd.to_datetime(df['Data'])
    df['AnoMes'] = df['Data'].dt.to_period('M')
    relatorio = df.groupby('AnoMes')['Valor'].sum()
    return relatorio

def exibir_relatorio_completo(df):
    print("Relatório por Categoria:")
    relatorio_categoria = relatorio_por_categoria(df)
    for categoria, valor in relatorio_categoria.items():
        print(f"{categoria}: R$ {valor:.2f}")
    
    print("\nRelatório Mensal:")
    relatorio_mensal_resultado = relatorio_mensal(df)
    for mes, valor in relatorio_mensal_resultado.items():
        print(f"{mes}: R$ {valor:.2f}")

# Exemplo de uso
if __name__ == "__main__":
    # Criar o DataFrame
    df_despesas = criar_dataframe()
    
    # Adicionar algumas despesas
    df_despesas = adicionar_despesa(df_despesas, '2024-08-01', 'Alimentação', 'Supermercado', 150.00)
    df_despesas = adicionar_despesa(df_despesas, '2024-08-03', 'Transporte', 'Combustível', 200.00)
    df_despesas = adicionar_despesa(df_despesas, '2024-08-05', 'Lazer', 'Cinema', 50.00)
    df_despesas = adicionar_despesa(df_despesas, '2024-08-10', 'Alimentação', 'Restaurante', 80.00)
    
    # Exibir o relatório completo
    exibir_relatorio_completo(df_despesas)
