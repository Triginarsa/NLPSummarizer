from static import static


class Stemmer(object):
    def __init__(self):
        self.vowels = 'aeiou'
        self.cvc_ignore = 'wxy'

    def huruf_konsonan(self, letter: str) -> bool:
        # menentukan huruf konsonan
        if letter not in self.vowels:
            return True
        return False

    def huruf_vokal(self, letter: str) -> bool:
        # menentukan huruf vokal
        return not self.huruf_konsonan(letter=letter)

    def konsonan_perindex_kata(self, word: str, index: int) -> bool:
        # menentukan index kata adalah konsonan
        letter = word[index]
        if self.huruf_konsonan(letter=letter):
            if letter == 'y' and self.huruf_konsonan(word[index - 1]):
                return False
            return True
        return False

    def vokal_perindex_kata(self, word: str, index: int) -> bool:
        # menentukan index kata adalah vokal
        return not self.konsonan_perindex_kata(word=word, index=index)

    def akhiran_s(self, stem: str, letter='s') -> bool:
        # *s stem akhiran_s S
        if stem.endswith(letter):
            return True
        return False

    def akhiran_konsonan_ganda(self, stem: str) -> bool:
        # *d stem memiliki akhiran konsonan yang sama
        if len(stem) < 2:
            return False
        if stem[-1] != stem[-2]:
            return False
        if not (self.konsonan_perindex_kata(word=stem, index=-1)
                and self.konsonan_perindex_kata(word=stem, index=-2)):
            return False
        return True

    def vokal_dalam_kata(self, stem: str) -> bool:
        # *v* stem yang mengandung vokal
        for letter in stem:
            if self.huruf_vokal(letter=letter):
                return True
        return False

    def buat_format(self, word: str) -> str:
        # mengembalikan urutan VC berdasarkan vokal dan konsonan kata
        form = str()
        for index in range(len(word)):
            if self.konsonan_perindex_kata(word=word, index=index):
                if index:
                    if not self.akhiran_s(stem=form, letter='C'):
                        form += 'C'
                else:
                    form += 'C'
            else:
                if index:
                    if not self.akhiran_s(stem=form, letter='V'):
                        form += 'V'
                else:
                    form += 'V'
        return form

    def hitung_vc(self, word: str) -> int:
        # dapatkan jumlah kemunculan VC dalam satu kata
        return self.buat_format(word=word).count('VC')

    def cvc(self, word: str) -> bool:
        # *o  penentuan stem berakhir dalam cvc, tetapi C kedua (konsonan) bukan W, X atau Y
        if len(word) < 3:
            return False
        if self.konsonan_perindex_kata(word=word, index=-1) and \
                self.vokal_perindex_kata(word=word, index=-2) and \
                self.konsonan_perindex_kata(word, index=-3):
            if word[-1] not in self.cvc_ignore:
                return True
            return False
        return False

    def ganti(self, origin: str, rem: str, rep: str, m=None) -> str:
        # Ganti akhiran kata asli yang dimasukkan
        if m is None:
            return origin[:origin.rfind(rem)] + rep
        else:
            base = origin[:origin.rfind(rem)]
            if self.hitung_vc(word=base) > m:
                return base + rep
            else:
                return origin

    def stem(self, word: str) -> str:
        if word.endswith('sses'):
            word = self.ganti(origin=word, rem='sess', rep='ss')
        elif word.endswith('ies'):
            word = self.ganti(origin=word, rem='ies', rep='i')
        elif word.endswith('ss'):
            word = self.ganti(origin=word, rem='ss', rep='ss')
        elif word.endswith('s'):
            word = self.ganti(origin=word, rem='s', rep='')

        flag = False
        if word.endswith('eed'):
            base = word[:word.rfind('edd')]
            if self.hitung_vc(word=base):
                word = base + 'ee'
        elif word.endswith('ed'):
            base = word[:word.rfind('ed')]
            if self.vokal_dalam_kata(stem=base):
                word = base
                flag = True
        elif word.endswith('ing'):
            base = word[:word.rfind('ing')]
            if self.vokal_dalam_kata(stem=word):
                word = base
                flag = True

        if flag:
            if word.endswith(
                ('at', 'bl', 'iz')
            ) or self.hitung_vc(word=word) == 1 and self.cvc(word=word):
                word += 'e'
            elif self.akhiran_konsonan_ganda(
                    stem=word) and not self.akhiran_s(
                        stem=word, letter='l') and not self.akhiran_s(
                            stem=word, letter='s') and not self.akhiran_s(
                                stem=word, letter='z'):
                word = word[:-1]

        if word.endswith('y'):
            base = word[:word.rfind('y')]
            if self.vokal_dalam_kata(stem=base):
                word = base + 'i'

        for x, y in static.step_a.items():
            if word.endswith(x):
                word = self.ganti(origin=word, rem=x, rep=y)

        for x, y in static.step_b.items():
            if word.endswith(x):
                word = self.ganti(origin=word, rem=x, rep=y)

        for x, y in static.step_c.items():
            if word.endswith(x):
                word = self.ganti(origin=word, rem=x, rep=y, m=1)

        if word.endswith('ion'):
            base = word[:word.rfind('ion')]
            if self.hitung_vc(word=base) > 1 and (
                    self.akhiran_s(stem=base, letter='s')
                    or self.akhiran_s(stem=base, letter='t')):
                word = base
            else:
                word = self.ganti(origin=word, rem='', rep='', m=1)

        if word.endswith('e'):
            base = word[:-1]
            m_count = self.hitung_vc(word=base)
            if m_count > 1 or (m_count == 1 and not self.cvc(word=base)):
                word = base

        if self.hitung_vc(
                word=word) > 1 and self.akhiran_konsonan_ganda(
                    stem=word) and self.akhiran_s(
                        stem=word, letter='l'):
            word = word[:-1]
        return word
        