# Projeto de automação 
## Desafio:
Este projeto de automação foi um resultado de um desafio utilizando a linguagem python com o intuito de aprender a controlar o mouse e o teclado para que executem tarefas como se fosse você. A ideia do projeto é que você consiga entrar em um site, fazer seu login e fazer o cadastro de todos os produtos de forma automática.
### Descrição:
 Em uma situação hipotética, imagine que você tem 500 informações, seria um tanto trabalhoso ter que fazer tudo isso de forma manual não é mesmo?
### Instrução:
Os dados que foram utilizados são as informações que estão dentro do arquivo produtos.csv. Nesse arquivo temos diversos produtos para serem cadastrados no sistema de forma automática. É provável que terá uma lista dos itens que precisa cadastrar quando for fazer um procedimento similar, condorda? Então, temos exatamente essa lista (que é uma base de dados) com as informações a serem cadastradas.

_![Imagem de produtos](https://github.com/user-attachments/assets/b3afeb78-96c2-4a59-b344-820a0a67c9e6)

Está descrito o código do produto, marca, tipo, preço unitário, custo e observação.Porém, as informações estão no formato csv, dificultando um pouco a visualização.  Outro fator importante é que temos 264 linhas de informação, portanto,teria que preencher 6 informações no sistema para cada linha da base de dados.Com o objetivo de evitar esse tipo de trabalho manual é que vamos criar automações com Python, simplificando e facilitando o trabalho deixando-o mais rápido, automático e sem chances de inserir informações erradas.
#### Etapas:
**Ao rodar o programa vamos ter as seguintes ações para completar o nosso cadastro:**

![imagem Etapa1](https://github.com/user-attachments/assets/e2b05c33-8a95-49b0-910c-7898d85fe26f)

![Formulário](https://github.com/user-attachments/assets/15501b81-bd3a-4340-b8ca-092ec04aafac)

    • Abrir o navegador
    • Acessar o site do sistema com login e senha
    • Inserir todas as informações do produto
    • Enviar as informações para o sistema
    • Repetir o cadastro até acabar o cadastro de todos os produtos

### Importando os dados

Utilizaremos a biblioteca pandas para importar a base de dados e visualizar como estão organizados. A base de dados é o arquivo produtos.csv, é necessário que o arquivo esteja no mesmo local em que criou o seu arquivo em Python. Assim, podemos utilizar apenas o comando pd.read_csv e colocar o nome do arquivo. Utilize o print para visualizar os dados:

```import pyautogui```
``` import pandas```
#### Importe os dados dos produtos

```tabela = pd.read_csv("produtos.csv")```
```print(tabela)```
