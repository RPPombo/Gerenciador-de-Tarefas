# 📌 Projeto Gerenciador de Tarefas
## 📖 Introdução

Este projeto foi desenvolvido como um desafio pessoal, com o objetivo de aprendizado e prática dos conceitos básicos da linguagem de programação Python.

## 🎯 Objetivo

O Gerenciador de Tarefas tem como objetivo auxiliar na organização do dia a dia, permitindo que o usuário acompanhe suas atividades e visualize quais tarefas já foram concluídas, aumentando assim sua eficiência e produtividade.

## 🏗 Arquitetura do Projeto

A estrutura de diretórios do projeto está organizada da seguinte forma:  

```bash
Gerenciador-de-Tarefas/  
│
├── Serviços/  
│   ├── auxiliares.py  
│   └── gerenciador_dataframes.py  
│
├── Tela/  
│   ├── Frames/  
│   │   ├── frame_esquerda.py  
│   │   └── frame_direita.py  
│   └── interface.py  
│
├── app.py  
├── .gitignore  
└── README.md  
```

## ⚙️ Funcionamento
O projeto utiliza as seguintes bibliotecas do Python:  
- tkinter → Interface gráfica  
- pandas → Manipulação de tabelas e armazenamento das tarefas em arquivos CSV  
- time → Obtenção do horário local  

## ▶️ Como executar
1. Certifique-se de ter o Python 3.8+ instalado.  
2. Instale as dependências necessárias (se houver).  
3. Execute o arquivo principal:  

```bash
python app.py
```

## 🖥 Uso
* O programa possui uma interface gráfica simples e intuitiva, desenvolvida em tkinter.
* Todas as ações podem ser realizadas diretamente pelos botões na interface, sem necessidade de utilizar o terminal.
* As tarefas são armazenadas em arquivos CSV, garantindo que as informações sejam salvas e possam ser carregadas em futuras execuções.
* Para fins de acompanhamento, algumas mensagens informativas sobre as ações internas são exibidas no terminal.
* Para facilitar a utilização do programa, ele foi compilado em um arquivo *.exe* (dentro da pasta dist), utilizando a biblioteca pyinstaller