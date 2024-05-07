import nltk
from nltk.chat.util import Chat, reflections

# Baixar o pacote de dados necessário
nltk.download('punkt')

# Definir pares de padrões e respostas
pares = [
    [
        r"Olá|Oi|E aí|Oi, tudo bem?",
        ["Olá! Como posso ajudar você?", "Oi! Qual é a sua dúvida?", "E aí! Em que posso ser útil?"],
    ],
    [
        r"Qual é o seu nome?",
        ["Eu sou um chatbot simples. Você pode me chamar de MiniIA.",],
    ],
    [
        r"Como você está?",
        ["Estou bem, obrigado por perguntar!", "Tudo tranquilo! Como posso ajudar você hoje?"],
    ],
    [
        r"Qual é a sua cor favorita?",
        ["Eu não tenho uma cor favorita. Estou aqui para responder suas perguntas!",],
    ],
    [
        r"Sair|Até logo",
        ["Até mais! Se precisar de algo, estarei por aqui.", "Até logo! Tenha um ótimo dia!"],
    ],
]

# Criar o chatbot
chatbot = Chat(pares, reflections)

# Iniciar o chat
print("Olá! Eu sou um chatbot. Digite 'Sair' para encerrar o chat.")
chatbot.converse()
