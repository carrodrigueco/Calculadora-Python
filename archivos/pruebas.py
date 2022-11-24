import pandas as pd
dataframe = pd.read_csv("")
columnas_valores = ["Valor del Contrato", "Valor de pago adelantado", "Valor Pendiente de pago", "Valor Pagado"]
valores =  dataframe[columnas_valores].copy()
print(valores)