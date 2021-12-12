from myhdl import block, always, now


@block
def Hello(clk, to):

    @always(clk.posedge)
    def say_hello():
        print("%s Hello %s" % (now(), to))

    @always(clk.posedge)
    def say_hello_polish():
        print(f'{now()} Cześć {to}')

    return say_hello, say_hello_polish
