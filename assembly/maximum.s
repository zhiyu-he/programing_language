.section .data

data_items:
    .long 3, 67, 34, 222, 45, 75, 54, 34, 44, 33, 22, 11, 66, 0
    .section .text
    
    .global _start

_start:
    movl $0, %edi   # edi maybe i means idx, edi hold 0 now.
    movl data_items(,%edi, 4), %eax
    movl %eax, %ebx

start_loop:
    cmpl $0, %eax
    je loop_exit
    incl %edi   # edi increase 1.
    movl data_items(, %edi, 4), %eax
    cmpl %ebx, %eax
    jle start_loop # jump less or equal

    movl %eax, %ebx

    jmp start_loop

loop_exit:
    movl $1, %eax   # set system signal to eax
    int $0x80

