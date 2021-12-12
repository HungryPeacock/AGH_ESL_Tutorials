from myhdl import intbv, modbv, Signal

modified_int = intbv(-4, min=-4, max=16)
# alternative - bit width, only unsigned
# modified_int = intbv(6)[5:0]

print(f'Hex: {modified_int}\n'
      f'Binary: {bin(modified_int)}\n'
      f'Length: {len(modified_int)}\n'
      f'Minimum: {modified_int.min}\n'
      f'Maximum: {modified_int.max}\n')

print('Convert to unsigned')
modified_int = modified_int.unsigned()
print(f'Binary: {bin(modified_int)}\n')

print('Change third less significant bit to 0')
modified_int[2] = 0
print(f'Binary: {bin(modified_int)}')

# modbv -> wraparound
# count = Signal(modbv(0, min=0, max=2**2))
