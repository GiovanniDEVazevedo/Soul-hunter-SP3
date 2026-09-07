
olhos = {
    "olho1": {
        'url':"exemplo.com", 
        'descricao': "olho exemplo"
        },
    "olho2":{
        'url':"exemplo.com2", 
        'descricao': "olho exemplo2"
    },
    "olho3": {
            'url':"exemplo.com3", 
            'descricao': "olho exemplo3"
    }, 
}
bocas = {
    'boca1': {
        'url': "exemplo.com/boca1",
        'descricao': "exemplo boca1"
    },
    'boca2': {
            'url': "exemplo.com/boca2",
            'descricao': "exemplo boca2"
        },
    'boca3': {
            'url': "exemplo.com/boca3",
            'descricao': "exemplo boca3"
        },
}
corpos ={
    'corpo1': {
        'url': "exemplo.com/corpo",
        'descricao':"exemplo corpo 1"
    },
    'corpo2': {
            'url': "exemplo.com/corpo",
            'descricao':"exemplo corpo 2"
        },
    'corpo3': {
            'url': "exemplo.com/corpo",
            'descricao':"exemplo corpo 3"
        },
}
acessorios = {
    'acessorio':{
        'url': "exemplo.com/acessorio",
        'descricao': "exemplo acessorio"
    },
    'acessorio2':{
            'url': "exemplo.com/acessorio",
            'descricao': "exemplo acessorio2"
        },
    'acessorio3':{
            'url': "exemplo.com/acessorio",
            'descricao': "exemplo acessorio3"
        },
}
auras = {
    'aura1':{
        "url": "exemplo.com/aura",
        'descricao':"exemplo aura"
    },
    'aura2':{
            "url": "exemplo.com/aura",
            'descricao':"exemplo aura2"
        },
    'aura3':{
            "url": "exemplo.com/aura",
            'descricao':"exemplo aura3"
        },
}
efeitos = {
    'efeito1':{
        'url':"exemplo.com/efeito",
        'descricao':"exemplo efeito"
    },
    'efeito2':{
            'url':"exemplo.com/efeito",
            'descricao':"exemplo efeito2"
        },
    'efeito3':{
            'url':"exemplo.com/efeito",
            'descricao':"exemplo efeito3"
        },
}
import random
def sortear_partes(raridade):

    fantasma = {}

    # Partes básicas
    fantasma["corpo"] = random.choice(list(corpos.keys()))
    fantasma["olho"] = random.choice(list(olhos.keys()))
    fantasma["boca"] = random.choice(list(bocas.keys()))

    if raridade == "COMUM":
        pass

    elif raridade == "RARO":
        fantasma["acessorios"] = random.sample(
            list(acessorios.keys()),1
        )

    elif raridade == "EPICO":
        fantasma["acessorios"] = random.sample(
            list(acessorios.keys()),
            2
        )

        fantasma["aura"] = random.choice(
            list(auras.keys())
        )

    elif raridade == "LENDARIO":
        fantasma["acessorios"] = random.sample(
            list(acessorios.keys()),
            2
        )

        fantasma["aura"] = random.choice(
            list(auras.keys())
        )

        fantasma["efeito"] = random.choice(
            list(efeitos.keys())
        )

    return fantasma

