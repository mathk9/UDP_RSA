import random
import math

class RSA:
    def main(self):
        bitlen = 4096

        r = random.SystemRandom()
        p = self.generate_prime(bitlen // 2, r)
        q = self.generate_prime(bitlen // 2, r)

        n = p * q

        m = (p - 1) * (q - 1)

        e = 3

        while math.gcd(m, e) > 1:
            e += 2

        d = self.mod_inverse(e, m)

        # print("p:", p)
        # print("q:", q)

        return n, e, d


    def encrypt(self, msg, e, n):
        msg_cifrada = pow(int.from_bytes(msg.encode(), byteorder='big'), e, n)
        print("msg cifrada:", msg_cifrada)
        return msg_cifrada
    
    def decrypt(self, msg, d, n):
        # msg_decifrada = int.to_bytes(pow(msg, d, n), length=(msg.bit_length() + 7) // 8, byteorder='big').decode()
        
        intermediate_result = pow(msg, d, n)

        # Determine o número de partes em que você deseja dividir o valor
        num_parts = 1

        # Calcule o tamanho de cada parte
        part_size = (intermediate_result.bit_length() + 7) // 8 // num_parts

        # Inicialize uma lista para armazenar as partes
        parts = []

        # Divida o valor em num_parts partes
        for i in range(num_parts):
            shift = (num_parts - i - 1) * part_size * 8
            mask = ((1 << (part_size * 8)) - 1) << shift
            part_value = (intermediate_result & mask) >> shift
            part_bytes = part_value.to_bytes(part_size, byteorder='big')
            parts.append(part_bytes)

        # Agora você tem as partes convertidas em bytes em uma lista 'parts'
        # Você pode concatená-las se desejar
        byte_result = b''.join(parts)

        print(parts)

        # Decodifique a sequência de bytes em uma string
        msg_decifrada = byte_result.decode()


        print("msg decifrada:", msg_decifrada)
        return msg_decifrada

    def generate_prime(self, bitlen, r):
        while True:
            potential_prime = r.getrandbits(bitlen)
            potential_prime |= (1 << (bitlen - 1)) | 1 
            if self.is_prime(potential_prime):
                return potential_prime

    def is_prime(self, n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        # n as d*2^r + 1
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False

        return True

    def mod_inverse(self, e, m):
        g, x, y = self.extended_gcd(e, m)
        if g != 1:
            raise Exception('Modular não existe')
        else:
            return x % m

    def extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.extended_gcd(b % a, a)
            return (g, y - (b // a) * x, x)

