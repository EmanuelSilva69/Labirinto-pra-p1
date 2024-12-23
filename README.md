# Criação e Resolução de Labirintos

<div align="center">
  <img src="https://img.shields.io/badge/Versão-1.0-blue.svg" alt="Versão 1.0">
  <img src="https://img.shields.io/badge/Licença-MIT-green.svg" alt="Licença MIT">
</div>

---
## Atenção!!
> **Caso tente rodar o código sem baixar o arquivo.json dentro da pasta código, O Main irá criar 2 labirintos. A primeira criará os arquivos necessários, a 2º funcionará normalmente.**

## Resumo do Trabalho

> **O objetivo deste trabalho é desenvolver um sistema que permita a criação, visualização e resolução de labirintos utilizando algoritmos computacionais e interfaces interativas. O projeto engloba três etapas principais: a geração de labirintos de forma procedural, utilizando métodos como busca em profundidade com backtracking para criar labirintos únicos e estruturados; a resolução automática dos labirintos, implementando algoritmos de busca, como o BFS (Busca em Largura), para encontrar o caminho entre o ponto inicial e o objetivo; e a interação do usuário, que pode controlar manualmente o agente dentro do labirinto ou observar a resolução automática animada. Esse trabalho combina lógica algorítmica, manipulação de estruturas de dados e visualização gráfica, promovendo a integração entre teoria de grafos e programação prática para resolver desafios de navegação e busca em espaços complexos.**

## Descrição

> **Este trabalho tem como objetivo principal desenvolver um sistema completo para a criação, resolução e visualização de labirintos, integrando algoritmos computacionais eficientes e uma interface gráfica interativa. O projeto abrange a geração procedural de labirintos, utilizando o algoritmo de busca em profundidade com backtracking, que constrói caminhos de forma recursiva, removendo paredes para criar passagens. Cada célula do labirinto contém informações sobre suas paredes, que determinam as conexões entre células vizinhas, e os dados gerados são exportados em formato JSON (`walls_data.json`), permitindo que outros módulos do sistema reutilizem essas informações. Durante a geração, o processo é animado em tempo real com o uso da biblioteca Pygame, oferecendo uma visualização dinâmica e intuitiva da construção do labirinto.**

> **A resolução do labirinto pode ser realizada de duas maneiras: de forma automática ou manual. No modo automático, o algoritmo de Busca em Largura (BFS) é implementado para encontrar o caminho mais curto entre o ponto inicial e o objetivo, garantindo uma solução eficiente e clara. O caminho encontrado é animado na interface gráfica, destacando o percurso do início ao fim. Já no modo manual, o usuário pode controlar diretamente o agente dentro do labirinto utilizando teclas direcionais ou `WASD`. Nesse caso, a movimentação do agente é limitada pelas paredes do labirinto, e cada célula visitada é visualmente destacada, permitindo ao usuário explorar e resolver o labirinto por conta própria.**

> **A interface gráfica desempenha um papel central, proporcionando uma experiência interativa e visualmente rica. O labirinto, suas paredes, o agente e o objetivo são representados graficamente, com cores distintas para destacar os elementos. O caminho percorrido pelo agente, tanto no modo automático quanto no manual, é exibido em tempo real, oferecendo ao usuário uma visão clara do progresso. A modularidade do sistema é garantida pela divisão do projeto em diferentes arquivos e funções, incluindo a geração do labirinto (`GerarMaze.py`), a resolução com BFS (`Breadth_First_Search.py`), o controle do agente (`agente.py`) e o fluxo principal (`main.py`), que orquestra a execução de todas as partes.**

> **Esse trabalho combina teoria de grafos, algoritmos de busca e geração procedural, além de programação gráfica, para criar um sistema robusto e versátil. As aplicações práticas incluem jogos, onde mapas dinâmicos e interativos são necessários, ensino de algoritmos fundamentais de ciência da computação e até simulações para navegação em robótica. Ao integrar essas técnicas, o projeto oferece uma solução completa para explorar conceitos fundamentais e avançados de computação, promovendo aprendizado e inovação em áreas como navegação, simulação e design procedural.**

## Estrutura do Repositório 

- **`/Relatório/`**: Documentações adicionais (diagramas, relatórios, manuais).
- **`/código/`**: Código-fonte principal.
---
## Requisitos :
> **Instalar o Pygame**

> **pip install pygame**

>**Rodar o GerarMaze inicialmente para gerar os dados necessários.**
----------------------------------------
**https://github.com/pygame/pygame**

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


- https://github.com/EmanuelSilva69/Formigueiro-em-Netlogo

---

## Copyright / License

Este material é resultado de um trabalho acadêmico para a disciplina **INTELIGÊNCIA ARTIFICIAL**, sob a orientação do professor **Dr. THALES LEVI AZEVEDO VALENTE**, no semestre letivo **2024.2**, do curso de **Engenharia da Computação** na Universidade Federal do Maranhão (**UFMA**).

Todo o material sob esta licença é **software livre**: pode ser usado para fins acadêmicos e comerciais **sem nenhum custo**. Não há papelada, nem royalties, nem restrições de “copyleft” do tipo GNU. Ele é licenciado sob os termos da **Licença MIT**, reproduzida abaixo, e, portanto, é compatível com a GPL e também se qualifica como software de código aberto. É de domínio público. O espírito desta licença é que você é livre para usar este material para qualquer finalidade, sem nenhum custo. O único requisito é que, se você usá-lo, nos dê crédito.



Copyright © 2024 Material Educacional

Este material está licenciado sob a Licença MIT. É permitido o uso, cópia, modificação, e distribuição deste material para qualquer fim, desde que acompanhado deste aviso de direitos autorais.

O MATERIAL É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM HIPÓTESE ALGUMA OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ATO ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE, OU EM CONEXÃO COM O MATERIAL OU O USO OU OUTRAS NEGOCIAÇÕES NO MATERIAL.

Para mais informações sobre a Licença MIT: https://opensource.org/licenses/MIT.

Copyright © 2024 Educational Material

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Para mais informações sobre a **Licença MIT**: [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

---

<div align="center">
Feito com ♥ por <strong>Alunos UFMA</strong>
</div>
