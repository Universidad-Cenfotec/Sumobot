
# fuzzy.py - Módulo de lógica difusa para CircuitPython (Sumobot)
# Autor: Tomás de Camino Beck, adaptado por ChatGPT
# Licencia: MIT

from typing import Callable, List

class FuzzyDef:
    def __init__(self, mina=0, minb=0, maxa=0, maxb=0, membership=None):
        self.mina = mina
        self.minb = minb
        self.maxa = maxa
        self.maxb = maxb
        self.centroid = 0
        self.membership = membership
        self.miu = 0.0

    def set_centroid(self):
        if self.minb > 0:
            self.centroid = (self.maxa + self.minb) / 2
        else:
            self.centroid = (self.mina + self.maxa) / 2

def triangle_value(t: float) -> float:
    return max(1 - abs(t), 0)

def triangle(fset: FuzzyDef, x: float) -> float:
    mid = ((fset.maxa - fset.mina) / 2) + fset.mina
    if x < fset.mina or x > fset.maxa:
        return 0
    return triangle_value((x - mid) / (fset.maxa - fset.mina) * 2)

def increasing(fset: FuzzyDef, x: float) -> float:
    if x < fset.mina:
        return 0
    if x > fset.maxa:
        return 1
    return (x - fset.mina) / (fset.maxa - fset.mina)

def decreasing(fset: FuzzyDef, x: float) -> float:
    if x < fset.mina:
        return 1
    if x > fset.maxa:
        return 0
    return (fset.maxa - x) / (fset.maxa - fset.mina)

def trapezoid(fset: FuzzyDef, x: float) -> float:
    if x < fset.mina or x > fset.maxb:
        return 0
    if fset.maxa <= x <= fset.minb:
        return 1
    if fset.mina <= x <= fset.maxa:
        return increasing(fset, x)
    if fset.minb <= x <= fset.maxb:
        return decreasing(fset, x)
    return 0

def truth_degree(fset: FuzzyDef, v: float) -> float:
    fset.miu = fset.membership(fset, v)
    return fset.miu

def fuzzy_union(set1: FuzzyDef, set2: FuzzyDef, v: float) -> float:
    return max(truth_degree(set1, v), truth_degree(set2, v))

def fuzzy_intersection(set1: FuzzyDef, set2: FuzzyDef, v: float) -> float:
    return min(truth_degree(set1, v), truth_degree(set2, v))

def is_member(fset: FuzzyDef) -> bool:
    return fset.miu > 0

def is_member_and(*sets: FuzzyDef) -> bool:
    return all(s.miu > 0 for s in sets)

def is_member_or(*sets: FuzzyDef) -> bool:
    return any(s.miu > 0 for s in sets)

def set_miu(fset: FuzzyDef, v: float):
    fset.miu = max(fset.miu, v)

class FuzzyDomain:
    def __init__(self, nset: int):
        self.fset: List[FuzzyDef] = [FuzzyDef() for _ in range(nset)]
        self.nset = nset

    def reset_domain(self):
        for f in self.fset:
            f.miu = 0

    def truth_degree(self, v: float):
        for f in self.fset:
            truth_degree(f, v)

    def set_domain(self, minvalue: float, maxvalue: float):
        if self.nset <= 1:
            return
        d = (maxvalue - minvalue) / (self.nset + 1)
        s = self.nset - 1

        self.fset[0].mina = minvalue + d
        self.fset[0].maxa = minvalue + 2 * d
        self.fset[0].membership = decreasing
        self.fset[0].set_centroid()

        for i in range(1, s):
            self.fset[i].mina = minvalue + i * d
            self.fset[i].maxa = minvalue + (i + 2) * d
            self.fset[i].membership = triangle
            self.fset[i].set_centroid()

        self.fset[s].mina = maxvalue - 2 * d
        self.fset[s].maxa = maxvalue - d
        self.fset[s].membership = increasing
        self.fset[s].set_centroid()

    def defuzzify_weighted_average(self) -> float:
        wsum = sum(f.miu * f.centroid for f in self.fset)
        sum_miu = sum(f.miu for f in self.fset)
        if sum_miu == 0:
            return 0
        return wsum / sum_miu
