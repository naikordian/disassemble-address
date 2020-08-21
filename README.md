# disassemble-address
https://microcorruption.com/assembler

```asm
;test.txt
0b12           push r11
0412           push r4
0441           mov  sp, r4
2452           add  #0x4, r4
3150 e0ff      add  #0xffe0, sp
3b40 2045      mov  #0x4520, r11
073c           jmp  $+0x10
1b53           inc  r11
8f11           sxt  r15
0f12           push r15
0312           push #0x0
b012 6424      call #0x2464
```
./asm_addr.py test.txt 1000
```asm
1000:  0b12           push r11
1002:  0412           push r4
1004:  0441           mov  sp, r4
1006:  2452           add  #0x4, r4
1008:  3150 e0ff      add  #0xffe0, sp
100c:  3b40 2045      mov  #0x4520, r11
1010:  073c           jmp  $+0x10
1012:  1b53           inc  r11
1014:  8f11           sxt  r15
1016:  0f12           push r15
1018:  0312           push #0x0
101a:  b012 6424      call #0x2464
```
