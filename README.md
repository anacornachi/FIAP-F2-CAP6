# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Cap 6 - Python e além - Gestão do agronegócio em python

## Nome do grupo
Grupo 42

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/anacornachi/">Ana Cornachi</a>
- <a href="https://www.linkedin.com/in/carlamaximo/">Carla Máximo</a>
- <a href="https://www.linkedin.com/in/lucas-lins-lima/">Lucas Lins</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi Chiovato</a>


## 📜 Descrição

Pequenos produtores rurais enfrentam desafios significativos na gestão da produção agrícola, especialmente no controle do uso de insumos e no planejamento de safras futuras. A falta de ferramentas digitais acessíveis leva muitos a dependerem de registros em papel, dificultando o acompanhamento da produtividade, causando desperdícios, comprometendo o controle financeiro e limitando o acesso a crédito rural.

Outro problema importante é a ausência de previsões baseadas em dados, o que torna o planejamento da próxima safra uma tarefa baseada em suposições, não em análises históricas.

Segundo a Embrapa, 61% dos produtores rurais apontam a falta de infraestrutura de conectividade como o principal obstáculo para a adoção de tecnologias digitais no campo. Soma-se a isso o fato de que muitos ainda utilizam métodos tradicionais e empíricos, transmitidos de geração em geração, o que limita a eficiência e a precisão na gestão agrícola.

### Objetivo da Solução

Desenvolver um sistema simples em Python, acessível via terminal, que permita ao pequeno produtor rural registrar suas culturas e insumos utilizados, armazenar os dados localmente em JSON (ou banco Oracle, em uma versão alternativa) e, a partir desses dados, gerar relatórios e realizar **previsões de demanda futura por insumos agrícolas** usando **regressão linear**.

A proposta é facilitar a gestão da produção e fornecer uma base para tomada de decisões mais eficientes, promovendo autonomia e organização no campo.

### Justificativa

Essa solução parte de uma dor concreta do agronegócio brasileiro e foca em um público estratégico: os pequenos produtores, responsáveis por uma parcela significativa da produção agrícola nacional. Ao mesmo tempo, atende aos conteúdos exigidos pela disciplina, utilizando subalgoritmos com passagem de parâmetros, estruturas de dados como listas e dicionários, manipulação de arquivos JSON e conexão com banco de dados (Oracle).
O uso de regressão linear como base estatística para previsão agrega inovação e valor à proposta, mesmo em um ambiente simplificado, de forma a aplicar os conhecimentos adquiridos durante as aulas.

### Funcionalidades da solução

1. **Cadastro de cultura**: O usuário poderá registrar informações como nome da cultura, datas de plantio e colheita, área plantada e produtividade.
2. **Registro de insumo**: Será possível registrar fertilizantes e outros insumos utilizados, associando-os a uma cultura e a uma data de aplicação.
3. **Relatórios por cultura ou safra**: O sistema irá gerar relatórios limpos e organizados com as informações cadastradas.
4. **Previsão de demanda por insumo**: Com base no histórico de uso, o sistema aplicará regressão linear para prever a quantidade necessária para o próximo ciclo agrícola.
5. **Validação de entrada**: O sistema incluirá verificações para garantir que os dados inseridos estejam corretos (por exemplo, impedir letras em campos numéricos).
6. **Persistência de dados**: Os dados serão armazenados localmente em arquivos JSON. Em uma versão expandida, haverá integração com banco Oracle simulando um cenário real de gestão de dados.

### Aplicação de conteúdos do curso

- **Subalgoritmos**: Separação de lógicas em funções para modularidade do sistema.
- **Estruturas de dados**: Uso de listas, dicionários e tuplas para organizar os registros.
- **Manipulação de arquivos**: Gravação e leitura de dados em formato JSON.
- **Banco de dados Oracle**: Simulação de integração para cadastro e consulta.
- **Análise estatística (regressão linear)**: Aplicação prática de modelo de previsão com base em dados históricos.

### Conclusão

A solução proposta visa empoderar pequenos produtores com uma ferramenta simples, funcional e baseada em dados. Além de atender aos objetivos da disciplina, ela propõe uma transformação realista e aplicável no cotidiano agrícola, utilizando Python como meio de inovação acessível no campo.

O projeto olha para além da formação acadêmica e entrega uma proposta aplicável a realidade brasileira, aliando conhecimento técnico a responsabilidade social.

---

## Referências

1. EMBRAPA. Agricultura – Semear Digital. Disponível em: https://www.semear-digital.cnptia.embrapa.br/noticia/category/agricultura/. Acesso em: 12 ab. 2025

2. EMBRAPA. Pesquisa mostra o retrato da agricultura digital brasileira. Embrapa, 16 out. 2019. Disponível em: https://www.embrapa.br/busca-de-noticias/-/noticia/54770717/pesquisa-mostra-o-retrato-da-agricultura-digital-brasileira. Acesso em: 12 abr. 2025.

3. SEBRAE. Pesquisa Agricultura Digital no Brasil. Disponível em: https://sebrae.com.br/sites/PortalSebrae/artigos/pesquisa-agricultura-digital-no-brasil%2Cd7cd720d1eed3710VgnVCM1000004c00210aRCRD. Acesso em: 12 abr. 2025.

4. FARMONAUT. Agronegócio Brasileiro em 2025: Crescimento, Inovação e Desafios para Produtores Rurais. Disponível em: https://farmonaut.com/south-america/agronegocio-brasileiro-em-2025-crescimento-inovacao-e-desafios-para-produtores-rurais/. Acesso em: 12 abr. 2025.

5. ABIMAQ. Conectividade Rural, Mecanização na Agricultura Familiar e os Desafios para a Recuperação em 2025 da Indústria Agrícola. Disponível em: https://informaq.abimaq.org.br/conectividade-rural-mecanizacao-na-agricultura-familiar-e-os-desafios-para-a-recuperacao-em-2025-da-industria-agricola/. Acesso em: 12 abr. 2025.

6. GOVERNO FEDERAL. Ministro Carlos Fávaro apresenta prioridades do Mapa para 2025-2026 em comissão no Senado. Disponível em: https://www.gov.br/agricultura/pt-br/assuntos/noticias/ministro-carlos-favaro-apresenta-prioridades-do-mapa-para-2025-2026-em-comissao-no-senado. Acesso em: 12 abr. 2025.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


## 🗃 Histórico de lançamentos

* 0.1.0 - 12/04/2025
    * Documentação (README) criada seguindo o modelo PBL.
    * Adicionado o menu principal de navegação para o usuário.
    * Criado o primeiro fluxo: registro de culturas com validação de dados utilizando Cerberus e tratamento de erros com mensagens amigáveis.


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


