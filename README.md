![Banner](assets/banner.png)
# 🖱️ Mouse Wifi — MIT App Inventor

![MIT App Inventor](https://img.shields.io/badge/Engine-MIT%20App%20Inventor-blue)
![Python](https://img.shields.io/badge/Server-Python%20Flask-yellow)
![Plataforma](https://img.shields.io/badge/Plataforma-Android%20%7C%20Windows-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Projeto que transforma um celular Android em um touchpad remoto para controlar o computador via rede Wi-Fi local.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Telas do App](#-telas-do-app)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
- [Como Descobrir o IP](#-como-descobrir-o-ip)
- [Configuração no MIT App Inventor](#-configuração-no-mit-app-inventor)
- [Como Usar em Outro Computador](#-como-usar-em-outro-computador)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Observações](#-observações)
- [Importar o Projeto](#-importar-o-projeto)
- [O que Aprendi](#-o-que-aprendi)
- [Autor](#️-autor)

---

## 📱 Sobre o Projeto

Mouse Wifi transforma um celular Android em um touchpad remoto para controlar o computador via rede Wi-Fi local. O celular se comunica com um servidor Python rodando no PC, enviando comandos de movimentação e clique em tempo real.

**Ferramenta:** MIT App Inventor  
**Servidor:** Python com Flask e PyAutoGUI  
**Conexão:** Wi-Fi local  
**Plataforma:** Android + Windows  

---

## ✅ Funcionalidades

- Movimentação do cursor pelo touchpad da tela
- Clique esquerdo
- Clique direito
- Controle via rede Wi-Fi local

---

## 📸 Telas do App

### Interface do Touchpad
![Design do App](assets/tela_mouse.png)

### Blocos MIT App Inventor
![Blocos MIT App Inventor](assets/blocks_mit.png)

---

## ⚙️ Requisitos

### No computador

- Python 3 instalado
- Flask
- PyAutoGUI
- VS Code (opcional)

### No celular

- Aplicativo criado no MIT App Inventor instalado via APK ou MIT AI2 Companion

---

## 🚀 Instalação

### 1. Instalar dependências

Abra o terminal e execute:

```
pip install flask pyautogui
```

### 2. Executar o servidor

Na pasta onde está o arquivo `mouse.py` execute:

```
python mouse.py
```

Se tudo estiver correto aparecerá no terminal:

```
Running on http://0.0.0.0:5000
```

---

## 🔍 Como Descobrir o IP

Abra o Prompt de Comando e execute:

```
ipconfig
```

Procure pela linha **Endereço IPv4**. O resultado será algo como:

```
000.000.0.000
```

Esse endereço deverá ser usado no aplicativo MIT App Inventor para conectar ao servidor.

---

## 📲 Configuração no MIT App Inventor

O componente **Web** do MIT App Inventor deve utilizar URLs no seguinte formato:

**Movimentação do cursor:**
```
http://IP_DO_PC:5000/move?x=VALORX&y=VALORY
```

**Clique esquerdo:**
```
http://IP_DO_PC:5000/click
```

**Clique direito:**
```
http://IP_DO_PC:5000/rightclick
```

Substitua `IP_DO_PC` pelo endereço IPv4 encontrado com o comando `ipconfig`.

**Exemplo:**
```
http://000.000.0.000:5000/click
```

---

## 💻 Como Usar em Outro Computador

1. Baixe o arquivo `mouse.py` deste repositório
2. Abra o terminal na pasta do projeto
3. Execute o servidor:
```
python mouse.py
```
4. Descubra o IP do computador com `ipconfig` no Prompt de Comando
5. Atualize o IP no aplicativo MIT App Inventor
6. Conecte o celular e o computador na mesma rede Wi-Fi
7. Utilize normalmente

---

## 📂 Estrutura do Projeto

```
MouseWifiMIT/
│
├── mouse.py
└── README.md
```

---

## ⚠️ Observações

- Computador e celular devem estar conectados na mesma rede Wi-Fi
- Alguns firewalls podem bloquear a porta 5000 — desative temporariamente se necessário
- Caso o IP mude, atualize o endereço no aplicativo
- O servidor deve permanecer aberto enquanto o aplicativo estiver sendo utilizado

---

## 📦 Importar o Projeto

Baixe o arquivo `MouseWifiMIT.aia` na seção [Releases](../../releases) e importe diretamente no MIT App Inventor:

```
Projects → Import project (.aia)
```

---

## 📚 O que Aprendi

- Comunicação entre Android e Python via requisições HTTP
- Criação de servidor local com Flask
- Uso do componente Web do MIT App Inventor para enviar requisições
- Controle de mouse via código com PyAutoGUI
- Conceito de rede local e endereço IP
- Integração entre programação em blocos e linguagem de texto

---

## ✏️ Autor

Desenvolvido por **Kayozkx**

> Desenvolvido em 04 de junho de 2026.
