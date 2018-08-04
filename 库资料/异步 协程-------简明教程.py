a='' #if '' in a:
b=''
if '' in a:c=""""""
if ' 异步 asyncio-I / O' in a:
    if '运行事件循环' in a:
        if '获取当前上下文的事件循环' in a:
            c="""要获取当前上下文的事件循环，请使用get_event_loop（）。
                这将返回实现下面指定接口的事件循环对象，
                或者在没有为当前上下文设置事件循环的情况下引发异常，
                并且当前策略未指定创建一个事件循环。它不应该返回None。"""
            c="""预计get_event_loop（）根据上下文返回不同的事件循环对象（事实上，这是上下文的定义）。
                如果没有设置并且策略允许创建，它可以创建一个新的事件循环对象。
                默认的策略将仅在主线程中创建一个新的事件循环（由threading.py，
                它采用了特殊的子类，主线程定义），且仅当 get_event_loop（）之前被调用set_event_loop（）是不断调用。
                （要重置此状态，请重置策略。）在其他线程中，必须明确设置事件循环。其他政策可能会有不同的表现。
                由默认策略创建的事件循环是懒惰的; 即第一次调用get_event_loop（） 
                根据需要创建一个事件循环实例，并由当前策略指定。"""
        if '为当前上下文设置事件循环' in a:
            c="""要为当前上下文设置事件循环，请使用 set_event_loop（event_loop），
            其中event_loop是事件循环对象，即AbstractEventLoop的实例，或者是None。
            可以将当前事件循环设置为None，在这种情况下，
            对get_event_loop（）的后续调用将引发异常。
            这对于测试不应该依赖于默认事件循环的代码是很有用的。"""
        if '第三个策略函数：new_event_loop（）' in a:
            c="""为了单元测试和其他特殊情况的好处，还有第三个策略函数：new_event_loop（），
            它根据策略的默认规则创建并返回一个新的事件循环对象。
            要使其成为当前事件循环，必须使用它调用set_event_loop（）。"""
        if '要更改事件循环策略' in a:
            c="""要更改事件循环策略，请调用 set_event_loop_policy（policy），
            其中policy是事件循环策略对象或None。如果不是None，则策略对象必须是AbstractEventLoopPolicy的一个实例，
            该实例定义方法 get_event_loop（），set_event_loop（loop）和 new_event_loop（），
            其行为与上述函数类似。"""
    if '明确地传递事件循环' in a:
        c="""可以编写使用事件循环的代码，而无需依赖全局或每个线程的默认事件循环。
            为此，所有需要访问当前事件循环（而不是事件类中的方法）的API都需要一个名为loop的可选关键字参数。
            如果这个参数是None或者unspecified，那么这个API会调用 get_event_loop（）来获取默认的事件循环，
            但是如果 循环关键字参数被设置为一个事件循环对象，他们将使用该事件循环，
            并且将其传递给其他任何其他的循环他们调用的这些API。例如，Future（loop = my_loop）
            将创建绑定到事件循环my_loop的Future。当默认的当前事件是 None时，循环关键字参数是有效的。
            请注意，显式传递的事件循环必须仍然属于当前线程;
            在循环关键字参数不会奇迹般地改变事件循环如何被使用的约束。"""
    
    if '指定时间' in a:
        a="""像往常一样在Python中，所有超时，间隔和延迟都是以秒为单位来测量的，
        并且可以是整数或浮点数。但是，绝对时间不是指定为POSIX时间戳。时钟的准确性，
        精确性和时代性都取决于实施。
        默认实现使用time.monotonic（）。
        书可以写出这个选择的含义。更好地阅读标准库时间模块的文档。"""
    if '嵌入事件循环' in a:
        a="""在一些平台上，系统提供事件循环。当用户代码开始时，
        这样的循环可能已经在运行，并且可能没有办法停止或关闭它而不退出程序。在这种情况下，
        启动，停止和关闭事件循环的方法可能无法实现，并且is_running（）可能总是返回 True。"""
    if '事件循环类' in a:
        a="""没有名为EventLoop的实际类。有一个 AbstractEventLoop类，
        它定义了所有没有实现的方法，主要作为文档。定义了以下具体类：
            SelectorEventLoop是基于选择器模块（Python 3.4中的新增功能）的完整API的具体实现。
        构造函数接受一个可选参数selectors.Selector 对象。
        默认情况下，会创建并使用selectors.DefaultSelector的一个实例。
            ProactorEventLoop是API的具体实现，除了I / O事件处理和信号处理方法外。
        它只在Windows（或其他支持“重叠I / O”类似API的平台上定义）。构造函数接受一个可选参数Proactor对象。
        默认情况下创建并使用IocpProactor的一个实例 。
        （IocpProactor类不是由此PEP指定的;它只是ProactorEventLoop类的实现细节。）"""
    if '事件循环方法概述' in a:
        if '所有符合事件循环的实现都必须支持第一组类别' in a:
            a="""符合事件循环的方法分为几类。所有符合事件循环的实现都必须支持第一组类别，
                但嵌入事件循环可能不会实现启动，停止和关闭的方法。
                （但是，部分符合事件循环仍然比没有好。:-)"""
            a="""开始，停止和关闭：
                run_forever（）， run_until_complete（），
                stop（），is_running（），
                close（）， is_closed（）。"""
            a="""基本的和定时的回调：
                call_soon（），call_later（），
                call_at（），time（）。"""
            a="""线程交互：
                call_soon_threadsafe（）， run_in_executor（），
                set_default_executor（）。"""
            a="""互联网名称查找：
                getaddrinfo（），getnameinfo（）。"""
            a="""Internet连接：
                create_connection（），create_server（）， 
                create_datagram_endpoint（）。"""
            a="""包装套接字方法：
                sock_recv（），sock_sendall（）， 
                sock_connect（），sock_accept（）。"""
            a="""任务和期货支持：
                create_future（），create_task（），
                set_task_factory（），get_task_factory（）。"""
            a="""错误处理：
                get_exception_handler（），set_exception_handler（）， 
                default_exception_handler（），call_exception_handler（）。"""
            a="""调试模式：
                get_debug（），set_debug （）。"""
        
        if '第二组类别' in a:
            a="""第二组类别可以由一致的事件循环实现来支持。
                如果不支持，他们将引发 NotImplementedError。
                （在默认实现中， UNIX系统上的SelectorEventLoop支持所有这些;
                Windows上的SelectorEventLoop支持I / O事件处理类别;                 
                Windows上的ProactorEventLoop支持管道和子流程类别。"""
            a="""I / O回调：
                add_reader（），remove_reader（），
                add_writer（），remove_writer（）。"""
            a="""管道和子进程：
                connect_read_pipe（）， connect_write_pipe（），
                subprocess_shell（）， subprocess_exec（）。"""
            a="""信号回调：
                add_signal_handler（）， remove_signal_handler（）。"""
    if '事件循环方法' in a:
        if '开始，停止和结束' in a:
            if 'run_forever（）。运行事件循环，直到调用stop（）。' in a:
                a="""当事件循环已经运行时，不能调用它。
                    （这有一个长名字，部分是为了避免与早期版本的PEP混淆，run（）有不同的行为，部分原因是已经有太多的API有run（）方法，
                    部分原因是应该无论如何，这里不会有很多地方。）"""
            if 'run_until_complete（将来）。运行事件循环直到未来完成。' in a:
                a="""如果未来完成，则返回结果或引发异常。当事件循环已经运行时，不能调用它。
                如果参数是一个协程，该方法将创建一个新的Task对象。"""
            if 'stop()。一旦方便，就停止事件循环。' in a:
                a="""随后用run_forever（）或 run_until_complete（）重新启动循环就好了 ; 
                如果这样做没有预定的回调将被丢失。注意：stop（）正常返回，并且允许当前的回调继续。
                在这之后，事件循环停止的时间是多久，取决于实现，但是意图是停止对I / O轮询，
                并且不运行将来计划的任何回调。一个实现的主要自由是多少“准备好的队列”（call_soon（）
                已经预定的回调 ）在停止之前处理。"""
            if 'is_running（）。条件判断' in a:
                a="""如果事件循环当前正在运行，则返回True;如果停止，则返回False。"""
            if 'close()。关闭事件循环，释放它可能持有的任何资源' in a:
                a="""如epoll（）或 kqueue（）使用的文件描述符，以及默认的执行程序。
                在事件循环运行时不应该调用它。在调用之后，事件循环不应该再次使用。
                它可能被称为多次; 随后的电话是没有操作。"""
            if 'is_closed（）。如果事件循环关闭则返回True， 否则返回False。' in a:
                a="""（主要用于错误报告;请不要实现基于此方法的功能。）"""
        if '' in a:
                    if '' in a:
    if '时间延迟' in a:
        a="""协程asyncio.sleep（延迟）在给定的时间延迟后返回。"""
if '定义协程 async 语法' in a:
        if '定义协程' in a:a="""例：
            async def data(db):
                pass"""
        if '协程的关键属性：' in a:
            a="""异步def函数总是协程，即使它们不包含等待表达式。
                在异步函数中有一个SyntaxError表达式的yield或 yield from。
                内部引入了两个新的代码对象标志：
                    CO_COROUTINE用于标记本地协程 （用新语法定义）。
                    CO_ITERABLE_COROUTINE用于使基于生成器的协程与本地协程兼容（由 types.coroutine（）函数设置）。
                普通生成器在被调用时返回一个生成器对象 ; 同样，协程返回一个协程对象。
                StopIteration异常不会传播出协程，而会被RuntimeError所取代。对于普通发电机组，这种行为需要将来进口（见PEP 479）。
                当本地协程被垃圾收集时， 如果从未等待，则会引发RuntimeWarning（另请参阅 调试功能）。
                另请参阅协程对象部分。
            """
        if '等待表达 await ' in a:
            a="""以下新的await表达式用于获取协程执行的结果：
                async def read_data（db）：
                    data = await db.fetch（'SELECT ...'）
                    ...
                """
            if 'await等待' in a:
                a="""await等待，类似于  产生yield from，暂停执行 read_data协同程序，
                直到db.fetch 等待完成并返回结果数据。
                它使用实现中的收益，并验证其参数。 等待只接受一个等待，可以是其中之一："""
                a="""一个原生协程对象从返回的本地协程功能。
                    甲发电的协程对象从装饰的函数返回（）types.coroutine。
                    带有__await__方法的对象返回一个迭代器。
                    来自连锁通话的任何收益以收益率结束。这是期货如何实施的基本机制。因为，在内部，协同程序是一种特殊的发电机，每一个 等待被暂停的产量某处链 等待调用（请参阅PEP 3156的详细解释）。
                    为了启用协程的这种行为，添加了一个叫做__await__的新的魔术方法 。例如，在asyncio中，为了 在等待语句中启用Future对象，唯一的变化是将__await__ = __iter__行添加 到asyncio.Future类。
                    带有__await__方法的对象在PEP的其余部分被称为类似Future的对象。
                    这是一个TypeError，如果__await__返回的只是一个迭代器。
                    使用CPython C API和tp_as_async.am_await 函数定义对象，并返回一个迭代器（类似于__await__方法）。
                    这是一个SyntaxError使用异步def 函数之外的等待（就像它是一个SyntaxError来使用除def函数之外的 yield）。
                    它是一种类型错误比一个其他任何传递awaitable对象到一个等待表达。"""
                if '更新了运算符优先级表' in a:
                    if 'await 等待关键字定义如下：' in a:
                        power ::=  await ["**" u_expr]
                        await ::=  ["await"] primary
                    if '其中“主要”代表语言的最紧密绑定的操作。其语法是：' in a:
                        primary ::=  atom | attributeref | subscription | slicing | call
                    if 'await 等待 的优先级低于[] ，（） ，和。  ，但高于** 操作符 。' in a:
                        a="""在Python中常见的运算符有： +、-、*、/、**/<、>、!=、//、%、&、|、
                            ^、~、>>、<<、<=、>=、==、not、and、or """  
                        a="""操作符列表	              描述
                            yield x, yield from x 	生成器 表达
                            lambda 	表达 匿名函数
                            if -- else 	有条件的表达
                            or 	布尔OR
                            and 	布尔与
                            not x 	布尔NOT
                            in, not in, is, is not, <, <=, >, >=, !=, == 	比较，包括成员资格测试和身份测试
                            | 	按位或
                            ^ 	按位XOR
                            & 	按位与
                            <<, >> 	转变
                            +, - 	加减
                            *, @, /, //, % 	乘法，矩阵乘法，除法，余数
                            +x, -x, ~x 	积极，消极，按位不
                            ** 	幂
                            await x 	等待表达
                            x[index], x[index:index], x(arguments...), x.attribute 	订阅，切片，调用，属性引用
                            (expressions...), [expressions...], {key: value...}, {expressions...} 	绑定或元组显示，列表显示，字典显示，设置显示
                            """      
                    if '“await 等待”表达式的例子' in a:a="""有效的语法示例："""
                        a="""表达列表	                    将被解析为
                            if await fut: pass	              如果（等待 后续）：通过
                            if await fut + 1: pass	        如果（等待  后续）+ 1：通过
                            pair = await fut, 'spam'	     对=（等待），“垃圾邮件”
                            with await fut, open(): pass	（等待  后续），open（）： pass
                            await foo()['spam'].baz()()	await（foo（）['spam']。baz（）（））
                            return await coro()	            返回（等待coro（））
                            res = await coro() ** 2	        res =（等待coro（）） ** 2
                            func(a1=await coro(), a2=0)	      func（a1 =（等待 coro（））， a2 = 0）
                            await foo() + await bar()	           （await foo（）） +（await bar（））
                            -await foo()	-                       （等待 foo（））
                            """ 
                    if '无效的语法示例：' in a:
                        a="""await await coro()
                            await -coro()
                            """ 
                if '异步上下文管理器' in a:       
                    if '异步上下文管理器的一个例子：' in a:
                        class AsyncContextManager:
                            async def __aenter__(self):
                                await log('entering context')
                            async def __aexit__(self, exc_type, exc, tb):
                                await log('exiting context')
                    if '为协程实现适当的数据库事务管理器' in a:
                        a="""管理协同程序："""  
                        async def commit(session, data):
                            ...
                            async with session.transaction():
                                ...
                                await session.update(data)
                                ...      
                if '异步迭代器和“异步”' in a:
                    a="""一个异步迭代能够调用其异步代码 ITER执行，
                        并异步迭代器可以调用异步代码在它的下一个方法。为了支持异步迭代："""
                    a="""
                        1.一个对象必须实现一个 __aiter__方法（或者，如果使用CPython C API定义的话，
                        tp_as_async.am_aiter slot）将返回一个 异步迭代器对象。
                        2.一个异步迭代器对象必须实现__anext__ 方法（或，如果与CPython的C API定义，
                        tp_as_async.am_anext 时隙）返回一个awaitable。
                        3.停止迭代__anext__必须引发StopAsyncIteration 异常。"""
                    if '异步迭代的一个例子：' in a:
                        class AsyncIterable:
                            def __aiter__(self):
                                return self
                            async def __anext__(self):
                                data = await self.fetch_data()
                                if data:
                                    return data
                                else:
                                    raise StopAsyncIteration
                            async def fetch_data(self):
                                ...
                if '用于迭代异步迭代器 for遍历 的新语句：' in a:
                    if '样板 例子' in a:
                        async for TARGET in ITER:
                                BLOCK#  BLOCK Python模块 
                        else:
                            BLOCK2
                        
                    if '这在语义上等同于：' in a:
                        iter = (ITER)
                        iter = type(iter).__aiter__(iter)
                        running = True
                        while running:
                            try:
                                TARGET = await type(iter).__anext__(iter)
                            except StopAsyncIteration:
                                running = False
                            else:
                                BLOCK
                        else:
                            BLOCK2
                    if '以下代码演示了新的异步迭代协议：' in a:
                        class Cursor:
                            def __init__(self):
                                self.buffer = collections.deque()
                            async def _prefetch(self):
                                ...
                            def __aiter__(self):
                                return self
                            async def __anext__(self):
                                if not self.buffer:
                                    self.buffer = await self._prefetch()
                                    if not self.buffer:
                                        raise StopAsyncIteration # raise 提交错误至上一层
                                return self.buffer.popleft()
                    if '那么可以使用Cursor 游标类如下：' in a:
                        if '样板 例' in a:
                            async for row in Cursor():
                                print(row)
                        if '相当于下面的代码：' in a:
                            i = Cursor().__aiter__()
                            while True:
                                try:
                                    row = await i.__anext__()
                                except StopAsyncIteration:
                                    break
                                else:
                                    print(row)
                        if '异常 迭代器没有更多的值 StopIteration' in a:
                            if '下面的例子将其StopIteration封装到一个 RuntimeError' in a:
                                async def a1():
                                    await fut
                                    raise StopIteration('spam')# raise 提交错误至上一层
                                a="""告诉外部代码迭代已经结束的唯一方法是提出StopIteration之外的其他东西。
                                    因此，添加了一个新的内置异常类StopAsyncIteration。
                                    而且，通过PEP 479的语义，在协程中引发的所有StopIteration异常
                                    都被包装在RuntimeError中。"""
        if '协程对象' in a:
            if '与生成器的差异' in a:
                a="""本节仅适用于带有CO_COROUTINE 标志的本地协程，即使用新的异步def语法定义。
                asyncio中基于* generator生成的协程*的行为保持不变。
                已经做了很大的努力来确保协程和发生器被视为不同的概念：
                    1.本地协程对象不实现__iter__和 __next__方法。因此，它们不能迭代或传递给iter（），list（），
                    tuple（）等内建函数。它们也不能用于for..in循环。
                    2.尝试在本地协程对象上使用__iter__或__next__将导致TypeError。
                    3.普通生成器不能从 本地协程生成：这样做会导致TypeError。
                    4.基于生成器的协程（asyncio代码必须用@ asyncio.coroutine修饰）可以从 本地协程对象生成。
                    inspect.isgenerator（）和inspect.isgeneratorfunction（）为本地协程对象和本地协程函数 返回False。"""
            if '协程对象方法' in a:
                a="""协程是基于内部的生成器，因此它们共享实现。与生成器对象类似，
                协程有 throw（），send（）和close（）方法。 StopIteration和 GeneratorExit在协程中扮演相同的角色
                （尽管 协程默认启用了PEP 479）。有关详细信息，请参阅PEP 342，PEP 380和Python文档[11]。
                    用于协程的throw（），send（）方法用于推送值并将错误引发到类似Future的对象中。"""
        if '词汇表' in a:a="""
            本机协同功能
                协程函数用async def声明。它使用 await和返回值 return value ; 有关详细信息，请参阅新协程声明语法。
            本地协程
                从本地协程函数返回。有关 详细信息，请参阅等待表达式。
            基于生成器的协程功能
                基于生成器语法的协程。最常见的例子是用@ asyncio.coroutine装饰的函数。
            基于生成器的协程
                从基于生成器的协程函数返回。
            协同程序
                无论是原生协程或发电的协同程序。
            协程对象
                无论是原生协程对象或发电的协程 对象。
            未来的对象（后续）
                带有__await__方法的对象或带有tp_as_async-> am_await函数的C对象 返回一个迭代器。可以在协程中等待表达式消耗。
                等待Future类对象的协程暂停，直到Future类对象的__await__完成，并返回结果。有关详细信息，请参阅 等待表达式。
            Awaitable
                甲未来状物体或一个协程对象。有关详细信息，请参阅等待表达式。
            异步上下文管理器
                异步上下文管理器有__aenter__和__aexit__ 方法，可以和async一起使用。有关详细信息，请参阅异步上下文管理器和“与...异步”。
            异步迭代
                带有__aiter__方法的对象，它必须返回一个 异步迭代器对象。可以与async一起使用。有关详细信息，请参阅异步迭代器和“async for”。
            异步迭代器
                异步迭代器有一个__anext__方法。有关详细信息，请参阅 异步迭代器和“async for”。 """
        if '高级更改和新协议列表' in a:
            if '定义协程的新语法：async def和new await 关键字。' in a:
            if '异步上下文管理器的新语法：async with。' in a:
                a="""和__aenter__和__aexit__方法相关的协议。"""
            if '异步迭代的新语法：async for' in a:
                a="""和__aiter__，__aexit__和新的内置异常StopAsyncIteration相关的协议。
                新tp_as_async.am_aiter 和tp_as_async.am_anext插槽PyTypeObject。"""
            if '新的AST节点：AsyncFunctionDef，AsyncFor，AsyncWith， Await. 等待。' in a:
            if '新功能：（回调）' in a:
                a="""sys.set_coroutine_wrapper（callback 回调）， sys.get_coroutine_wrapper（） ，
                    types.coroutine（gen 根）， inspect.iscoroutinefunction（FUNC） ，inspect.iscoroutine（OBJ） ， 
                    inspect.isawaitable（OBJ） ，inspect.getcoroutinestate（coro 科洛），
                    并检查.getcoroutinelocals（coro 科罗）。"""
            if '代码对象的新CO_COROUTINE和CO_ITERABLE_COROUTINE位标志' in a:
            if '新的ABCs：' in a:
                a="""collections.abc.Awaitable， collections.abc.Coroutine，
                collections.abc.AsyncIterable和 collections.abc.AsyncIterator。"""
            if 'C API更改：新的PyCoro_Type' in a:
                a="""新的PyCoro_Type（作为types.CoroutineType公开给Python ）和PyCoroObject。 
                    PyCoro_CheckExact（* o）测试o是否是本地协程。"""
 
        if '所有概念示例' in a:
            import asyncio
            async def echo_server():
                print('Serving on localhost:8000')
                await asyncio.start_server(handle_connection,
                                        'localhost', 8000)#start_server接受一个简单的回调函数
            async def handle_connection(reader, writer):
                print('New connection...')
                while True:
                    data = await reader.read(8192)
                    if not data:
                        break
                    print('Sending {:.10}... back'.format(repr(data)))
                    writer.write(data)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(echo_server())
            try:
                loop.run_forever()
            finally:
                loop.close()
     
       
   
if '异步 网络器' in a:
    if '1.1. 基本请求用法' in a:
        if '样例' in a:
            async with aiohttp.get('https://github.com') as r:
            await r.text()
        if 'aiohttp会自动解码来自服务器的内容，其中r.text(), 可以在括号中指定解码方式，编码方式，例如' in a:
            await resp.text(encoding='windows-1251')
        if '或者也可以选择不编码，适合读取图像等，是无法编码的' in a:
            await resp.read()
       
    if '2.发起一个session请求' in a:
        a="""首先是导入aiohttp模块： import aiohttp"""
        if '然后我们试着获取一个web源码' in a:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.github.com/events') as resp:
                    print(resp.status)
                    print(await resp.text())
        if '上面的代码中' in a:
            a="""上面的代码中，我们创建了一个 ClientSession 对象命名为session，
            然后通过session的get方法得到一个 ClientResponse 对象，
            命名为resp，get方法中传入了一个必须的参数url，就是要获得源码的http url。
            至此便通过协程完成了一个异步IO的get请求。
                有get请求当然有post请求，并且post请求也是一个协程："""
            session.post('http://httpbin.org/post', data=b'data')
            a="""用法和get是一样的，区别是post需要一个额外的参数data，即是需要post的数据。
                除了get和post请求外，其他http的操作方法也是一样的："""
                session.put('http://httpbin.org/put', data=b'data')
                session.delete('http://httpbin.org/delete')
                session.head('http://httpbin.org/get')
                session.options('http://httpbin.org/get')
                session.patch('http://httpbin.org/patch', data=b'data')
            a="""小记：
                不要为每次的连接都创建一次session,一般情况下只需要创建一个session，
                然后使用这个session执行所有的请求。
                每个session对象，内部包含了一个连接池，并且将会保持连接和连接复用（默认开启）
                可以加快整体的性能。"""
    if '3.在URL中传递"如 页数 等参数' in a:a="""如 页数 """
        if '经常需要通过 get 在url中传递一些参数' in a:
            a="""我们经常需要通过 get 在url中传递一些参数，参数将会作为url问号后面的一部分发给服务器。
            在aiohttp的请求中，允许以dict的形式来表示问号后的参数。
            举个例子，如果你想传递 key1=value1   key2=value2 到 httpbin.org/get 
            你可以使用下面的代码："""
        if '样例' in a:
            params = {'key1': 'value1', 'key2': 'value2'}
            async with session.get('http://httpbin.org/get',
                                params=params) as resp:
                 assert resp.url == 'http://httpbin.org/get?key2=value2&key1=value1'
        if '除了上面两种，' in a:
            a="""我们也可以直接通过传递字符串作为参数来传递，但是需要注意，
            通过字符串传递的特殊字符不会被编码："""
            async with session.get('http://httpbin.org/get',
                       params='key=value+1') as r:
                assert r.url == 'http://httpbin.org/get?key=value+1'
    if '4.响应的内容' in a:
        a="""还是以GitHub的公共Time-line页面为例，我们可以获得页面响应的内容："""
        async with session.get('https://api.github.com/events') as resp:
            print(await resp.text())
        a="""运行之后，会打印出类似于如下的内容： 
          '[{"created_at":"2015-06-12T14:06:22Z","public":true,"actor":{..."""
        a="""resp的text方法，会自动将服务器端返回的内容进行解码--decode，
          当然我们也可以自定义编码方式："""
          await resp.text(encoding='gb2312')
        a="""除了text方法可以返回解码后的内容外，我们也可以得到类型是字节的内容： """
          print(await resp.read())
        a="""运行的结果是：
            [{"created_at":"2015-06-12T14:06:22Z","public":true,"actor":{..."""
        a="""gzip和deflate转换编码已经为你自动解码。"""
        a="""小记：
            text(),read()方法是把整个响应体读入内存，
            如果你是获取大量的数据，请考虑使用”字节流“（streaming response）"""
    if '5.特殊响应内容：json' in a:
        a="""如果我们获取的页面的响应内容是json，aiohttp内置了更好的方法来处理json:"""
            async with session.get('https://api.github.com/events') as resp:
                print(await resp.json())
        a="""如果因为某种原因而导致resp.json()解析json失败，例如返回不是json字符串等等，
            那么resp.json()将抛出一个错误，也可以给json()方法指定一个解码方式： """
            print(await resp.json(encoding='gb2312'))
        a="""或者传递一个函数进去："""
            print(await resp.json( lambda(x:x.replace('a','b')) ))
   
    if '6.以字节流的方式读取响应内容' in a:
        a="""虽然json(),text(),read()很方便的能把响应的数据读入到内存，
            但是我们仍然应该谨慎的使用它们，因为它们是把整个的响应体全部读入了内存。
            即使你只是想下载几个字节大小的文件，
            但这些方法却将在内存中加载所有的数据。所以我们可以通过控制字节数来控制读入内存的响应内容："""
            async with session.get('https://api.github.com/events') as resp:
                await resp.content.read(10) #读取前10个字节
        a="""一般地，我们应该使用以下的模式来把读取的字节流保存到文件中： """
            with open(filename, 'wb') as fd:
                while True:
                    chunk = await resp.content.read(chunk_size)
                    if not chunk:
                        break
                    fd.write(chunk)
    if '保存内容至文件' in a:c="""把图像内容以二进制字节流保存到文件中"""
          with open(filename, 'wb') as fd:
                while True:
                    chunk = await resp.content.read(chunk_size内容)
                    if not chunk:
                        break
                    fd.write(chunk)
       
    if '7.自定义请求头' in a:
        a="""如果你想添加请求头，可以像get添加参数那样以dict的形式，作为get或者post的参数进行请求："""
            import json
            url = 'https://api.github.com/some/endpoint'
            payload = {'some': 'data'}
            headers = {'content-type': 'application/json'}
            await session.post(url,
                            data=json.dumps(payload),
                            headers=headers)
  
    if '8.自定义Cookie' in a:
        a="""给服务器发送cookie，可以通过给 ClientSession 传递一个cookie参数："""
            url = 'http://httpbin.org/cookies'
            cookies = {'cookies_are': 'working'}
            async with ClientSession(cookies=cookies) as session:
                async with session.get(url) as resp:
                    assert await resp.json() == {
                    "cookies": {"cookies_are": "working"}}
        a="""可直接访问链接 “httpbin.org/cookies”查看当前cookie，访问session中的cookie请见第10节。"""
        
       
    if '9.post数据的几种方式' in a:
        if '（1）模拟表单post数据' in a:
            payload = {'key1': 'value1', 'key2': 'value2'}
            async with session.post('http://httpbin.org/post',
                                    data=payload) as resp:
                print(await resp.text())
            a="""注意：data=dict的方式post的数据将被转码，和form提交数据是一样的作用，
            如果你不想被转码，可以直接以字符串的形式 data=str 提交，这样就不会被转码。"""
        if '（2）post json ' in a:
            a="""其实json.dumps(payload)返回的也是一个字符串，
                只不过这个字符串可以被识别为json格式 """
            import json
            url = 'https://api.github.com/some/endpoint'
            payload = {'some': 'data'}
            async with session.post(url, data=json.dumps(payload)) as resp:
                ...
      
        if '（3）post 小文件' in a:
            url = 'http://httpbin.org/post'
            files = {'file': open('report.xls', 'rb')}
            await session.post(url, data=files)
            a="""可以设置好文件名和content-type: """
                url = 'http://httpbin.org/post'
                data = FormData()
                data.add_field('file',
                    open('report.xls', 'rb'),
                    filename='report.xls',
                    content_type='application/vnd.ms-excel')
                    await session.post(url, data=data)
            a="""如果将文件对象设置为数据参数，aiohttp将自动以字节流的形式发送给服务器。 """
      
        if '（4）post 大文件' in a:
            a="""aiohttp支持多种类型的文件以流媒体的形式上传 ，
            所以我们可以在文件未读入内存的情况下发送大文件。"""
                @aiohttp.streamer
                def file_sender(writer, file_name=None):
                    with open(file_name, 'rb') as f:
                        chunk = f.read(2**16)
                        while chunk:
                            yield from writer.write(chunk)
                            chunk = f.read(2**16)
                # Then you can use `file_sender` as a data provider:
                async with session.post('http://httpbin.org/post',
                                        data=file_sender(file_name='huge_file')) as resp:
                    print(await resp.text())
            a="""同时我们可以从一个url获取文件后，直接post给另一个url，并计算hash值: """
                async def feed_stream(resp, stream):
                    h = hashlib.sha256()
                    while True:
                        chunk = await resp.content.readany()
                        if not chunk:
                            break
                        h.update(chunk)
                        stream.feed_data(chunk)
                    return h.hexdigest()
                resp = session.get('http://httpbin.org/post')
                stream = StreamReader()
                loop.create_task(session.post('http://httpbin.org/post', data=stream))
                file_hash = await feed_stream(resp, stream)
            a="""因为响应内容类型是StreamReader，所以可以把get和post连接起来，同时进行post和get： """
                r = await session.get('http://python.org')
                await session.post('http://httpbin.org/post',
                                data=r.content)
       
        if '（5）post预压缩数据 ' in a:
            a="""在通过aiohttp发送前就已经压缩的数据, 
            调用压缩函数的函数名（通常是deflate 或 zlib）作为content-encoding的值："""
                async def my_coroutine(session, headers, my_data):
                    data = zlib.compress(my_data)
                    headers = {'Content-Encoding': 'deflate'}
                    async with session.post('http://httpbin.org/post',
                                            data=data,
                                            headers=headers)
                                            pass
    
    if '10.keep-alive, 连接池，共享cookie' in a:
        a="""ClientSession 用于在多个连接之间共享cookie："""
            async with aiohttp.ClientSession() as session:
                await session.get(
                    'http://httpbin.org/cookies/set?my_cookie=my_value')
                filtered = session.cookie_jar.filter_cookies('http://httpbin.org')
                assert filtered['my_cookie'].value == 'my_value'
                async with session.get('http://httpbin.org/cookies') as r:
                    json_body = await r.json()
                    assert json_body['cookies']['my_cookie'] == 'my_value'
        a="""也可以为所有的连接设置共同的请求头： """
            async with aiohttp.ClientSession(headers={"Authorization": "Basic bG9naW46cGFzcw=="}) as session:
            async with session.get("http://httpbin.org/headers") as r:
                json_body = await r.json()
                assert json_body['headers']['Authorization'] == \
                    'Basic bG9naW46cGFzcw=='
        a="""ClientSession 还支持 keep-alive连接和连接池(connection pooling)"""
    if '11.cookie安全性' in a:
        a="""默认ClientSession使用的是严格模式的 aiohttp.CookieJar. RFC 2109，
        明确的禁止接受url和ip地址产生的cookie，
        只能接受 DNS 解析IP产生的cookie。可以通过设置aiohttp.CookieJar 的 
        unsafe=True 来配置："""
            jar = aiohttp.CookieJar(unsafe=True)
            session = aiohttp.ClientSession(cookie_jar=jar)
    if '12.控制同时连接的数量（连接池）' in a:
        a="""也可以理解为同时请求的数量，为了限制同时打开的连接数量，
            我们可以将限制参数传递给连接器："""
            conn = aiohttp.TCPConnector(limit=30)#同时最大进行连接的连接数为30，默认是100，limit=0的时候是无限制
        a="""限制同时打开限制同时打开连接到同一端点的数量（(host, port, is_ssl) 三的倍数），
        可以通过设置 limit_per_host 参数："""
            conn = aiohttp.TCPConnector(limit_per_host=30)#默认是0
    if '13.自定义域名解析' in a:
        a="""我们可以指定域名服务器的 IP 对我们提供的get或post的url进行解析："""
            from aiohttp.resolver import AsyncResolver
            resolver = AsyncResolver(nameservers=["8.8.8.8", "8.8.4.4"])
            conn = aiohttp.TCPConnector(resolver=resolver)
    if '14.设置代理' in a:
        a="""aiohttp支持使用代理来访问网页："""
            async with aiohttp.ClientSession() as session:
            async with session.get("http://python.org",
                                proxy="http://some.proxy.com") as resp:
                print(resp.status)
        a="""当然也支持需要授权的页面："""
            async with aiohttp.ClientSession() as session:
            proxy_auth = aiohttp.BasicAuth('user', 'pass')
            async with session.get("http://python.org",
                                proxy="http://some.proxy.com",
                                proxy_auth=proxy_auth) as resp:
                print(resp.status)
        a="""或者通过这种方式来验证授权："""
            session.get("http://python.org",
            proxy="http://user:pass@some.proxy.com")
    if '15.响应状态码 response status code' in a:
        a="""可以通过 resp.status来检查状态码是不是200："""
            async with session.get('http://httpbin.org/get') as resp:
            assert resp.status == 200 #assert 断言
    if '16.响应头' in a:
        a="""我们可以直接使用　resp.headers 来查看响应头，得到的值类型是一个dict："""
            >>> resp.headers
            {'ACCESS-CONTROL-ALLOW-ORIGIN': '*',
            'CONTENT-TYPE': 'application/json',
            'DATE': 'Tue, 15 Jul 2014 16:49:51 GMT',
            'SERVER': 'gunicorn/18.0',
            'CONTENT-LENGTH': '331',
            'CONNECTION': 'keep-alive'}
        a="""或者我们可以查看原生的响应头： """
            >>> resp.raw_headers
            ((b'SERVER', b'nginx'),
            (b'DATE', b'Sat, 09 Jan 2016 20:28:40 GMT'),
            (b'CONTENT-TYPE', b'text/html; charset=utf-8'),
            (b'CONTENT-LENGTH', b'12150'),
            (b'CONNECTION', b'keep-alive'))
    if '17.查看cookie' in a:
        url = 'http://example.com/some/cookie/setting/url'
        async with session.get(url) as resp:
            print(resp.cookies)
    if '18.重定向的响应头' in a:
        a="""如果一个请求被重定向了，我们依然可以查看被重定向之前的响应头信息："""
            >>> resp = await session.get('http://example.com/some/redirect/')
            >>> resp
            <ClientResponse(http://example.com/some/other/url/) [200]>
            >>> resp.history
            (<ClientResponse(http://example.com/some/redirect/) [301]>,)
    if '19.超时处理' in a:
                a="""默认的IO操作都有5分钟的响应时间 我们可以通过 timeout 进行重写："""
            async with session.get('https://github.com', timeout=60) as r:
                      ...
        a="""如果 timeout=None 或者 timeout=0 将不进行超时检查，也就是不限时长。 """
    if '超时异常处理' in a:c=""""""
        捕捉就好了...基本上碰到的有这些异常
        asyncio.TimeoutError
        aiohttp.client_exceptions.ServerDisconnectedError
        aiohttp.client_exceptions.InvalidURL
        aiohttp.client_exceptions.ClientConnectorError
    if '访问多个链接' in a:c=""""""
        if '同步方式如下：' in a:c=""""""
            for url in urls:     
                print(requests.get(url).text)
        if '不过异步方式却没有这么容易。' in a:
            c="""需要将之包装在asyncio的 Future后续 对象中，然后将 Future后续 对象列表作为任务传递给事件循环。"""
                loop = asyncio.get_event_loop()
                tasks = []  #设置任务为一个列表
                url = "http://localhost:8080/{}" #初始网址
                
                for i in range(5): #遍历页数
                    #用format替换初始网址产生页数网址，将要代入hello模具，从而包装成一个任务
                    task = asyncio.ensure_future(hello(url.format(i))) 
                    tasks.append(task) #每个任务都加入列表

                loop.run_until_complete(asyncio.wait(tasks)) 

        if '搜集所有的 Future后续 对象，然后等待他们返回' in a:
            c="""asyncio.gather()返回所有的 Future后续 对象，将之存储在一个列表当中，最后再打印出来。"""
                #!/usr/local/bin/python3.5 
                import asyncio 
                from aiohttp import ClientSession 

                async def fetch(url):      
                async with ClientSession() as session:           
                    async with session.get(url) as response:             
                        return await response.read()             
                        
                async def run(loop,  r):     
                url = "http://localhost:8080/{}"         
                tasks = []         
                for i in range(r):             
                    task = asyncio.ensure_future(fetch(url.format(i)))                 
                    tasks.append(task) 

                #asyncio.gather()返回所有的 Future后续 对象        
                responses = await asyncio.gather(*tasks)         
                # you now have all response bodies in this variable         
                print(responses)     
                    
                def print_responses(result):       
                    print(result)     
                    
                loop = asyncio.get_event_loop() 
                future = asyncio.ensure_future(run(loop, 4)) 
                loop.run_until_complete(future)
        if '经验：任何时候，你在等待什么的时候，记得使用await。' in a:c=""""""
            if '想获取网页内容，却返回了一个生成器' in a:
                c="""*（返回网页内容）response.read()是一个异步操作，这意味着它不会立即返回结果，仅仅返回生成器。
                这些生成器需要被调用跟运行，但是这并不是默认行为。
                在Python34中加入的yield from以及Python35中加入的await便是为此而生。
                它们将迭代这些生成器。以上代码只需要在（返回网页内容）response.read()前加上await关键字即可修复。如下："""
                    # async operation must be preceded by await 
                    # # WARNING! BROKEN CODE DO NOT COPY PASTE 
                    async def fetch(url):      
                        async with ClientSession() as session:           
                            async with session.get(url) as response:            
                                return await response.read() 
                                # 只能返回生成器的错误: return response.read()
            if '查看本地日志，你会发现没有任何请求到达服务器，' in a:
                c="""实际上没有任何请求发生。打印信息首先打印<_Gathering pending>对象，
                然后警告等待的任务被销毁。又一次的，你忘记了await。"""
                    # WARNING! BROKEN CODE DO NOT COPY PASTE 
                    async def run(loop,  r):       
                    url = "http://localhost:8080/{}"         
                    tasks = []         
                    for i in range(r):             
                        task = asyncio.ensure_future(fetch(url.format(i)))                 
                        tasks.append(task) 
                        
                        responses = await asyncio.gather(*tasks)        
                        # 只能返回生成器的错误: responses = asyncio.gather(*tasks)         
                        
                        print(responses)
            if '加入一些同步机制，限制并发数量。：' in a:c="""在asyncio.Semaphore()中加入最大任务限制为1000."""
                c="""open files太多了，可能代表着open sockets太多。为什么叫文件？Sockets（套接字）仅仅是文件描述符，
                操作系统有数量的限制。多少才叫太多呢？我查看Python源码，然后发现这个值为1024.怎么样绕过这个问题？
                一个粗暴的办法是增加这个数值，但是听起来并不高明。更好的办法是，加入一些同步机制，
                限制并发数量。于是我在asyncio.Semaphore()中加入最大任务限制为1000."""
                c="""又一个异常的发生原因是操作系统的可用端口耗尽。之前限制了并发连接数最大为1k，
                可能有些sockets仍然处在closing状态，系统内核无法使用才导致这个问题。"""
                # modified fetch function with semaphore 
                import random 
                import asyncio 
                from aiohttp import ClientSession 

                async def fetch(url):      
                async with ClientSession() as session:         
                    async with session.get(url) as response:                     
                    　delay = response.headers.get("DELAY")                     
                    　date = response.headers.get("DATE")                     
                    　print("{}:{} with delay {}".format(date, response.url, delay))                     
                    　return await response.read() 
                    　
                async def bound_fetch(sem, url):     
                    # getter function with semaphore         
                    async with sem:                 
                    　await fetch(url) 
                    async def run(loop,  r):         
                    　url = "http://localhost:8080/{}"         
                    　tasks = []         
                    　# create instance of Semaphore 
                    # 
                    # 
                    # 加入一些同步机制，限制并发数量
                    # 
                    #         
                    　sem = asyncio.Semaphore(1000)         
                    　for i in range(r):             
                    　    # pass Semaphore to every GET request                 
                    　    task = asyncio.ensure_future(bound_fetch(sem, url.format(i)))                 
                    　    tasks.append(task)         
                    　    responses = asyncio.gather(*tasks)         
                    　    
                await responses number = 10000 
                loop = asyncio.get_event_loop() 
                future = asyncio.ensure_future(run(loop, number)) 
                loop.run_until_complete(future)
    c="""开始就设置asyncio.Semaphore()限制为4."""

                import asyncio
                import aiohttp
                import requests
                from bs4 import BeautifulSoup

                sem = asyncio.Semaphore(4)   #设置Semaphore为4，说明在抓取时最多并发发出4个请求 
                @asyncio.coroutine
                def get_urls_in_pages(from_page_num,to_page_num):
                    url = r'http://college.koolearn.com/kaoyan/s/fs-0-0-0-0-0-0/?p='
                    urls = []
                    for i in range(from_page_num,to_page_num+1):
                        urls.append(url + str(i))
                    for url in urls:
                        with(yield from sem):
                            response = yield from aiohttp.request('GET',url) #该语句功能是发出http请求，并在此处等待请求的结果
                        html = yield from response.read_and_close()
                        bs = BeautifulSoup(html.decode('utf-8'))
                    #以下的操作是抓取数据
                def main_test():
                    page_ranges_lst = [
                        (1,10),
                        (11,20),
                        (21,30),
                        (31,40),
                    ]

                    #下面三行语句代码完成的功能就是启动事件循环机制，生成待运行的诸协程，然后调度运行
                    loop = asyncio.get_event_loop()
                    for page_range in page_ranges_lst])
                        f = asyncio.wait([get_urls_in_pages(page_range[0],page_range[1])
                        loop.run_until_complete(f)

                if __name__ == '__main__':
                    mian_test()




if '异步运行的的样例' in a:
    loop = asyncio.get_event_loop()
    tasks=[模具O测试()]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()
def 异步运行的的样例二():
    import asyncio
    from aiohttp import ClientSession
    import requests

    async def 分支异步打开网页(网址):  # 定义（def）一个分支异步模具（async）
        async with ClientSession() as 会话:  # aiohttp 的ClientSession 库
            async with 会话.get(网址) as 返回网页内容:
                # 等待返回网页内容后，再return 返回模具的数据
                return await 返回网页内容.read()  # read()为内容二进制   text() 为文本


    async def 模具_分支异步打开网页二(self): #定义(def)一个分支异步模具(async)
        async with ClientSession() as 会话:  #aiohttp 的ClientSession 库
            async with 会话.get(self.网址) as 返回网页内容:
                #等待返回网页内容后,再return 返回模具的数据
                返回网页内容=await 返回网页内容.text()
                self.网页内容列表.append(返回网页内容)


    网址 = "http://localhost:8080/{}"  # {}初始网址
    sem = asyncio.Semaphore(4)  # 设置Semaphore为4，说明在抓取时最多并发发出4个请求
    # 下面三行语句代码完成的功能就是启动事件循环机制，生成待运行的诸协程，然后调度运行
    loop = asyncio.get_event_loop()
    任务组列表 = []  # 设置任务为一个列表

    for 数字遍历 in range(5):  # 遍历页数
        # 用format替换初始网址产生页数网址，将要代入hello模具，从而包装成一个任务
        任务 = asyncio.ensure_future(分支异步打开网页(网址.format(数字遍历)))
        任务组列表.append(任务)  # 每个任务都加入列表

    loop.run_until_complete(asyncio.wait(任务组列表))
if '异步 数据库aiomysql' in a:
    if '查询与读取' in a:
        #导入的模块
        import asyncio
        import aiomysql
        # 定义数据库操作为协程
        async def test_example_executemany():
            #连接数据库
            conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                            user='root', password='',
                                            db='sql库')
            #获取游标
            cur = await conn.cursor()
            # 定义执行SQL语句 为协程
            async with conn.cursor() as cur:
                #执行SQL查询语句，查询数据库，之后读取
                await cur.execute("SELECT * FROM music_style;")
                #数据库读取
                result = await cur.fetchall()
                
                print(result)
            # 关闭数据库连接
            conn.close()
        # 执行数据库操作
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_example_executemany())
    if '执行，插入、更改、删除' in a: 
        
        #导入的模块
        import asyncio
        import aiomysql
        # 定义数据库操作为协程
        async def test_example_executemany():
            #连接数据库
            conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                            user='root', password='',
                                            db='sql库')
            #获取游标
            cur = await conn.cursor()
            # 定义执行SQL语句 为协程
            async with conn.cursor() as cur:
                
                #举例data
                #data = [(4, 'gothic metal'), (5, 'doom metal'), (6, 'post metal')]
                #执行SQL插入语句，
                await cur.execute(
                    "INSERT INTO music_style (id, name)"
                    "values (25,'data')")
                #提交至数据库执行
                await conn.commit()
               
            # 关闭数据库连接
            conn.close()
        # 执行数据库操作
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_example_executemany())