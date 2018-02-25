import random
import re
import os

SPACE = re.compile(r'\s+')
THIS = os.path.dirname(os.path.realpath(__file__))


class Hashtags:
    def __init__(self, filepath, name=None):
        if not filepath.endswith('.txt'):
            filepath = f'{filepath}.txt'
        self._name = name or os.path.basename(filepath).strip('.txt')
        self._hts = []
        with open(filepath) as fin:
            for line in fin:
                line = line.strip().lower()
                if line:
                    line = SPACE.sub('', line)
                if not line.startswith('#'):
                    line = f'#{line}'
                self._hts.append(line)

    @property
    def hashtags(self):
        return self._hts

    @property
    def random(self):
        return random.choice(self._hts)

    @property
    def name(self):
        return self._name

    def __len__(self):
        return len(self._hts)

    def __str__(self):
        return str(self._hts)

    def __iter__(self):
        for item in self._hts:
            yield item

    def __getitem__(self, item):
        return self._hts[item]
