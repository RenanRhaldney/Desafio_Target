'''
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
'''

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
soma = SP + RJ + MG + ES + OUTROS

percent_sp = SP * 100 / soma
percent_rj = RJ * 100 / soma
percent_mg = MG * 100 / soma
percent_es = ES * 100 / soma
percent_outros = OUTROS * 100 / soma


print(f'Porcentagem de SP = {percent_sp:.2f}%')
print(f'Porcentagem de RJ = {percent_rj:.2f}%')
print(f'Porcentagem de MG = {percent_mg:.2f}%')
print(f'Porcentagem de ES = {percent_es:.2f}%')
print(f'Porcentagem de OUTROS = {percent_outros:.2f}%')
