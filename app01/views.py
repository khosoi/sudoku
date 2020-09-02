from django.shortcuts import render
from app01.forms import sudokuForm

# Create your views here.
from django.contrib.auth.decorators import login_required

from pulp import *
import openpyxl
from openpyxl.styles import Font

@login_required
def app_dashboard(request):
    return render(request, 'app01/sudoku.html')

@login_required
def app_user(request):
    return render(request, 'app01/user.html')

@login_required
def app_icons(request):
    return render(request, 'app01/icons.html')

@login_required
def app_map(request):
    return render(request, 'app01/map.html')

@login_required
def app_maps(request):
    return render(request, 'app01/maps.html')

@login_required
def app_notifications(request):
    return render(request, 'app01/notifications.html')

@login_required
def app_rtl(request):
    return render(request, 'app01/rtl.html')

@login_required
def app_tables(request):
    return render(request, 'app01/tables.html')

@login_required
def app_typography(request):
    return render(request, 'app01/typography.html')

@login_required
def app_upgrade(request):
    return render(request, 'app01/upgrade.html')
    
@login_required
def app_sudoku(request):


    #return render(request, 'app01/sudoku.html', {'sudoku_form':sudoku_form})
    return render(request, 'app01/sudoku.html')

@login_required
def app_sudoku_clear(request):
    context  = {}

    sudoku_form = sudokuForm(context)

    #return render(request, 'app01/sudoku.html', {'sudoku_form':sudoku_form})
    return render(request, 'app01/sudoku.html', context)


@login_required
def app_sudoku_solve(request):
    requestList = request.POST.getlist('number', None)
    #print(requestList)
    sudokuList = list(zip(*[iter(requestList)]*9))
    #print(sudokuList)
    N = [n for n in range(1,10)]

    U = [u*3+1 for u in range(3)]

    # 数理最適化問題を宣言（名前をつける必要あり）
    model = LpProblem('sudoku', LpMaximize)


    # 変数を宣言
    x = LpVariable.dicts("X",(N,N,N),0,1,LpInteger)

    # 定式化
    # 目的関数を宣言（最小化）
    model += lpSum([x[i][j][k] for i in N for j in N for k in N])

    # 制約条件を宣言
    for j in N:
        for k in N:
            model += lpSum([x[i][j][k] for i in N]) == 1
    for i in N:
        for k in N:
            model += lpSum([x[i][j][k] for j in N]) == 1
    for i in N:
        for j in N:
            model += lpSum([x[i][j][k] for k in N]) == 1
    for k in N:
        for s in U:
            for t in U:
                model += lpSum([x[i][j][k] for i in range(s,s+3) for j in range(t,t+3)]) == 1
    for i in N:
        for j in N:
            if sudokuList[i-1][j-1] != "":
                k=int(sudokuList[i-1][j-1])
                model += x[i][j][k] == 1

    # 最適化を実施
    #start_time = time.time()
    s=model.solve()
    #elapsed_time = time.time() - start_time

    print(f'-' * 40)
    print(f'[出力]')
    # テキスト出力
    #prob.printSolution()

    print(f'-' * 32)
    # 目的関数値や変数の値を個別に取得
    #print(f'目的関数値 = {prob.getObjVal()}')
    sudokuSolveList={}
    for i in N:
        for j in N:
            for k in N:
                if pulp.value(x[i][j][k]) >= 1:
                    sudokuSolveList[(i,j)]=k


    print(f'-' * 40)
    print(f'finish')
    #print(sudokuSolveList)


    context  = {'x11': sudokuSolveList[(1,1)],
            'x12': sudokuSolveList[(1,2)],
            'x13': sudokuSolveList[(1,3)],
            'x14': sudokuSolveList[(1,4)],
            'x15': sudokuSolveList[(1,5)],
            'x16': sudokuSolveList[(1,6)],
            'x17': sudokuSolveList[(1,7)],
            'x18': sudokuSolveList[(1,8)],
            'x19': sudokuSolveList[(1,9)],
            
            'x21': sudokuSolveList[(2,1)],
            'x22': sudokuSolveList[(2,2)],
            'x23': sudokuSolveList[(2,3)],
            'x24': sudokuSolveList[(2,4)],
            'x25': sudokuSolveList[(2,5)],
            'x26': sudokuSolveList[(2,6)],
            'x27': sudokuSolveList[(2,7)],
            'x28': sudokuSolveList[(2,8)],
            'x29': sudokuSolveList[(2,9)],
            
            'x31': sudokuSolveList[(3,1)],
            'x32': sudokuSolveList[(3,2)],
            'x33': sudokuSolveList[(3,3)],
            'x34': sudokuSolveList[(3,4)],
            'x35': sudokuSolveList[(3,5)],
            'x36': sudokuSolveList[(3,6)],
            'x37': sudokuSolveList[(3,7)],
            'x38': sudokuSolveList[(3,8)],
            'x39': sudokuSolveList[(3,9)],
            
            'x41': sudokuSolveList[(4,1)],
            'x42': sudokuSolveList[(4,2)],
            'x43': sudokuSolveList[(4,3)],
            'x44': sudokuSolveList[(4,4)],
            'x45': sudokuSolveList[(4,5)],
            'x46': sudokuSolveList[(4,6)],
            'x47': sudokuSolveList[(4,7)],
            'x48': sudokuSolveList[(4,8)],
            'x49': sudokuSolveList[(4,9)],
            
            'x51': sudokuSolveList[(5,1)],
            'x52': sudokuSolveList[(5,2)],
            'x53': sudokuSolveList[(5,3)],
            'x54': sudokuSolveList[(5,4)],
            'x55': sudokuSolveList[(5,5)],
            'x56': sudokuSolveList[(5,6)],
            'x57': sudokuSolveList[(5,7)],
            'x58': sudokuSolveList[(5,8)],
            'x59': sudokuSolveList[(5,9)],
            
            'x61': sudokuSolveList[(6,1)],
            'x62': sudokuSolveList[(6,2)],
            'x63': sudokuSolveList[(6,3)],
            'x64': sudokuSolveList[(6,4)],
            'x65': sudokuSolveList[(6,5)],
            'x66': sudokuSolveList[(6,6)],
            'x67': sudokuSolveList[(6,7)],
            'x68': sudokuSolveList[(6,8)],
            'x69': sudokuSolveList[(6,9)],

            'x71': sudokuSolveList[(7,1)],
            'x72': sudokuSolveList[(7,2)],
            'x73': sudokuSolveList[(7,3)],
            'x74': sudokuSolveList[(7,4)],
            'x75': sudokuSolveList[(7,5)],
            'x76': sudokuSolveList[(7,6)],
            'x77': sudokuSolveList[(7,7)],
            'x78': sudokuSolveList[(7,8)],
            'x79': sudokuSolveList[(7,9)],

            'x81': sudokuSolveList[(8,1)],
            'x82': sudokuSolveList[(8,2)],
            'x83': sudokuSolveList[(8,3)],
            'x84': sudokuSolveList[(8,4)],
            'x85': sudokuSolveList[(8,5)],
            'x86': sudokuSolveList[(8,6)],
            'x87': sudokuSolveList[(8,7)],
            'x88': sudokuSolveList[(8,8)],
            'x89': sudokuSolveList[(8,9)],

            'x91': sudokuSolveList[(9,1)],
            'x92': sudokuSolveList[(9,2)],
            'x93': sudokuSolveList[(9,3)],
            'x94': sudokuSolveList[(9,4)],
            'x95': sudokuSolveList[(9,5)],
            'x96': sudokuSolveList[(9,6)],
            'x97': sudokuSolveList[(9,7)],
            'x98': sudokuSolveList[(9,8)],
            'x99': sudokuSolveList[(9,9)]
            }

    #sudoku_form = sudokuForm(context)

    return render(request, 'app01/sudoku_solve.html', context)
