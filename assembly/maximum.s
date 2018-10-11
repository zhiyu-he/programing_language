.section .data

data_items:
.long 3, 67, 34, 222, 45, 75, 54, 34, 44, 33, 22, 11, 66, 0
.section .text

.global _start

_start:
movl $0, %edi   # edi maybe i means idx, edi hold 0 now. 立即寻址
movl data_items(,%edi, 4), %eax # 变址寻址=基准地址+变址寄存器+比例因子

movl %eax, %ebx #间接寻址, 通过寄存器指定的地址加载值

start_loop:
cmpl $0, %eax
je loop_exit
incl %edi   # edi increase 1.
movl data_items(, %edi, 4), %eax    #索引寻址
cmpl %ebx, %eax
jle start_loop # jump less or equal

movl %eax, %ebx

jmp start_loop

loop_exit:
movl $1, %eax   # set system signal to eax
int $0x80

