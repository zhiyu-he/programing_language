.section .data

.section .text

.global _start
.global factorial

_start:
 pushl $4
 call factorial
 addl $4, %esp      # 弹出入栈的参数
 movl %eax, %ebx    # 阶乘将答案返回到%eax, 我们希望它在%ebx.
 movl $1, %eax
 int $0x80


 .type factorial,@function

factorial:
 pushl %ebp
 movl %esp, %ebp
 movl 8(%ebp), %eax # 此时栈的结构是[参数1, 返回值, 旧的%ebp], 当前ebp指向旧的ebp
 cmpl $1, %eax
 je end_factorial
 decl %eax
 pushl %eax
 call factorial
 movl 8(%ebp), %ebx
 imull %ebx, %eax

end_factorial:
 movl %ebp, %esp
 popl %ebp
 ret

