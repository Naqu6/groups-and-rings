from typing import List
import itertools


class Bijection:
    mapping: dict[int, int]

    def __init__(self, mapping: dict[int, int]):
        assert sorted(list(mapping.keys())) == list(range(1, 1 + len(mapping)))
        self.mapping = mapping

    def __call__(self, arg: int) -> int:
        assert arg in self.mapping
        return self.mapping[arg]

    def __mul__(self, other: 'Bijection'):
        assert type(other) == type(self)
        keys = sorted(list(self.mapping.keys()))
        assert sorted(list(other.mapping.keys())) == keys

        return Bijection({key: self(other(key)) for key in keys})

    def __str__(self):
        result = f'bijection of size {len(self.mapping)}\n'
        mapping = sorted(self.mapping.items(), key=lambda item: item[0])
        result += ' '.join([str(k) for (k, _) in mapping]) + '\n'
        result += ' '.join([str(v) for (_, v) in mapping]) + '\n'
        result += '----'
        return result

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.mapping == other.mapping

    @classmethod
    def sn(cls, n: int) -> List['Bijection']:
        domain = range(1, n+1)
        return [
            cls({input_: output for (input_, output) in zip(
                domain, permutation)})
            for permutation in itertools.permutations(domain)]
