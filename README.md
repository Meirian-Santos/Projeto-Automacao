# Projeto de automação 
## Desafio:
Este projeto de automação foi um resultado de um desafio utilizando a linguagem python com o intuito de aprender a controlar o mouse e o teclado para que executem tarefas como se fosse você. A ideia do projeto é que você consiga entrar em um site, fazer seu login e fazer o cadastro de todos os produtos de forma automática.
### Descrição:
 Em uma situação hipotética, imagine que você tem 500 informações, seria um tanto trabalhoso ter que fazer tudo isso de forma manual não é mesmo?
### Instrução:
Os dados que foram utilizados são as informações que estão dentro do arquivo produtos.csv. Nesse arquivo temos diversos produtos para serem cadastrados no sistema de forma automática. É provável que terá uma lista dos itens que precisa cadastrar quando for fazer um procedimento similar, condorda? Então, temos exatamente essa lista (que é uma base de dados) com as informações a serem cadastradas.

_![Imagem de produtos](https://github.com/user-attachments/assets/b3afeb78-96c2-4a59-b344-820a0a67c9e6)

Está descrito o código do produto, marca, tipo, preço unitário, custo e observação.Porém, as informações estão no formato csv, dificultando um pouco a visualização.  Outro fator importante é que temos 264 linhas de informação, portanto,teria que preencher 6 informações no sistema para cada linha da base de dados.Com o objetivo de evitar esse tipo de trabalho manual é que vamos criar automações com Python, simplificando e facilitando o trabalho deixando-o mais rápido, automático e sem chances de inserir informações erradas.
### Etapas:
**Ao rodar o programa vamos ter as seguintes ações para completar o nosso cadastro:**

![imagem Etapa1](https://github.com/user-attachments/assets/e2b05c33-8a95-49b0-910c-7898d85fe26f)

![Formulário](https://github.com/user-attachments/assets/15501b81-bd3a-4340-b8ca-092ec04aafac)

    • Abrir o navegador
    • Acessar o site do sistema com login e senha
    • Inserir todas as informações do produto
    • Enviar as informações para o sistema
    • Repetir o cadastro até acabar o cadastro de todos os produtos

## Importando os dados

Utilizaremos a biblioteca pandas para importar a base de dados e visualizar como estão organizados. A base de dados é o arquivo produtos.csv, é necessário que o arquivo esteja no mesmo local em que criou o seu arquivo em Python. Assim, podemos utilizar apenas o comando pd.read_csv e colocar o nome do arquivo. Utilize o print para visualizar os dados:

```import pyautogui```
``` import pandas```
## Importando os dados dos produtos

```tabela = pd.read_csv("produtos.csv")```
```print(tabela)```

## Instalando a boblioteca pyautogui

Depois de ter feito a importação da biblioteca pyautogui, que é a biblioteca que vai permitir que você tenha controle do mouse e do seu teclado para fazer as automações no seu computador utilizando o Python. Para fazer a instalação da biblioteca basta abrir o seu terminal:

```pip install pyautogui``` 
## Link da documentação da biblioteca pyautogui

https://pyautogui.readthedocs.io/en/latest/

## Comandos

Os 3 comandos utilizados são:

 • Pyautogui.press – Para pressionar uma tecla do seu teclado
 
 • Pyautogui.write – Para escrever com o teclado (como se estivesse digitando em tempo real)
 
 • Pyautogui.click – Para clicar com o mouse

O será pyautogui.click será ncessário para passar uma posição x e y a partir da sua função de clique do mouse. Lembrando que a posção vai depender do tamanho do seu monitor.

## Posição do mouse

Esse é o código do arquivo pegar_posição.py, que é o código que te permite pegar a posição atual do seu mouse para que você saiba exatamente onde clicar na sua automação.

![Captura de tela 2 1](https://github.com/user-attachments/assets/6ea21a90-ef6d-42d4-b587-07172bb72a29)

![Captura de tela 2](https://github.com/user-attachments/assets/b8b612c2-9798-4889-9d38-cd1202d95768)
 _Atenção este é um código independente para pegar a posição do mouse, garantindo que vai clicar no local correto_

 ## Abrindo o Navegador
 
- Primeiramente vamos usar o comando pyautogui.PAUSE, que é para definir qual o tempo de espera entre os comandos do Pyautogui.
- Logo depois nós temos o comando pyautogui.press, para pressionar uma tecla do teclado.
- Em seguida use o “win” que é a tecla de Windows do computador, para abrirmos o menu iniciar.
- Use o comando pyautogui.write, para escrever.
- Aqui escrevi Edge que é o navegador que utilizei, mas você pode alterar para o seu navegador de preferência.
- Agora abra o navegador e escreva o link de onde o login para cadastrar os produtos serão feitos.
- Após o login tem o time.sleep para esperar que o carragamento do site para depois avançar.

![Captura de tela 4](https://github.com/user-attachments/assets/1e39f513-67b4-42ed-aed4-e2a8e8e74dc5)

## Login do sistema

![Captura de tela 5](https://github.com/user-attachments/assets/f8b5c61a-8096-4a4f-b354-7a343cd99236)

- Foi utilizado o pyautogui.click, pois já continha a posição de onde o click iria ser feito. Então é muito importante que já tenha as posições definidas de onde vai clicar tanto para 				escrever o login quanto para clicar no botão para entrar no sistema.
- O comando pyautogui.press(“tab”) tem como função a utilização da tecla tab para passar para o próximo campo, evitando dar dois cliques, e passar automaticamente para o próxi.mo campo

![Captura de tela 2024-07-17 113222](https://github.com/user-attachments/assets/da72e18d-bd35-4ce9-a79e-30e5142345f8)

## Cadastro dos produtos

- 1. Agora será feito o registro das informações no sistema. Neste momento a estrutura de repetição "_for_" será usado, percorrendo todas as linhas da base de dados para registrar cada uma das informações dos produtos e preenchendo todas as informações no sistema a partir do "_tab_" e clicando em enviar.

![Captura de tela 8](https://github.com/user-attachments/assets/09084cd6-6e33-46f7-bb80-eb331b15b657)

 - 2.0 Temos o comando de click para clicar no primeiro campo onde vamos preencher a primeira informação.
   - 2.1 Pyautogui.write – Comando para escrever.
     - 2.2 Str É um comando para transformar em string.
       - 2.3 (texto) .loc – Comando de busca de informação, neste caso dentro da nossa tabela.
         - 2.4 Buscando uma informação na linha x (dependendo de quantas vezes vai estar repetindo) na coluna “codigo”.
           - 2.5 A verificação com a estrutura condicional if (se) para se certificar que o campo de observação possui ou não alguma informação.
             - 2.6 Buscaremos se a informação de observação não está vazia, se não estiver preenchereremos o campo de obs, caso contrário, seguiremos sem fazer nada, já que nem todos os campos possuem     
              observação


