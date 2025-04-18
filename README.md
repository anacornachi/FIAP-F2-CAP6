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

Outro problema importante é a ausência de previsões baseadas em dados, o que torna o planejamento da próxima safra uma tarefa sujeita a suposições, e não a análises históricas confiáveis.

Segundo a Embrapa, 61% dos produtores rurais apontam a falta de infraestrutura de conectividade como o principal obstáculo para a adoção de tecnologias digitais no campo. Soma-se a isso o fato de que muitos ainda utilizam métodos tradicionais e empíricos, transmitidos de geração em geração, o que limita a eficiência e a precisão na gestão agrícola.

### Objetivo da Solução

Desenvolver um sistema simples em Python, acessível via terminal, que permita ao pequeno produtor rural registrar suas culturas e insumos utilizados, armazenar os dados em banco Oracle e, a partir desses dados, gerar relatórios e realizar **previsões de demanda futura por insumos agrícolas** usando **regressão linear**.

A proposta é facilitar a gestão da produção e fornecer uma base para tomada de decisões mais eficientes, promovendo autonomia e organização no campo.

### Justificativa

Essa solução parte de uma dor concreta do agronegócio brasileiro e foca em um público estratégico: os pequenos produtores, responsáveis por uma parcela significativa da produção agrícola nacional. Ao mesmo tempo, atende aos conteúdos exigidos pela disciplina, utilizando subalgoritmos com passagem de parâmetros, estruturas de dados como listas e dicionários, manipulação de arquivos JSON e conexão com banco de dados (Oracle).
O uso de regressão linear como base estatística para previsão agrega inovação e valor à proposta, mesmo em um ambiente simplificado, de forma a aplicar os conhecimentos adquiridos durante as aulas.

### Funcionalidades da solução

1. **Cadastro de cultura**: O usuário poderá registrar informações como nome da cultura, datas de plantio e colheita, área plantada e produtividade.
2. **Registro de insumo**: Será possível registrar fertilizantes, sementes ou defensivos, informando tipo, unidade, valor por unidade e vinculando-os opcionalmente a uma cultura com data e frequência de aplicação.
3. **Relatórios por cultura ou safra**: O sistema irá gerar relatórios limpos e organizados com as informações cadastradas.
4. **Importação de dados via JSON**: Os dados podem ser importados de arquivos JSON, facilitando testes em lote e simulações realistas de uso.
5. **Previsão de demanda por insumo**: Com base no histórico de uso, o sistema aplicará regressão linear para prever a quantidade necessária para o próximo ciclo agrícola.
6. **Validação de entrada**: O sistema incluirá verificações para garantir que os dados inseridos estejam corretos (por exemplo, impedir letras em campos numéricos).
7. **Persistência de dados**: Os dados são armazenados no banco Oracle simulando um cenário real de gestão de dados.

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

Este projeto foi desenvolvido em Python e executa via terminal, com foco em acessibilidade para pequenos produtores e integração com banco de dados Oracle. Abaixo, você encontrará todas as instruções necessárias para configurar o ambiente e rodar o projeto em sua máquina.

---

### ✅ Pré-requisitos

- [Python 3.9+](https://www.python.org/downloads/)
- Git
- Oracle Instant Client instalado e configurado (ou conexão com banco Oracle da FIAP)
- Acesso ao terminal ou prompt de comando
- IDE recomendada: VSCode ou PyCharm

---

### 🧪 Fase 1: Clonar o projeto

```bash
git clone https://github.com/anacornachi/FIAP-F2-CAP6.git
cd FIAP-F2-CAP6
```

---

### 🐍 Fase 2: Criar e ativar ambiente virtual (venv)

#### Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 📦 Fase 3: Instalar as dependências

Certifique-se de que o arquivo `requirements.txt` está na raiz do projeto:

```bash
pip install -r requirements.txt
```

---

### 🔐 Fase 4: Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis preenchidas:

```
ORACLE_USER=seu_usuario
ORACLE_PASSWORD=sua_senha
ORACLE_HOST=oracle.fiap.com.br
ORACLE_PORT=1521
ORACLE_SERVICE=ORCL
```

> **Dica:** O `.env` será lido automaticamente pelo projeto para realizar a conexão com o banco Oracle.  
> O carregamento é feito via `python-dotenv`, já incluída no `requirements.txt`.

---

### 🛠️ Fase 5: Criar as tabelas no banco Oracle

Execute o script abaixo para criar todas as tabelas necessárias:

```bash
python src/db/setup_db.py
```

As tabelas criadas serão:
- `crops`
- `inputs`
- `crop_input_applications`

---

### ▶️ Fase 6: Executar o sistema

Com o ambiente configurado, execute o sistema principal via terminal:

```bash
python src/main.py
```

Você verá um menu interativo com todas as opções disponíveis, como:
- Cadastro de culturas
- Registro e aplicação de insumos
- Importação via JSON
- Relatórios
- Análises preditivas
- Atualização da data de colheita

---

### 📥 Importação rápida com arquivos de exemplo

O projeto já possui arquivos JSON prontos para popular o banco com dados válidos e começar a testar:

- Culturas: `src/data/culturas.json`
- Insumos: `src/data/insumos.json`

No terminal, escolha a opção de importação e digite o caminho. Exemplo:

```
Informe o caminho do arquivo: src/data/culturas.json
```

---

### 🧪 Fase 7 (opcional): Executar os testes automatizados

```bash
python -m unittest discover src/tests
```
---

### Possíveis erros e soluções

- **Erro: arquivo `.env` não encontrado** → verifique se ele existe e está corretamente preenchido.
- **Erro de conexão Oracle** → revise seus dados de host, porta e serviço.
- **Tests não executam** → confira se está rodando o comando dentro do ambiente virtual ativo e se há testes válidos com `test_` no nome do arquivo.


## 🗃 Histórico de lançamentos

* 0.1.0 - 12/04/2025
    * Documentação (README) criada seguindo o modelo PBL.
    * Adicionado o menu principal de navegação para o usuário.
    * Criado o primeiro fluxo: registro de culturas com validação de dados utilizando Cerberus e tratamento de erros com mensagens amigáveis.
* 0.2.0 - 13/04/2025 
    * Integração com banco de dados OracleDB para persistência de culturas. 
    * Refatoração dos fluxos de cadastro e importação de culturas para salvamento direto no banco. 
    * Inclusão do método get_all_crops para leitura de registros persistidos. 
    * Implementação do validador customizado com suporte à regra regex_if_not_empty. 
    * Criação de testes unitários e de integração com dados reais e arquivos JSON simulando o uso em produção. 
    * Setup automatizado para truncar registros de teste antes e depois de cada execução.
* 0.3.0 - 17/04/2025 
    * Criação do fluxo de cadastro de insumos com unidade de medida e preço por unidade. 
    * Salvamento dos insumos no banco Oracle e visualização no terminal.
    * Implementação da aplicação de insumos em culturas com suporte à frequência e intervalo de aplicação.
    * Relacionamento N:N entre culturas e insumos por meio da tabela crop_input_applications.
    * Detecção automática da unidade do insumo ao aplicar em uma cultura, evitando repetição desnecessária.
    * Atualização do sistema de prompts com mensagens contextualizadas em português.
    * Criação do fluxo de importação de insumos via arquivo JSON.
    * Testes automatizados completos para:
      * Cadastro manual de insumo
      * Importação de insumos via JSON
      * Aplicação de insumo em cultura
      * Casos de erro e borda com mensagens específicas
    * Correção de mensagens de erro e validações para melhorar a experiência do usuário final.
* 0.4.0 - 18/04/2025
    * Criação do fluxo de atualização da data de colheita de culturas, com listagem de registros e validação de entrada.
    * Isolamento da lógica de acesso ao banco em repositórios (get_all_crops, update_crop_harvest_date) para maior organização e reutilização.
    * Revisão da função de previsão de demanda com aplicação de regressão linear múltipla utilizando scikit-learn.
    * Inclusão de novos indicadores no relatório preditivo:
      * Previsão de quantidade por insumo
      * Custo estimado com base no preço unitário
      * Índice de Eficiência do Insumo (IEI)
      * Classificação de eficiência (alta, média, baixa)
      * Uso médio por hectare
    * Melhorias na apresentação textual dos relatórios no terminal, com legendas e explicações finais.
    * Padronização da experiência do usuário com uso de ícones, linguagem acessível e validação de respostas em português.
    * Revisão da documentação principal (README.md) com ajustes na descrição PBL, mantendo o limite de 600 palavras.
    * Organização e limpeza do projeto: remoção de métodos duplicados e refatoração de chamadas diretas ao banco.
  
## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


