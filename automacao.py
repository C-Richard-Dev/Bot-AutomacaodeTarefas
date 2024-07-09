import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1.5

# passo 1: entrar no sistema da empresa
pyautogui.click(x=1238, y=23)
pyautogui.press('win')
time.sleep(6.0)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(9.0)
pyautogui.click(x=304, y=646)
time.sleep(4.0)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(6.0)

# passo 2: fazer login
pyautogui.click(x=322, y=405)
pyautogui.write('teste.@email.com')
pyautogui.press('tab')
time.sleep(1.0)
pyautogui.click(x=281, y=504)
pyautogui.write('12345')
pyautogui.press('tab')
pyautogui.press('enter')

# passo 3: importar base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)

# função para apagar o campo atual
def clear_field():
    pyautogui.hotkey('ctrl', 'a')


# passo 4: cadastrar produto
for index, row in tabela.iterrows():
    pyautogui.click(x=348, y=271)
    clear_field()
    pyautogui.write(str(row["codigo"]))
    pyautogui.press("tab")
    clear_field()
    pyautogui.write(str(row["marca"]))
    pyautogui.press("tab")
    clear_field()
    pyautogui.write(str(row["tipo"]))
    pyautogui.press("tab")
    clear_field()
    pyautogui.write(str(row["categoria"]))
    pyautogui.press("tab")
    clear_field()
    pyautogui.write(str(row["preco_unitario"]))
    pyautogui.press("tab")
    clear_field()
    pyautogui.write(str(row["custo"]))
    pyautogui.press("tab")
    clear_field()
    obs = row["obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até o fim

