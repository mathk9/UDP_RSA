# UDP_RSA
Este repositório contem os scripts Client e Server utilizados para realizar um teste de interceptação de mensagens criptografadas com a Criptografia de Substituição Polialfabética de Vigenère.

# Criptografia de Substituição Polialfabética de Vigenère

A criptografia de substituição polialfabética de Vigenère é uma técnica de criptografia clássica inventada por Blaise de Vigenère no século XVI. Ela é uma extensão da cifra de substituição simples e é um dos primeiros exemplos de criptografia polialfabética.

## Como Funciona

1. Escolha uma chave, geralmente uma palavra ou frase curta.
2. Repita ou estenda a chave para corresponder ao comprimento do texto original.
3. Desloque cada letra do texto original de acordo com a posição da letra correspondente na chave.
4. O resultado é o texto cifrado.

## Vantagens e Limitações

- A cifra de Vigenère é mais resistente à análise de frequência do que a cifra de substituição simples.
- A segurança depende do comprimento e da qualidade da chave.
- Não é considerada segura para uso moderno, pois pode ser quebrada com facilidade por métodos criptoanalíticos avançados.

Para o teste realizado pelo grupo foi utilizada uma chave de 4096 bits.
### Funcionamento dos scripts
Optamos por utilizar de exemplo uma classe em python adaptada de outra classe em Java disponbilizada pelo professor Fabio Henrique Cabrini em seu material, já contendo métodos para criptografar e decriptografar mensagens enviadas entre Cliente e Servidor. Adaptamos o script para adequar se aos métodos python.

Importamos a classe nos scripts Simple_udpClient.py e Simple_udpServer.py e realizamos as chamadas para que os scripts pudessem criptografar a mensagem enviada pelo Client e decriptografá-la para exibição ao Server, assim ao ser interceptada pelo programa WireShark ela seria de forma criptografada, dificultando a leitura de seu conteudo.

## Video de demonstração do teste
[Youtube |Demonstração criptografia RSA em web socket com captura no Wireshark](https://youtu.be/krKSIm_YvRA)
## Grupo
Caio Vinicius Magro - 081200042

Giovana Moreira da Silva - 081200043

Matheus Novais de Souza - 081190048

Ysabela Akiyama Molero Rodrigues - 081200044
