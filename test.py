import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']


# 函数 drawing 传入参数`path`表示文件路径
def drawing(path):
    # *********** Begin **********#
    prov, grades = [], []
    f = open(path, 'r', encoding='utf8')
    while True:
        line = f.readline()
        if line == '':
            break
        flds = line.split()
        try:
            grades.append(int(flds[0]))
            prov.append(flds[1])
        except:
            pass
    gradesRank = sorted(grades)[::-1]
    gradesRank = gradesRank[:3]
    provRank = []
    for i in range(len(gradesRank)):
        provRank.append(prov[grades.index(gradesRank[i])])
        plt.text(i, gradesRank[i] - 50, gradesRank[i], ha='center', fontsize=16)
    plt.bar(range(len(gradesRank)), gradesRank, color='rgb', tick_label=provRank)
    plt.savefig('./结果/a.png')
    plt.show()

    # 将图片文件保存至 `./结果/a.png`

    # *********** End **********#

drawing("test.txt")