# Complete o programa abaixo para que funcione a implementação de lista dinâmica.

# Foram adicionadas saídas esperadas que devem ser cumpridas como testes.

class DynamicIntArray:

    def __init__(self, capacity=2):

        if capacity <= 0:

            raise ValueError("Capacidade inicial deve ser maior que 0.")

        self.capacity = capacity        # Tamanho real do array interno

        self.size = 0                   # Quantos elementos o usuário colocou

        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)


    def append(self, value):

        if self.size == self.capacity:

            self._resize_up(2 * self.capacity)

        self.data[self.size] = value

        self.size += 1


    def _resize_up(self, new_capacity):

        print(f"⏫ Redimensionando de {self.capacity} para {new_capacity}")

        new_data = [0] * new_capacity

        for i in range(self.size):

            new_data[i] = self.data[i]

        self.data = new_data

        self.capacity = new_capacity

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora dos limites")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora dos limites")
        self.data[index] = value

    def contains(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora dos limites")
        
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
        
        if self.size > 0 and self.size <= self.capacity // 4:
            new_capacity = max(2, self.capacity // 2)
            self._resize_up(new_capacity)


lista = DynamicIntArray()

lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)