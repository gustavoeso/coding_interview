def swap_odd_even_bits(x: int) -> int:
    mascara_impar = 0xAAAAAAAA
    mascara_par = 0x55555555

    shift_bits_impar = (x & mascara_impar) >> 1
    shift_bits_par = (x & mascara_par) << 1

    return shift_bits_impar | shift_bits_par