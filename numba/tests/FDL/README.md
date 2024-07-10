
这个FDL/flowlang项目的调研文档  
1. a numba AOT sample  
- 编译生成my_module  
python pycc.py
- 运行测试用例  
python my_test.py  
2. a numba JIT sample  
- 运行测试用例  
python my_test.py

3. my_test_main.py  
是为了更好的运行指定用例  

4. .vscode里面有一个launch.json，可以配置调试用例
- 为了能调试第三方源码，justMyCode设置为false  
- NUMBA_DUMP_IR设置为0，不打印IR  
- python路径设置为conda环境中的python路径  
```
      "justMyCode": false,
      "env": {
        "NUMBA_DUMP_IR": "0"
      },
      "python": "/home/wangmingfa/anaconda3/envs/numbaenv/bin/python",
```
