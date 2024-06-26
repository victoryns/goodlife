# Projeto: Programa de Cronograma Saudável

## Objetivo

Desenvolver uma aplicação que ajude os usuários a montar um cronograma saudável, incluindo atividades físicas e plano alimentar diário, personalizado com base nas preferências e informações físicas do usuário. Este projeto está alinhado com o **ODS 3 - Saúde e Bem-Estar**, promovendo hábitos de vida mais saudáveis.

## Problema

Muitas pessoas têm dificuldade em manter um estilo de vida saudável devido à falta de orientação personalizada e organizada. Isso inclui dificuldades em planejar refeições equilibradas e escolher atividades físicas adequadas. A solução de software planejada visa resolver esses problemas fornecendo um cronograma personalizado para cada usuário, ajudando-os a seguir um estilo de vida mais saudável.

## Tipo de Solução

A solução será uma **aplicação de terminal** desenvolvida em **Python** que permitirá aos usuários:

- **Registrar suas informações pessoais** (nome, idade, peso, altura, etc.).
- **Escolher atividades físicas** de sua preferência.
- Receber um **plano alimentar diário** baseado nas informações fornecidas.
- **Visualizar e seguir um cronograma diário** de atividades físicas e refeições.

## Requisitos

### Requisitos Funcionais

- **Cadastro de Usuário:** O sistema deve permitir o cadastro de informações pessoais do usuário (nome, idade, peso, altura).
- **Cadastro de Alimentos:** O sistema deve permitir o cadastro de alimentos com informações nutricionais.
- **Cadastro de Atividades:** O sistema deve permitir o cadastro de atividades físicas.
- **Escolha de Atividades:** O sistema deve permitir que o usuário escolha atividades físicas de sua preferência.
- **Montagem do Cronograma:** O sistema deve gerar um cronograma diário com plano alimentar e atividades físicas baseado nas informações do usuário.
- **Visualização do Cronograma:** O sistema deve permitir que o usuário visualize seu cronograma diário.

### Requisitos Não Funcionais

- **Usabilidade:** O sistema deve ser fácil de usar, com uma interface de linha de comando simples e intuitiva.
- **Desempenho:** O sistema deve ser rápido na montagem e visualização do cronograma.
- **Segurança:** O sistema deve garantir a segurança e privacidade dos dados pessoais dos usuários.
- **Portabilidade:** O sistema deve ser compatível com diferentes sistemas operacionais onde o Python pode ser executado.

## Diagrama de Caso de Uso

```mermaid
usecaseDiagram
    actor "Usuário" as Usuario
    actor "Administrador" as Administrador

    Usuario -> (Registrar Informações Pessoais)
    Usuario -> (Escolher Atividades Físicas)
    Usuario -> (Visualizar Cronograma)
    
    Administrador -> (Cadastrar Alimentos)
    Administrador -> (Cadastrar Atividades)

    (Registrar Informações Pessoais) --> (Montar Cronograma)
    (Escolher Atividades Físicas) --> (Montar Cronograma)
    (Cadastrar Alimentos) --> (Montar Cronograma)
    (Cadastrar Atividades) --> (Montar Cronograma)
    (Montar Cronograma) --> (Visualizar Cronograma)
