import random
from services.rarity_service import sortear_raridade
from data.fantasma_part import sortear_partes
def gerar_fantasma(seed=None):
    if seed == None:
                seed = random.getrandbits(32)
                
    elif not isinstance(seed, int):
        raise ValueError("Seed deve ser um número inteiro")
    
    elif 0 >  seed or seed >  2**32 - 1  :
        raise ValueError("Seed esta fora da faixa de geracao") 
    
    
    random.seed(seed)

    raridade = sortear_raridade()
    partes = sortear_partes(raridade)
    return{
            'seed': seed, 'raridade': raridade, 'partes':partes
        }
    
        