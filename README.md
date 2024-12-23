# Criação e Resolução de Labirintos

<div align="center">
  <img src="https://img.shields.io/badge/Versão-1.0-blue.svg" alt="Versão 1.0">
  <img src="https://img.shields.io/badge/Licença-MIT-green.svg" alt="Licença MIT">
</div>

---

## Resumo do Trabalho

> **[O objetivo deste trabalho é desenvolver um sistema que permita a criação, visualização e resolução de labirintos utilizando algoritmos computacionais e interfaces interativas. O projeto engloba três etapas principais: a geração de labirintos de forma procedural, utilizando métodos como busca em profundidade com backtracking para criar labirintos únicos e estruturados; a resolução automática dos labirintos, implementando algoritmos de busca, como o BFS (Busca em Largura), para encontrar o caminho entre o ponto inicial e o objetivo; e a interação do usuário, que pode controlar manualmente o agente dentro do labirinto ou observar a resolução automática animada. Esse trabalho combina lógica algorítmica, manipulação de estruturas de dados e visualização gráfica, promovendo a integração entre teoria de grafos e programação prática para resolver desafios de navegação e busca em espaços complexos.]**

## Descrição

> **[ 1. Geração do Labirinto
Objetivo:
Criar um labirinto único e estruturado de forma procedural, garantindo a navegabilidade entre o ponto inicial e o objetivo.

Metodologia:
O labirinto é gerado usando o algoritmo de busca em profundidade com backtracking, que constrói caminhos de forma recursiva, removendo paredes para criar passagens.
Cada célula do labirinto contém informações sobre suas paredes (cima, baixo, esquerda, direita), que determinam as conexões entre as células vizinhas.
Os dados do labirinto são exportados em formato JSON (walls_data.json), contendo as coordenadas e o estado das paredes de cada célula. Isso permite a reutilização dos dados por outros módulos do sistema.
Visualização:
Durante a geração, o labirinto é desenhado na tela utilizando a biblioteca Pygame, com células representadas por blocos e paredes desenhadas como linhas.
O processo de geração é animado, permitindo que o usuário acompanhe a construção em tempo real.
2. Resolução do Labirinto
Modo Automático: Resolução com BFS
O labirinto é tratado como um grafo, onde cada célula é um nó e cada passagem (ausência de parede) é uma aresta.
O algoritmo Busca em Largura (BFS) é utilizado para encontrar o caminho mais curto entre o ponto inicial e o objetivo.
A BFS percorre o grafo camada por camada, garantindo que o primeiro caminho encontrado seja o mais curto.
A resolução gera uma lista de coordenadas que representa o caminho percorrido do início ao objetivo.
Caso o objetivo não seja acessível (labirinto desconectado), o sistema informa que o objetivo não pode ser alcançado.
Modo Manual: Controle pelo Usuário
O usuário pode controlar manualmente o agente no labirinto utilizando as teclas direcionais ou WASD.
A movimentação do agente é limitada pela presença de paredes, garantindo que ele só possa se mover para células conectadas.
Cada movimento do agente é registrado, e o caminho percorrido é destacado na interface para facilitar a visualização.
3. Visualização Gráfica
Objetivo:
Fornecer uma interface intuitiva que permita acompanhar tanto a geração quanto a resolução do labirinto.

Funcionalidades:
O labirinto é desenhado em uma janela interativa, com células, paredes, e o agente sendo representados graficamente.
No modo automático, o caminho percorrido pelo agente é animado, destacando as células visitadas.
No modo manual, o agente se move em tempo real, com o caminho percorrido sendo marcado na tela.
Cores diferenciadas são usadas para destacar elementos como o ponto inicial, o objetivo, o agente e as células visitadas.]**

## Estrutura do Repositório 

- **`/Relatórios/`**: Documentações adicionais (diagramas, relatórios, manuais).
- **`/código/`**: Código-fonte principal.
---

## Autores

- [Emanuel Lopes Silva](emanuel.silva@discente.ufma.br)  
- [Letícia Delfino  de Araújo](ld.araujo@discente.ufma.br)  
- [Thales Aymar Fortes de Souza](thales.aymar@discente.ufma.br)  
---

## Agradecimentos

- **Universidade Federal do Maranhão (UFMA)**  
- **Professor Doutor Thales Levi Azevedo Valente**  
- **Colegas de curso**

Agradecemos a todas as pessoas e instituições que contribuíram para a realização deste trabalho.

---

## Outros Repositórios

> **[Liste aqui os links para outros repositórios que fazem parte do seu portfólio ou que complementam este projeto. Exemplo:]**

- https://github.com/EmanuelSilva69/Formigueiro-em-Netlogo

---

## Copyright / License

Este material é resultado de um trabalho acadêmico para a disciplina ** INTELIGÊNCIA ARTIFICIAL**, sob a orientação do professor **Dr. THALES LEVI AZEVEDO VALENTE**, no semestre letivo **2024.2**, do curso de **Engenharia da Computação** na Universidade Federal do Maranhão (**UFMA**).

Todo o material sob esta licença é **software livre**: pode ser usado para fins acadêmicos e comerciais **sem nenhum custo**. Não há papelada, nem royalties, nem restrições de “copyleft” do tipo GNU. Ele é licenciado sob os termos da **Licença MIT**, reproduzida abaixo, e, portanto, é compatível com a GPL e também se qualifica como software de código aberto. É de domínio público. O espírito desta licença é que você é livre para usar este material para qualquer finalidade, sem nenhum custo. O único requisito é que, se você usá-lo, nos dê crédito.



Copyright © 202X Material Educacional

Este material está licenciado sob a Licença MIT. É permitido o uso, cópia, modificação, e distribuição deste material para qualquer fim, desde que acompanhado deste aviso de direitos autorais.

O MATERIAL É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM HIPÓTESE ALGUMA OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ATO ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE, OU EM CONEXÃO COM O MATERIAL OU O USO OU OUTRAS NEGOCIAÇÕES NO MATERIAL.

Para mais informações sobre a Licença MIT: https://opensource.org/licenses/MIT.

Copyright © 202X Educational Material

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Para mais informações sobre a **Licença MIT**: [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

---

<div align="center">
Feito com ♥ por <strong>Alunos UFMA</strong>
</div>
