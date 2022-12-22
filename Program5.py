from Program4 import create_polynomial

with open('1polynomial', 'w') as polynomial_file_1:
    polynomial_file_1.write(f'{create_polynomial(int(input("input
polynomial degree: ")))}')
with open('1polynomial', 'r') as polynomial_file_1:
    pol_1 = polynomial_file_1.read()
with open('2polynomial', 'w') as polynomial_file_2:
    polynomial_file_2.write(f'{create_polynomial(int(input("input
polynomial degree: ")))}')
with open('2polynomial', 'r') as polynomial_file_2:
    pol_2 = polynomial_file_2.read()
pol_1 = pol_1.replace(' = 0', '')
pol_1 = pol_1.replace(' - ', ' -')
pol_1 = pol_1.replace(' + ', ' +')
if not pol_1[-1].isdigit():
    pol_1 = pol_1 + '^1'
pol_lst1 = pol_1.split(' ')
pol_2 = pol_2.replace(' = 0', '')
pol_2 = pol_2.replace(' - ', ' -')
pol_2 = pol_2.replace(' + ', ' +')
if not pol_2[-1].isdigit():
    pol_2 = pol_2 + '^1'
pol_lst2 = pol_2.split(' ')
result = []
for i in range(0, len(pol_lst1)):
    flag = 1
    for j in range(0, len(pol_lst2)):
        if pol_lst1[i][-1] == pol_lst2[j][-1]:
            flag = 0
            result.append(f'{int(pol_lst1[i][0 : -3]) +
int(pol_lst2[j][0 : -3])}x^{pol_lst2[j][-1]}')
    if flag:
        result.append(pol_lst1[i])
for i in range(0, len(pol_lst2)):
    flag = 1
    for j in range(0, len(pol_lst1)):
        if pol_lst2[i][-1] == pol_lst1[j][-1]:
            flag = 0
    if flag:
        result.append(pol_lst2[i])
for i in range(len(result) - 1):
    for j in range(len(result) - 1):
        if int(result[j][-1]) < int(result[j + 1][-1]):
            temp = result[j]
            result[j] = result[j + 1]
            result[j + 1] = temp
for i in range(1, len(result)):
    if result[i][0].isdigit():
        result[i] = '+' + result[i]
result.append('=0')
result = ''.join(result)
with open('result', 'w') as result_f:
    result_f.write(result)
