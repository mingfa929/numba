from numba.pycc import CC

cc = CC('my_module')

cc.verbose = True                   # 取消注释以下行,以打印出编译步骤


@cc.export('multf', 'f8(f8, f8)')   # 双精度浮点
@cc.export('multi', 'i4(i4, i4)')   # 32位整数
def mult(a, b):

    return a * b


@cc.export('square', 'f8(f8)')
def square(a):

    return a ** 2


if __name__ == "__main__":          # 生成名为的扩展模块 my_module.pyd

    cc.compile()
