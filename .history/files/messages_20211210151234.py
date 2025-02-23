geral_faceis = [ # 60 palavras de 6 letras cada
    'teste', 'apice', 'animo', 'comum', 'graca', 'graxa', 'terra', 'corda', 'carro', 'visor', 'tampa', 'vidro', 
    'barra', 'ganso', 'manso', 'senso', 'algoz', 'nobre', 'exito', 'sagaz', 'inato', 'ideia', 'honra', 'poder',
    'sutil', 'mutua', 'afeto', 'mexer', 'aquem', 'ardil', 'corja', 'prole', 'digno', 'crivo', 'culto', 'mundo',
    'brado', 'gleba', 'tenaz', 'regra', 'saude', 'viril', 'usura', 'clava', 'pifio', 'feliz', 'heroi', 'coisa',
    'plato', 'alibi', 'fluxo', 'senil', 'lugar', 'ligar', 'crise', 'grato', 'vital', 'valor', 'olhar', 'fator',
] 

geral_medianas = [ # 63 palavras de 8 letras cada
    'inerente', 'peculiar', 'denegrir', 'respeito', 'genocida', 'anuencia', 'deferido', 'prudente', 'equidade',
    'pandemia', 'iminente', 'invasivo', 'essencia', 'desgraca', 'alienado', 'misogino', 'eminente', 'extensao',
    'abstrato', 'empirico', 'premissa', 'conceito', 'ardiloso', 'reiterar', 'ascensao', 'passivel', 'prodigio',
    'devaneio', 'talarico', 'lascivia', 'conserto', 'modestia', 'apologia', 'analogia', 'insercao', 'ativista',
    'inospito', 'monotono', 'respaldo', 'remissao', 'sinonimo', 'mediocre', 'concerne', 'rapariga', 'despeito',
    'gratidao', 'alicerce', 'retorica', 'destarte', 'rechacar', 'fomentar', 'proceder', 'demagogo', 'primazia',
    'metodico', 'consiste', 'distinto', 'abnegado', 'criterio', 'desfecho', 'sucumbir', 'historia', 'elegivel',
]

geral_dificeis = [
    'paralelepipedo', 'empoderamento', 'delineamento', 'caleidoscopio', 'polinesio', 'polifonico',
]

categoria_geral = [geral_faceis, geral_medianas, geral_faceis]


tech_faceis = ['byte', 'bit', 'git', 'put', 'add']

tech_medianas = ['append', 'enumerate', 'while', 'atribuicao', 'repeticao', 'condicional', 'flutuante']

tech_dificeis = ['engenharia_de_dados', 'data_ wharehouse', 'business intelligence', 'data mining', 'data science', 'artificial intelligence',
'machine learning','deep learning']

categoria_tech = [tech_faceis, tech_medianas, tech_dificeis]

tech_dicionario = {
'engenharia de dados':' DICA: É a disciplina focada nos apectos como a identificação das fontes de dados, coletânea e,'
'\nno armazenamento dos dados.',
'data wharehouse' :' DICA: É um repositório central de informações que pode ser usado para analisar e tomar decisões mais informadas.',
'business intelligence' :'DICA: É a disciplina de analisar e transformar dados para extrair valiosos insights de negócios para permitir'
'\na tomada de decisões. Hoje, o BI é normalmente usado para se referir a análises descritivas e relatórios.',
'data mining' : 'DICA: É um processo de extração e descoberta de padrões em grandes conjuntos de dados envolvendo métodos na interseção'
'\nde aprendizado de máquina, estatísticas e sistemas de banco de dados.',
'data science' : 'DICA: É a disciplina de aplicação de técnicas analíticas avançadas para extrair informações valiosas de dados para a'
'\ntomada de decisões de negócios e planejamento estratégico.',
'artificial intelligence' : 'DICA: Refere-se à capacidade de uma máquina de imitar as capacidades da mente humana, como aprender com'
'\nexemplos e experiências, reconhecer objetos, compreender e responder à linguagem, tomar decisões e resolver problemas.',
'machine learning': 'DICA: É um subconjunto da disciplina de inteligência artificial (IA) que fornece aos sistemas a capacidade'
'\nde aprender e melhorar automaticamente com a experiência, sem ser explicitamente programado.',
'deep learning' : 'DICA: É uma técnica que se enquadra na disciplina de aprendizado de máquina. É baseado em redes neurais artificiais'
'\ninspiradas na estrutura do cérebro humano.',
}



