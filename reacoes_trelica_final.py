import math

# =========================================================
# Análise Completa de Treliça (Reações e Nó A)
# Linguagem: Python  (Álgebra e Funções)
# =========================================================

# --- I. DADOS GERAIS E GEOMETRIA ---

# Cargas da Imagem
P_VERT_1 = 8.0   # kN, aplicada no Nó A
P_VERT_2 = 4.0   # kN, aplicada a 2m de A
P_VERT_3 = 10.0  # kN, aplicada a 4m de A
P_HORIZ = 3.0    # kN, para a esquerda, aplicada no Nó A

# Distâncias (m)
L1 = 2.0         # Posição de P_VERT_2
L_total = 4.0    # Distância total entre Apoios (A e B)
h = 1.5          # Altura da Treliça

# Soma total das forças verticais externas
Cargas_Verticais_Total = P_VERT_1 + P_VERT_2 + P_VERT_3 

print("##  Início da Análise Estrutural ##")
print(f"Cargas Verticais Total: {Cargas_Verticais_Total:.2f} kN | Horizontal: {P_HORIZ:.2f} kN")
print(f"Dimensões: Base = {L_total}m, Altura = {h}m")
print("-" * 40)


# --- II. ETAPA 1: CÁLCULO DAS REAÇÕES DE APOIO ---

# A. EQUAÇÃO ΣFx = 0
# R_Ax - P_HORIZ = 0
R_Ax = P_HORIZ

# B. EQUAÇÃO ΣMA = 0 (Encontrar R_By)
try:
    Momento_Total_Cargas = (P_VERT_2 * L1) + (P_VERT_3 * L_total) 
    R_By = Momento_Total_Cargas / L_total
    
    # C. EQUAÇÃO ΣFy = 0 (Encontrar R_Ay)
    R_Ay = Cargas_Verticais_Total - R_By 

    print("### 1. Reações de Apoio Encontradas ###")
    print(f"R_Ax (Pino): {R_Ax:.2f} kN (Direita)")
    print(f"R_Ay (Pino): {R_Ay:.2f} kN (Cima)")
    print(f"R_By (Rolete): {R_By:.2f} kN (Cima)")
    print("-" * 40)
    
except ZeroDivisionError:
    print("\nERRO DE CÁLCULO: A distância L_total não pode ser zero.")
    exit() # Interrompe a execução se houver erro

    
# --- III. ETAPA 2: MÉTODO DOS NÓS (NÓ A) ---

# Geometria e Componentes Trigonométricas da barra diagonal (F_AC)
b_no_A = L1 # Base da diagonal do Nó A é 2.0m
L_diag = math.sqrt(h**2 + b_no_A**2) # Comprimento da diagonal (2.5m)
cos_theta = b_no_A / L_diag # 0.8
sin_theta = h / L_diag      # 0.6

# A. EQUAÇÃO ΣFy = 0 (Encontrar F_AC)
# R_Ay (cima) - P_VERT_1 (baixo) + F_AC * sin_theta = 0
Forca_Vertical_Liquida = R_Ay - P_VERT_1 # 10.0 kN - 8.0 kN = 2.0 kN (cima)

# F_AC = - Forca_Vertical_Liquida / sin_theta
F_AC = - Forca_Vertical_Liquida / sin_theta

# B. EQUAÇÃO ΣFx = 0 (Encontrar F_AB)
# R_Ax (direita) - P_HORIZ (esquerda) + F_AB (direita) + F_AC * cos_theta (direita) = 0
Forca_Horizontal_Liquida = R_Ax - P_HORIZ # 3.0 kN - 3.0 kN = 0.0 kN

# F_AB = - (Forca_Horizontal_Liquida + F_AC * cos_theta)
F_AB = - (Forca_Horizontal_Liquida + F_AC * cos_theta)

print("### 2. Forças Internas no Nó A ###")
print(f"Ângulo da Diagonal (cos, sen): ({cos_theta:.1f}, {sin_theta:.1f})")
print(f"Força na Diagonal (F_AC): {F_AC:.3f} kN")
print(f"Força na Horizontal (F_AB): {F_AB:.3f} kN")
print("-" * 40)

# --- IV. INTERPRETAÇÃO DOS RESULTADOS ---

def interpretar_forca(forca, nome_barra):
    if forca < 0:
        return f"A barra {nome_barra} está em **Compressão** ({abs(forca):.3f} kN)"
    else:
        return f"A barra {nome_barra} está em **Tração** ({forca:.3f} kN)"

print("##  Interpretação Final ##")
print(interpretar_forca(F_AC, "AC (Diagonal)"))
print(interpretar_forca(F_AB, "AB (Base)"))