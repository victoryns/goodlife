# Planos de Testes da Aplicação

## Casos de Teste por Caso de Uso

### Caso de Uso: Registrar Informações Pessoais

1. **Descrição:** Testar o registro correto das informações pessoais do usuário.
   - **Pré-condição:** Usuário acessa o sistema de registro.
   - **Passos:**
     1. Usuário insere nome, idade, peso e altura.
     2. Usuário confirma o registro.
   - **Resultado Esperado:** As informações são salvas corretamente no banco de dados e podem ser recuperadas para verificação.

2. **Descrição:** Testar o comportamento do sistema com dados de entrada inválidos.
   - **Pré-condição:** Usuário acessa o sistema de registro.
   - **Passos:**
     1. Usuário insere idade como um texto em vez de um número.
     2. Usuário tenta confirmar o registro.
   - **Resultado Esperado:** Sistema valida corretamente os campos e exibe mensagem de erro para entrada inválida.

3. **Descrição:** Testar a atualização de informações pessoais existentes.
   - **Pré-condição:** Usuário acessa o sistema de perfil para atualizar informações pessoais.
   - **Passos:**
     1. Usuário modifica o peso atual.
     2. Usuário confirma a atualização.
   - **Resultado Esperado:** As informações são atualizadas corretamente no banco de dados sem afetar outros dados do usuário.

### Caso de Uso: Escolher Atividades Físicas

1. **Descrição:** Testar a seleção de atividades físicas pelo usuário.
   - **Pré-condição:** Usuário acessa a função de escolha de atividades físicas.
   - **Passos:**
     1. Usuário seleciona diferentes tipos de atividades (por exemplo, caminhada, corrida, natação).
     2. Usuário salva as escolhas.
   - **Resultado Esperado:** As atividades selecionadas são salvas no perfil do usuário e podem ser visualizadas posteriormente.

2. **Descrição:** Testar a exclusão de atividades físicas previamente selecionadas.
   - **Pré-condição:** Usuário acessa a função de escolha de atividades físicas com atividades já selecionadas.
   - **Passos:**
     1. Usuário remove uma ou mais atividades da lista de seleção.
     2. Usuário confirma a exclusão.
   - **Resultado Esperado:** As atividades removidas são atualizadas no perfil do usuário e refletem corretamente na visualização do cronograma.

3. **Descrição:** Testar o limite máximo de atividades que o usuário pode selecionar.
   - **Pré-condição:** Usuário acessa a função de escolha de atividades físicas.
   - **Passos:**
     1. Usuário tenta selecionar mais atividades do que o limite estabelecido.
   - **Resultado Esperado:** Sistema valida corretamente o número máximo de atividades permitidas e impede a seleção adicional após atingir o limite.

### Caso de Uso: Visualizar Cronograma

1. **Descrição:** Testar a visualização do cronograma diário de refeições e atividades físicas.
   - **Pré-condição:** Usuário acessa a função de visualização de cronograma.
   - **Passos:**
     1. Usuário acessa seu cronograma diário.
   - **Resultado Esperado:** O sistema exibe corretamente as refeições planejadas e atividades físicas de acordo com as escolhas do usuário.

2. **Descrição:** Testar a personalização do cronograma com base nas preferências do usuário.
   - **Pré-condição:** Usuário realiza alterações nas
