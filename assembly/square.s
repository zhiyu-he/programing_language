.section .data
.section .text

.global _start

_start:
 pushl $4
 call square
 movl %eax, %ebx
 movl $1, %eax
 int $0x80

 .type square, @function

square:
 pushl %ebp         # 旧的ebp入栈
 movl %esp, %ebp    # 将esp指向当前的ebp

 movl 8(%ebp), %eax
 imul 8(%ebp), %eax
 jmp end_square

end_square:
 movl %ebp, %esp
 popl %ebp
 ret
