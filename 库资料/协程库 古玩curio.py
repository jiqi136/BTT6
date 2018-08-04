
import curio  #导入协程 curio

a=''
if '协程概念' in a:
    if '协程是一个使用定义的函数，例如：async def' in a:
        async def hello(name):
            return 'Hello ' + name

    if '协程调用其他协程使用 await 例如：' in a:
        async def main(name):
            s = await hello(name)
            print(s)

    if '与常规函数不同的是，协程永远无法自行运行。' \
       '它总是必须在管理者（例如，事件循环，内核等）的监督下执行。' \
       '在 curio，一个初始的协程是由一个低级内核使用该 run()函数来执行的。例如：' in a:

        curio.run(main, 'Guido')

        a = '当通过古玩 curio 执行时，协程被认为是“任务”。每当使用单词“任务（Task）”时，它指的是协程的执行。'



    if '协程概念' in a:
    if '协程概念' in a:

