```mermaid
C4Container
    System_Boundary(health_app, "Health App") {
        Container(usuarios, "Usuarios", "List of users")
        Container(alimentos, "Alimentos", "List of foods")
        Container(atividades, "Atividades", "List of activities")
        Container(health_app_core, "Health App Core", "Core logic of the app") {
            Component(cadastrar_usuario, "Cadastrar Usuário", "Register a new user")
            Component(cadastrar_alimento, "Cadastrar Alimento", "Register a new food")
            Component(cadastrar_atividade, "Cadastrar Atividade", "Register a new activity")
            Component(escolher_atividades, "Escolher Atividades", "Choose activities for a user")
            Component(calcular_calorias_diarias, "Calcular Calorias Diárias", "Calculate daily calories for a user")
            Component(montar_cronograma, "Montar Cronograma", "Create a meal plan for a user")
            Component(visualizar_cronograma, "Visualizar Cronograma", "Display a user's meal plan")
        }
        Container(menu, "Menu", "User interface") {
            Component(menu, "Menu", "Display menu options to the user")
        }
    }

    Rel(usuarios, health_app_core, "Uses")
    Rel(alimentos, health_app_core, "Uses")
    Rel(atividades, health_app_core, "Uses")
    Rel(health_app_core, menu, "Uses")