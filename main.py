
from repertorio_bot_sucesso_silencioso import (
    frases_impacto,
    frases_direct,
    respostas_comentario,
    legendas_bom_dia,
    legendas_motivacional,
    legendas_vitoria,
    hashtags_virais,
    chamada_afiliado
)
import random
import time

# Exemplo de uso dos repertórios
def executar_bot():
    print("Comentário aleatório:", random.choice(frases_impacto))
    print("Mensagem para DM:", random.choice(frases_direct).format(link=chamada_afiliado))
    print("Legenda da manhã:", random.choice(legendas_bom_dia))
    print("Hashtags virais:", ' '.join(random.sample(hashtags_virais, 5)))

if __name__ == "__main__":
    while True:
        executar_bot()
        time.sleep(300)  # Espera 5 minutos entre cada execução
