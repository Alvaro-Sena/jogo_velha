# Jogo da Velha com Minimax

Este projeto implementa o jogo da velha (Tic-Tac-Toe) utilizando o algoritmo Minimax para a tomada de decisões da IA. O código foi desenvolvido como parte do curso **CS50 - Introduction to Artificial Intelligence with Python**, oferecido por **Harvard University**.

## Tecnologias Utilizadas  
- **Linguagem**: Python 3  
- **Bibliotecas**:  
  - `copy` (para deepcopy de estados do tabuleiro)  
  - `math` (cálculos de valores extremos)  
- **Algoritmos/Conceitos**:  
  - Minimax com poda alpha-beta implícita  
  - Busca Adversarial em Árvore de Estados  
  - Teoria de Jogos para Decisões Ótimas  
  - Recursão Multi-nível  
  
## Estrutura do Projeto

A pasta contém os seguintes arquivos:

- **`runner.py`**: Interface gráfica para jogar o jogo da velha (fornecida pelo CS50).
- **`tictactoe.py`**: Implementação da lógica do jogo e do algoritmo Minimax.
- **Outros arquivos**: Foram fornecidos pelo curso CS50 de Harvard como base para o desenvolvimento.

## Features  
- **IA Invencível**:  
  - Implementação completa do algoritmo Minimax para decisões perfeitas  
  - Escolhe estratégias ótimas para ambos jogadores (X ofensivo, O defensivo)  
- **Mecanismos Avançados**:  
  - Detecção instantânea de vitória/empate em todas direções  
  - Sistema de otimização para primeiro movimento (prioriza canto)  
  - Validação rigorosa de jogadas inválidas  
- **Arquitetura do Sistema**:  
  - Separação clara entre:  
    - Lógica do jogo (controle de turnos/vencedor)  
    - Motor de IA (tomada de decisão estratégica)  
  - Representação eficiente de estados (matriz 3x3)  
- **Controle de Estados**:  
  - Gerenciamento completo de estados do tabuleiro  
  - Cálculo recursivo de utilidade para todas jogadas possíveis  
- **Otimizações**:  
  - Redução de complexidade por avaliação precoce de estados terminais  
  - Deepcopy seletivo para evitar alterações no estado atual  
  
## Minha Contribuição

Toda a lógica do jogo e a implementação do algoritmo Minimax foram desenvolvidas no arquivo `tictactoe.py`.

## Como Rodar o Jogo

1. Clone este repositório:
```bash
git clone https://github.com/Alvaro-Sena/jogo_velha.git 
```
2. Navegue até a pasta
```bash
cd jogo_velha/
```
3. Instale as dependências:  
 ```bash  
 pip install -r requirements.txt  
 ```  
3. Execute o jogo:  
 ```bash  
 python runner.py  
 ```

Certifique-se de que possui **Python 3** instalado no seu ambiente, bem como, instalar a biblioteca presente em requirements.txt.

## Contato
Caso tenha dúvidas ou sugestões, entre em contato através do meu [LinkedIn](www.linkedin.com/in/alvaro-sena), [GitHub](https://github.com/Alvaro-Sena) ou [WhatsApp](https://wa.me/447356040385).
