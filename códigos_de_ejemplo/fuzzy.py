# fuzzy.py - Módulo de lógica difusa para CircuitPython (Sumobot)
# Autor: Tomás de Camino Beck, adaptado por ChatGPT
# Licencia: MIT

from typing import Callable, List

# Clase que define una función de membresía difusa
class FuzzyDef:
    def __init__(self, mina=0, minb=0, maxa=0, maxb=0, membership=None):
        self.mina = mina      # Límite inferior del soporte
        self.minb = minb      # Inicio del núcleo del trapecio (si aplica)
        self.maxa = maxa      # Fin del núcleo o pico del triángulo
        self.maxb = maxb      # Límite superior del soporte (si aplica)
        self.centroid = 0     # Centro de gravedad del conjunto difuso
        self.membership = membership  # Función de membresía asignada
        self.miu = 0.0        # Grado de verdad actual para un valor dado

    # Calcula el centroide según los valores definidos
    def set_centroid(self):
        if self.minb > 0:
            self.centroid = (self.maxa + self.minb) / 2
        else:
            self.centroid = (self.mina + self.maxa) / 2

# Función auxiliar que devuelve valor triangular entre 0 y 1
def triangle_value(t: float) -> float:
    return max(1 - abs(t), 0)

# Función de membresía triangular
def triangle(fset: FuzzyDef, x: float) -> float:
    mid = ((fset.maxa - fset.mina) / 2) + fset.mina
    if x < fset.mina or x > fset.maxa:
        return 0
    return triangle_value((x - mid) / (fset.maxa - fset.mina) * 2)

# Función de membresía creciente (rampa de 0 a 1)
def increasing(fset: FuzzyDef, x: float) -> float:
    if x < fset.mina:
        return 0
    if x > fset.maxa:
        return 1
    return (x - fset.mina) / (fset.maxa - fset.mina)

# Función de membresía decreciente (rampa de 1 a 0)
def decreasing(fset: FuzzyDef, x: float) -> float:
    if x < fset.mina:
        return 1
    if x > fset.maxa:
        return 0
    return (fset.maxa - x) / (fset.maxa - fset.mina)

# Función de membresía trapezoidal
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

# Calcula y almacena el grado de verdad (miu) para un valor dado
def truth_degree(fset: FuzzyDef, v: float) -> float:
    fset.miu = fset.membership(fset, v)
    return fset.miu

# Unión difusa (máximo de los grados de verdad)
def fuzzy_union(set1: FuzzyDef, set2: FuzzyDef, v: float) -> float:
    return max(truth_degree(set1, v), truth_degree(set2, v))

# Intersección difusa (mínimo de los grados de verdad)
def fuzzy_intersection(set1: FuzzyDef, set2: FuzzyDef, v: float) -> float:
    return min(truth_degree(set1, v), truth_degree(set2, v))

# Verifica si un conjunto tiene grado de verdad mayor que cero
def is_member(fset: FuzzyDef) -> bool:
    return fset.miu > 0

# Verifica si todos los conjuntos tienen miu > 0 (AND lógico)
def is_member_and(*sets: FuzzyDef) -> bool:
    return all(s.miu > 0 for s in sets)

# Verifica si alguno de los conjuntos tiene miu > 0 (OR lógico)
def is_member_or(*sets: FuzzyDef) -> bool:
    return any(s.miu > 0 for s in sets)

# Establece un nuevo valor de miu si es mayor que el actual
def set_miu(fset: FuzzyDef, v: float):
    fset.miu = max(fset.miu, v)

# Clase que define un dominio difuso compuesto por múltiples conjuntos
class FuzzyDomain:
    def __init__(self, nset: int):
        # Crea una lista de n conjuntos difusos
        self.fset: List[FuzzyDef] = [FuzzyDef() for _ in range(nset)]
        self.nset = nset

    # Reinicia los grados de verdad de todos los conjuntos
    def reset_domain(self):
        for f in self.fset:
            f.miu = 0

    # Calcula el grado de verdad de cada conjunto para un valor dado
    def truth_degree(self, v: float):
        for f in self.fset:
            truth_degree(f, v)

    # Define automáticamente el dominio dividiendo un rango entre los conjuntos
    def set_domain(self, minvalue: float, maxvalue: float):
        if self.nset <= 1:
            return
        d = (maxvalue - minvalue) / (self.nset + 1)
        s = self.nset - 1

        # Primer conjunto: función decreciente
        self.fset[0].mina = minvalue + d
        self.fset[0].maxa = minvalue + 2 * d
        self.fset[0].membership = decreasing
        self.fset[0].set_centroid()

        # Conjuntos intermedios: funciones triangulares
        for i in range(1, s):
            self.fset[i].mina = minvalue + i * d
            self.fset[i].maxa = minvalue + (i + 2) * d
            self.fset[i].membership = triangle
            self.fset[i].set_centroid()

        # Último conjunto: función creciente
        self.fset[s].mina = maxvalue - 2 * d
        self.fset[s].maxa = maxvalue - d
        self.fset[s].membership = increasing
        self.fset[s].set_centroid()

    # Defuzzificación por media ponderada: centroide ponderado por miu
    def defuzzify_weighted_average(self) -> float:
        wsum = sum(f.miu * f.centroid for f in self.fset)
        sum_miu = sum(f.miu for f in self.fset)
        if sum_miu == 0:
            return 0
        return wsum / sum_miu
