# Importa a biblioteca Dear PyGui e a renomeia como 'dpg'
import dearpygui.dearpygui as dpg

# Cria um contexto para Dear PyGui, que é necessário para iniciar qualquer aplicação usando esta biblioteca
dpg.create_context()

# Definição da função que será chamada quando o usuário clicar no botão de calcular
def calcular_preco():
    # Obtém os valores inseridos nos campos de texto da interface
    preco_fipe = dpg.get_value("preco_fipe")
    nota_avaliacao = dpg.get_value("nota_avaliacao")
    
    try:
        # Tenta converter os valores obtidos para os tipos numéricos adequados
        preco_fipe = float(preco_fipe)
        nota_avaliacao = int(nota_avaliacao)

        # Avalia a nota de avaliação e calcula o preço final baseado nela
        if 0 <= nota_avaliacao < 50:
            preco_final = preco_fipe * 0.8  # Reduz o preço em 20%
        elif 50 <= nota_avaliacao < 80:
            preco_final = preco_fipe  # Mantém o preço
        elif 80 <= nota_avaliacao <= 100:
            preco_final = preco_fipe * 1.2  # Aumenta o preço em 20%
        else:
            # Define uma mensagem de erro se a nota estiver fora do intervalo válido
            preco_final = "Erro: A nota de avaliação deve estar entre 0 e 100"
        
        # Configura o valor do texto de resultado na interface com o preço final ou mensagem de erro
        dpg.set_value("resultado", f"Preço final do veículo: R${preco_final:,.2f}")
    except ValueError:
        # Define uma mensagem de erro se os valores inseridos não puderem ser convertidos para numéricos
        dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

# Cria uma janela para visualização da aplicação com um título e dimensões definidas
dpg.create_viewport(title='Calculadora de Preco de Veeculos', width=700, height=300)

# Define a janela principal onde os elementos da interface serão colocados
with dpg.window(label="Calculadora FIPE", width=700, height=300):
    # Adiciona um campo de texto para o usuário inserir o preço FIPE
    dpg.add_input_text(label="Preço FIPE (R$):", tag="preco_fipe")
    # Adiciona um campo de texto para o usuário inserir a nota de avaliação
    dpg.add_input_text(label="Nota de Avaliação (0-100):", tag="nota_avaliacao")
    # Adiciona um botão que, quando clicado, chama a função 'calcular_preco'
    dpg.add_button(label="Calcular Preço", callback=calcular_preco)
    # Adiciona um espaço para exibir o resultado ou mensagens de erro
    dpg.add_text("", tag="resultado")

# Configura e mostra a janela
dpg.setup_dearpygui()
dpg.show_viewport()
# Inicia o loop de eventos da interface, onde a aplicação efetivamente roda e espera por interações do usuário
dpg.start_dearpygui()
# Destroi o contexto da aplicação após o fechamento da janela, liberando recursos
dpg.destroy_context()
