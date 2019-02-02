class Dice:
    @staticmethod
    def get_roll(n, size):
        import random

        r = {}
        v = 0
        for i in range(n):
            r[i] = random.randint(1, size)
            v += r[i]

        r["n"] = n
        r["size"] = size
        r["total"] = v

        return r
