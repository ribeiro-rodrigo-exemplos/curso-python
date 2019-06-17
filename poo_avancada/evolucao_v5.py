#!/usr/bin/python3


class Humano:
    # atributo de classe
    especie = 'Humo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')

        self._idade = idade

    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade não implementada')

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Autralopiteco', ) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('John Doe')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('propriedade abstrata')

    jose = HomoSapiens('José')
    grogn = Neanderthal('Grogn')

    print('{} da classe {}, inteligente: {}'.format(
        jose.nome, jose.__class__.__name__, jose.inteligente))

    print('{} da classe {}, inteligente: {}'.format(
        grogn.nome, grogn.__class__.__name__, grogn.inteligente))
