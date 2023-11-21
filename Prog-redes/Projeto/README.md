# Aplicação Cliente/Servidor - Programação para Redes (IFRN)

Este projeto implementa uma aplicação cliente/servidor

## Funções do Programa

### Cliente (Agente)

1. **Conexão:**
   - A conexão entre o cliente e o servidor é estabelecida através de sockets TCP 

2. **Registro Online:**
   - Ao ser executado, o cliente informa ao servidor que está online, fornecendo o nome do HOST, seu IP e o usuário logado.

3. **Execução em Segundo Plano:**
   - O cliente é executado em segundo plano, liberando o terminal para o usuário.

4. **Verificação de Servidor Online:**
   - Se o servidor estiver offline, o cliente fica em segundo plano, testando a um tempo pré-determinado se o servidor voltou a ficar online.

5. **Controle de Instâncias:**
   - O cliente não permite que uma segunda instância seja carregada na memória.

6. **Remoção da Memória Manualmente:**
   - O cliente possui uma opção para se remover da memória manualmente.

7. **Resposta a Requisições do Servidor:**
   - O cliente responde a requisições oriundas do servidor enquanto está na memória.

### Servidor

1. **Conexão:**
   - O servidor permite conexões simultâneas de vários clientes (agentes) usando um socket TCP.

2. **Gerenciamento de Conexões:**
   - O servidor gerencia as conexões ativas e detecta quando um cliente fica offline.

3. **Execução em Segundo Plano:**
   - O servidor é executado em segundo plano, liberando o terminal para o usuário.

4. **Controle de Instâncias:**
   - O servidor não permite que uma segunda instância seja carregada na memória.

5. **Remoção da Memória Manualmente:**
   - O servidor possui uma opção para se remover da memória manualmente.

6. **Comandos do BOT no Telegram:**
   - Implementação de comandos via bot no Telegram para:
     - Informações do hardware onde o servidor está sendo executado.
       ```
       ====================== /info-h =======================
       ```
     - Lista de programas instalados no servidor.
       ```
       ====================== /info-p =======================
       ```
     - Histórico de navegação em diferentes navegadores.
       ```
       ====================== /historic ======================
       ```
     - Informações detalhadas do usuário logado.
       ```
       ====================== /info-u =======================
       ```
     - Lista dos agentes online com informações básicas.
       ```
       ====================== /listclient =====================
       ```

## Tipos de Sockets 

- **Tipo de Socket:**
  - Utiliza socket TCP no servidor para garantir controle de transmissão.

---

*Victor Diniz*
