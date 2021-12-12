from myhdl import block, always_seq, always


@block
def inc(count, enable, clock, reset):
    """ Incrementer with enable.

    count -- output
    enable -- control input, increment when 1
    clock -- clock input
    reset -- asynchronous reset input
    """

    # always with reset functionality
    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            count.next = count + 1

    #alternative
    @always(clock.posedge, reset.negedge)
    def seq_logic():
        if not reset:
            count.next = 0
        else:
            if enable:
                count.next = count + 1

    # return seq
    return seq_logic
