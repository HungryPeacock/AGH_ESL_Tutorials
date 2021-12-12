from myhdl import block, Signal

from ClkDriver import ClkDriver
from Hello import Hello


@block
def Greetings(to: str = 'Student'):

    clk = Signal(0)

    clk_driver = ClkDriver(clk=clk, period=10)
    hello = Hello(clk=clk, to=to)

    return clk_driver, hello


inst = Greetings()
inst.run_sim(50)
