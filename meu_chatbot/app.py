import os
import platform
import time


# os.system("color")
def enable_color_on_windows():
  if platform.system() == "Windows":
    os.system("color")


# Dicionário de perguntas e respostas
perguntas_respostas = {
    '1': {
        'text': 'Site',
        'suboptions': {
            '1': {
                'text':
                'Marcas parceiras',
                'response':
                'Nossas marcas parceiras são cuidadosamente selecionadas para oferecer produtos de alta qualidade e confiabilidade para você {nome}, dentre muitos parceiros temos nomes como: Brosol, Mecar, Halley, DS e muitas outras marcas nacionais de ótima qualidade.'
            },
            '2': {
                'text':
                'Não consigo calcular o frete',
                'response':
                'Estamos de fato com algumas complicações com o calculo de frete {nome}, chame-nos em nosso Whatsapp: (11) 2786-3980 para que possamos calcular para você manualmente. Agradeçemos a compreensão.'
            },
            '3': {
                'text':
                'Quais as formas de pagamento?',
                'response':
                'Aceitamos várias formas de pagamento, incluindo cartões de crédito, sendo em até 4x sem juros ou de 5x a 12x com juros; transferência banc ária; PIX; boleto ou pagamento em dinheiro na nossa loja física.'
            },
            '4': {
                'text':
                'Não encontro o produto que quero',
                'response':
                '{nome}, se você não consegue encontrar o produto que deseja, por favor, verifique se digitou o nome corretamente na barra de pesquisa ou entre em contato conosco pelo nosso Whatsapp: (11) 2786-3980.'
            },
            '5': {
                'text':
                'O site aceita cupons de desconto?',
                'response':
                'Sim, aceitamos cupons de desconto. Ao finalizar a compra no carrinho, há um campo para inserir o código do cupom e aplicar o desconto. Fique ligado {nome}, pois apenas damos cupons em datas especiais e com validade!'
            },
            '6': {
                'text':
                'Posso rastrear meu pedido após a compra?',
                'response':
                'Sim {nome}, após a compra, você receberá informações de rastreamento pelo próprio site, na aba "Meus Pedidos" para que possa acompanhar o status do seu pedido.'
            },
            '7': {
                'text':
                'Quais são as opções de envio internacional?',
                'response':
                'Oferecemos opções de envio internacional para atender clientes em todo o mundo. As opções e taxas podem variar de acordo com o destino, para que possamos calcular os prazos e valores, chame-nos em nosso Whatsapp: (11) 2786-3980.'
            },
            '8': {
                'text':
                'Como posso garantir que minha compra é segura?',
                'response':
                'Mantemos rigorosos padrões de segurança, incluindo certificados SSL e métodos de pagamento confiáveis. Além disso {nome}, protegemos suas informações pessoais de acordo com nossa política de privacidade.'
            },
            '9': {
                'text':
                'Quanto tempo leva para meu pedido ser processado e enviado?',
                'response':
                'O tempo de processamento e envio varia de acordo com o produto e a região de entrega. Normalmente, processamos e enviamos os pedidos em 1 dia útil.'
            },
            '10': {
                'text':
                'O que devo fazer se meu pagamento não for processado corretamente?',
                'response':
                'Se o seu pagamento não for processado corretamente {nome}, verifique se os detalhes do pagamento estão corretos. Se o problema persistir, entre em contato com a agência de seu banco para verificar o que esta ocorrendo, de qualquer forma nos mantemos a disposição, basta nos chamar em nosso Whatsapp: (11) 2786-3980.'
            }
        }
    },
    '2': {
        'text': 'Quem somos?',
        'suboptions': {
            '1': {
                'text':
                'Localização',
                'response':
                'Estamos localizados na Rua Andarai, 95 - Vila Floresta, Santo André - SP, 09050-000. Seria um prazer te receber em nossa loja física {nome}.'
            },
            '2': {
                'text':
                'Nossa história',
                'response':
                'CARBURADOR BRASIL, empresa nacional que há mais de 20 anos comercializa carburadores e componentes automotivos de marcas consolidadas. Somos referência no e-commerce no seguimento de carburadores. Atendemos todos os níveis de consumidores: particulares, pessoas física e jurídica. Nossa logística abrange todo o território nacional além da América Latina, Europa e Estados Unidos. Para saber mais, visite: "https://www.carburadorbrasil.com.br/pagina/quem-somos.html".'
            },
            '3': {
                'text':
                'Horário de funcionamento',
                'response':
                'Nosso horário de funcionamento é de segunda a sexta-feira, das 8h às 17h.'
            },
            '4': {
                'text':
                'Vocês fazem restauração?',
                'response':
                'Sim {nome}! Oferecemos serviços de restauração de carburadores, é um processo que utiliza o seu próprio carburador, onde é feito o reparo completo do mesmo para deixá-lo no melhor estado possível e em perfeitas condições de trabalho. Para saber mais, visite: "https://www.carburadorbrasil.com.br/pagina/restauracao-de-carburadores.html".'
            },
            '5': {
                'text':
                'Qual é a política de garantia?',
                'response':
                'Todos os nossos produtos contém garantia de 06 meses para defeitos que surgem como resultado de uso normal do produto. Mais informações estão disponíveis em nossa página de política de trocas e devoluções: "https://www.carburadorbrasil.com.br/pagina/politica-de-trocas-e-devolucoes.html".'
            },
            '6': {
                'text':
                'Quais são os valores e princípios da empresa?',
                'response':
                'Nossos valores incluem qualidade no atendimento e compromisso com o cliente, assim estabelecendo uma conexão diferenciada com pessoas. Para saber mais visite: "https://www.carburadorbrasil.com.br/pagina/quem-somos.html".'
            },
            '7': {
                'text':
                'Quais são os critérios para seleção de produtos à venda?',
                'response':
                'Selecionamos produtos com base em qualidade, durabilidade e somente de empresas que confiamos para que possamos garantir a satisfação dos nossos clientes.'
            },
            '8': {
                'text':
                'Diferenciais que tornam a empresa única em relação à concorrência?',
                'response':
                'Visamos sempre o melhor atendimento, oferecendo o melhor produto, as melhores condições para compra e um pós-venda profissional e comprometido, fatores que nos colocam como referência no mercado.'
            },
            '9': {
                'text':
                'Como a empresa lida com feedbacks e sugestões dos clientes para melhorias?',
                'response':
                'Estamos em constante melhoria, tanto que valorizamos muito o feedback dos clientes e usamos suas sugestões para aprimorar nossos produtos e serviços. Caso queira dar um feedback aceitariamos de braços abertos {nome}, mande em nosso Whatsapp: (11) 2786-3980.'
            },
            '10': {
                'text':
                'A empresa participa de feiras, eventos ou exposições relacionados ao setor?',
                'response':
                'Sim, participamos regularmente de feiras e eventos para que possamos interagir com nossos clientes e parceiros. A principal feira que participamos é a Automec, a maior feira internacional de autopeças.'
            }
        }
    },
    '3': {
        'text': 'Dúvidas referente à carburação',
        'suboptions': {
            '1': {
                'text':
                'Como funciona um carburador?',
                'response':
                'Um carburador é um dispositivo mecânico que regula a quantidade de ar e combustível que entra no motor do seu veículo. A mistura é enviada para os cilindros do motor para a combustão.'
            },
            '2': {
                'text':
                'Como regulo a mistura de ar do meu carburador?',
                'response':
                'Regular um carburador requer conhecimento técnico, recomendamos que você procure um profissional qualificado {nome}, para obter um trabalho de qualidade. Caso queira regula-lo em casa, ajuste o parafuso para atingir a rotação ideal do motor, quando o carburador se manter suave e estável, ai então estará tudo correto. Isso contribuirá para um funcionamento eficiente do veículo.'
            },
            '3': {
                'text':
                'Para que serve o embuchamento',
                'response':
                'O embuchamento é um conjunto de peças que controla o fluxo de ar que entra no carburador, o que afeta diretamente a quantidade de combustível que é misturada com o ar para alimentar o motor. O movimento da borboleta, uma das partes do embuchamento, é controlado pelo pedal do acelerador dentro do veículo.'
            },
            '4': {
                'text':
                'Como saber o modelo do meu carburador?',
                'response':
                'Ao decorrer do anos muitos carburadores foram fabricados, muitos até foram importados. Por sorte nossa equipe tem a experiência necessária para saber o modelo do seu carburador {nome}, chame-nos em nosso Whatsapp: (11) 2786-3980 que iremos te ajudar.'
            },
            '5': {
                'text':
                'O que é o afogador do carburador e quando devo usá-lo?',
                'response':
                'O afogador é um dispositivo muito importante para pessoas que moram em lugares com um clima mais frio. Ele facilita a partida quando as condições de temperatura do motor estão abaixo do ideal, enriquecendo temporariamente a mistura ar-combustível.'
            },
            '6': {
                'text':
                'De quanto em quanto tempo deve ser feita a limpeza do carburador?',
                'response':
                '{nome}, a frequência recomendada para a limpeza do carburador é a cada 06 meses. Carburadoes que ficam mais de 1 ano sem receber uma revisão adequada, tendem a durar muito menos tempo do que um carburador revisado regularmente.'
            },
            '7': {
                'text':
                'Qual a diferença entre um carburador de 1 estágio e 2 estágios?',
                'response':
                'A principal diferença é que o carburador de 1 estágio tem um único conjunto de elementos de mistura e é usado em motores com potência moderada. Já o carburador de 2 estágios possui dois conjuntos de elementos: um para baixas demandas de potência e outro para maior potência.'
            },
            '8': {
                'text':
                'Diferença entre o gicleur de marcha lenta mecânico e o eletromagnético',
                'response':
                'O gicleur de marcha lenta, seja mecânico ou eletromagnético, refere-se à mesma função. Ambos controlam a quantidade de combustível liberada durante a marcha lenta do motor no carburador. A diferença principal está na forma de controle, onde o mecânico é ajustado manualmente por um parafuso, enquanto o eletromagnético é ajustado eletronicamente por uma unidade de controle baseada em sensores do motor.'
            },
            '9': {
                'text':
                'É possível converter um sistema de injeção para carburação em um veículo?',
                'response':
                'Sim, é possível {nome}, basta ter uma flange de adaptação. Atualmente, temos a flange que é aplicada nos veículos da GM. Caso você precise adaptar em outro veículo precisariamos verificar qual a flange correta para o seu caso.'
            },
            '10': {
                'text':
                'Como saber o tamanho certo dos gicleurs para melhorar o desempenho do veículo?',
                'response':
                '{nome}, a escolha do tamanho correto dos gicleurs é uma tarefa complexa e requer um entendimento profundo de engenharia automotiva. Em todos os casos recomendamos colocar a giclagem que saiu original de tabela e caso precise fazer alguns ajustes, ir alterando conforme você e o seu mecânico acharem necessário.'
            }
        }
    }
}


def start():
  enable_color_on_windows()
  print('\033[1;32m' +
        'Olá! Bem-vindo à central de atendimento da CARBURADOR BRASIL' +
        '\033[0m')
  nome = innome = input('Digite seu nome: ')
  print(f'\nComo posso te ajudar hoje, {nome}?\n')

  while True:
    print_menu()
    resposta = input('\033[1;32m' + 'Escolha uma opção: ' + '\033[0m')
    print()  # Linha vazia para separação
    if resposta in perguntas_respostas:
      processar_resposta(resposta, nome)
    else:
      print('Escolha inválida. Digite um número válido.')


def print_menu():
  print('[1] Site')
  print('[2] Quem somos?')
  print('[3] Dúvidas referente à carburação')
  print()  # Linha vazia para separação


def print_menu_suboptions(suboptions):
  for key, sub_option in suboptions.items():
    print(f'[{key}] {sub_option["text"]}')


def processar_resposta(resposta, nome):
  suboptions = perguntas_respostas[resposta]['suboptions']
  print_menu_suboptions(suboptions)
  print()  # Linha vazia para separação
  sub_resposta = input('\033[1;32m' + 'Escolha uma subopção: ' + '\033[0m')
  if sub_resposta in suboptions:
    response = suboptions[sub_resposta]['response']
    print(f'\n{response.replace("{nome}", nome)}\n')
    continuar = input('\033[1;32m' +
                      'Além disso, posso ajudar em algo mais? (sim/não):' +
                      '\033[0m')

    print()  # Linha vazia para separação
    if continuar.lower() == 'sim':
      print_menu()
      nova_resposta = input('\033[1;32m' + 'Escolha uma opção: ' + '\033[0m')
      if nova_resposta in perguntas_respostas:
        processar_resposta(nova_resposta, nome)
    else:
      print(f'\nOk {nome}, sempre que precisar estarei à disposição!')
      time.sleep(5)
      exit()  # Encerrar o código aqui

  else:
    print('Subopção inválida. Digite um número válido.')

  print_menu()  # Movi esta linha para fora do bloco else


if __name__ == '__main__':
  start()
