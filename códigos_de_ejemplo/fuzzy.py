# fuzzy.py - Módulo de lógica difusa para CircuitPython (Sumobot)
# Autor: Tomás de Camino Beck, adaptado por ChatGPT
# Licencia: MIT

# Clase que define un conjunto difuso con sus límites y función de pertenencia
class FuzzyDef:
    def __init__(self, mina=0, minb=0, maxa=0, maxb=0, membership=None):
        self.mina = mina      # Límite inferior del inicio de la curva
        self.minb = minb      # Límite inferior del plato del trapecio
        self.maxa = maxa      # Límite superior del plato del trapecio
        self.maxb = maxb      # Límite superior de la curva
        self.centroid = 0     # Centroide del conjunto, usado para desfusificación
        self.membership = membership  # Función de pertenencia (e.g. triangular, trapezoidal)
        self.miu = 0.0        # Grado de pertenencia (resultado entre 0 y 1)

    # Calcula el centroide para métodos de desfusificación
    def set_centroid(self):
        if self.minb > 0:
            self.centroid = (self.maxa + self.minb) / 2.0
        else:
            self.centroid = (self.mina + self.maxa) / 2.0

# Función auxiliar para forma triangular simétrica
def triangle_value(t):
    return max(1 - abs(t), 0)

# Función de pertenencia triangular
def triangle(fset, x):
    mid = ((fset.maxa - fset.mina) / 2.0) + fset.mina
    if x < fset.mina or x > fset.maxa:
        return 0
    return triangle_value((x - mid) / (fset.maxa - fset.mina) * 2.0)

# Función de pertenencia creciente (forma de rampa positiva)
def increasing(fset, x):
    if x < fset.mina:
        return 0
    if x > fset.maxa:
        return 1
    return (x - fset.mina) / (fset.maxa - fset.mina)

# Función de pertenencia decreciente (forma de rampa negativa)
def decreasing(fset, x):
    if x < fset.mina:
        return 1
    if x > fset.maxa:
        return 0
    return (fset.maxa - x) / (fset.maxa - fset.mina)

# Función de pertenencia trapezoidal
def trapezoid(fset, x):
    if x < fset.mina or x > fset.maxb:
        return 0
    if fset.maxa <= x <= fset.minb:
        return 1
    if fset.mina <= x <= fset.maxa:
        return increasing(fset, x)
    if fset.minb <= x <= fset.maxb:
        return decreasing(fset, x)
    return 0

# Calcula y guarda el grado de verdad (miu) para un valor v dado
def truth_degree(fset, v):
    fset.miu = fset.membership(fset, v)
    return fset.miu

# Unión difusa (OR): elige el valor más alto de pertenencia
def fuzzy_union(set1, set2, v):
    return max(truth_degree(set1, v), truth_degree(set2, v))

# Intersección difusa (AND): elige el valor más bajo
def fuzzy_intersection(set1, set2, v):
    return min(truth_degree(set1, v), truth_degree(set2, v))

# Verifica si un conjunto tiene pertenencia mayor a cero
def is_member(fset):
    return fset.miu > 0

# Condición lógica AND entre dos conjuntos difusos
def is_member_and(set1, set2):
    return set1.miu > 0 and set2.miu > 0

# AND para tres conjuntos
def is_member_and3(set1, set2, set3):
    return set1.miu > 0 and set2.miu > 0 and set3.miu > 0

# Condición lógica OR entre dos conjuntos difusos
def is_member_or(set1, set2):
    return set1.miu > 0 or set2.miu > 0

# OR para tres conjuntos
def is_member_or3(set1, set2, set3):
    return set1.miu > 0 or set2.miu > 0 or set3.miu > 0

# Asigna un valor máximo al grado de pertenencia
def set_miu(fset, v):
    fset.miu = max(fset.miu, v)

# Clase que representa un dominio difuso (conjunto de FuzzyDefs)
class FuzzyDomain:
    def __init__(self, nset):
        self.fset = []     # Lista de conjuntos difusos
        self.nset = nset   # Número total de conjuntos
        for i in range(nset):
            self.fset.append(FuzzyDef())

    # Reinicia todos los grados de pertenencia del dominio
    def reset_domain(self):
        for f in self.fset:
            f.miu = 0

    # Calcula el grado de pertenencia de cada conjunto para un valor dado
    def truth_degree(self, v):
        for f in self.fset:
            truth_degree(f, v)

    # Define el rango de valores y asigna funciones de pertenencia a cada conjunto
    def set_domain(self, minvalue, maxvalue):
        if self.nset <= 1:
            return
        d = (maxvalue - minvalue) / (self.nset + 1.0)
        s = self.nset - 1

        # Primer conjunto con pendiente negativa
        self.fset[0].mina = minvalue + d
        self.fset[0].maxa = minvalue + 2 * d
        self.fset[0].membership = decreasing
        self.fset[0].set_centroid()

        # Conjuntos intermedios triangulares
        for i in range(1, s):
            self.fset[i].mina = minvalue + i * d
            self.fset[i].maxa = minvalue + (i + 2) * d
            self.fset[i].membership = triangle
            self.fset[i].set_centroid()

        # Último conjunto con pendiente positiva
        self.fset[s].mina = maxvalue - 2 * d
        self.fset[s].maxa = maxvalue - d
        self.fset[s].membership = increasing
        self.fset[s].set_centroid()

    # Desfusificación: promedio ponderado de centroides
    def defuzzify_weighted_average(self):
        wsum = 0
        sum_miu = 0
        for f in self.fset:
            wsum += f.miu * f.centroid
            sum_miu += f.miu
        if sum_miu == 0:
            return 0
        return wsum / sum_miu
