# UDP_RSA
Este repositório contem os scripts Client e Server utilizados para realizar um teste de interceptação de mensagens criptografadas com a criptografia RSA.

# Criptografia RSA

A criptografia RSA é um dos algoritmos de criptografia de chave pública mais amplamente utilizados. Ela foi inventada por Ron Rivest, Adi Shamir e Leonard Adleman em 1977 e é amplamente empregada para garantir a confidencialidade e a autenticidade de comunicações digitais.

## Como Funciona

1. Chave Pública e Chave Privada:
   - Cada pessoa ou entidade possui duas chaves: uma pública e uma privada.
   - A chave pública é usada para criptografar mensagens.
   - A chave privada é usada para descriptografar mensagens.

2. Criptografia:
   - O remetente usa a chave pública do destinatário para criptografar a mensagem.
   - A mensagem criptografada é enviada ao destinatário.

3. Descriptografia:
   - O destinatário usa sua chave privada para descriptografar a mensagem e ler o conteúdo original.

## Segurança e Utilização

- A segurança do RSA baseia-se na dificuldade de fatorar grandes números primos.
- É amplamente utilizado em comunicações seguras na Internet, como HTTPS.
- Também é usado para assinaturas digitais, autenticação e segurança de dados.

Para o teste realizado pelo grupo foi utilizada uma chave de 4096 bits.
### Funcionamento dos scripts
Optamos por utilizar de exemplo uma classe em python adaptada de outra classe em Java disponbilizada pelo professor Fabio Henrique Cabrini em seu material, já contendo métodos para criptografar e decriptografar mensagens enviadas entre Cliente e Servidor. Adaptamos o script para adequar se aos métodos python.

Importamos a classe nos scripts Simple_udpClient.py e Simple_udpServer.py e realizamos as chamadas para que os scripts pudessem criptografar a mensagem enviada pelo Client e decriptografá-la para exibição ao Server, assim ao ser interceptada pelo programa WireShark ela seria de forma criptografada, dificultando a leitura de seu conteudo.

## Video de demonstração do teste
[Youtube |Demonstração criptografia RSA em web socket com captura no Wireshark](https://youtu.be/krKSIm_YvRA)

## Grupo
Caio Vinicius Magro - 081200042

Giovana Moreira da Silva - 081200043

Matheus de Novais Souza - 081190048

Ysabela Akiyama Molero Rodrigues - 081200044
