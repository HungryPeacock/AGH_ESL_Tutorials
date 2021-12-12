from myhdl import intbv, Signal, ConcatSignal

print('List of signals:')
request_list = [Signal(bool(1)) for i in range(5)]
print(request_list, '\n')

print('Connect list of signals to bit vector:')
request_vector = ConcatSignal(*reversed(request_list))
print(request_vector, '\n')

print('Inverse problem')
grant_vector = Signal(intbv(0)[5:])
print(grant_vector)
grant_list = [grant_vector(i) for i in range(5)]
print(grant_list)
