import random
from myhdl import block, instance, Signal, intbv, delay
from multiplexer import mux

random.seed(2)
randrange = random.randrange


@block
def test_mux():

    z, a, b, sel = [Signal(intbv(0)) for _ in range(4)]
    mux_1 = mux(z, a, b, sel)

    @instance
    def stimulus():
        print("z a b sel")
        for i in range(12):
            a.next, b.next, sel.next = randrange(8), randrange(8), randrange(2)
            yield delay(10)
            print("%s %s %s %s" % (z, a, b, sel))

    return mux_1, stimulus


tb = test_mux()
tb.run_sim()
