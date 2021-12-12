from myhdl import block, delay, always, now, Signal


@block
def HelloWorld():

    clk = Signal(0)

    @always(delay(10))
    def drive_clk():
        clk.next = not clk

    @always(clk.negedge)
    def say_hello_rise():
        print("%s Hello World!" % now())

    @always(clk.posedge)
    def say_hello_fall():
        print("%s Hello World!" % now())

    return drive_clk, say_hello_rise


inst = HelloWorld()
inst.run_sim(50)
