class ContaBancaria:
    """Representa uma conta bancária básica com titular, saldo e status de ativação."""
    def __init__(self, titular, saldo):
        """Inicializa uma nova conta bancária.
        Args:
            titular (str): Nome do titular da conta.
            saldo (float): Saldo inicial da conta.
        """
        self.titular = titular
        self.saldo = saldo
        self._ativo = False  # Atributo privado para indicar se a conta está ativa
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"
     @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True


conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


class ContaBancariaPythonica:
    """Representa uma conta bancária com encapsulamento de atributos através de propriedades."""
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


class ClienteBanco:
    """Representa um cliente de um banco com seus dados pessoais."""
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        """Cria uma nova conta bancária associada a um cliente.
        Args:
            titular (str): Nome do titular da conta (que é o cliente).
            saldo_inicial (float): Saldo inicial da conta.
        Returns:
            ContaBancariaPythonica: A nova conta bancária criada.
        """
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
