.code32
.section .data

.section .text

.global _start

_start:
 pushl $3
 pushl $2
 call power     # 1. 将下一条指令的地址即返回地址压入栈中; 2. 修改%eip指向函数启始初
 addl $8, %esp  # 将栈指针向后移动
 pushl %eax


 pushl $2
 pushl $5
 call power
 addl $8, %esp

 popl %ebx

 addl %eax, %ebx

 movl $1, %eax
 int $0x80


.type power,@function

# 函数执行完毕
# 1. 返回值存储到%eax
# 2. 将栈恢复到调用函数时的状态
#    movl %ebp, %esp
#    popl %ebp 此时esp指向返回地址
#    ret
# 3. 将控制权交还给调用它的程序. 通过RET实现, 将栈顶的值弹出并设置%eip
 power:
  pushl %ebp        # 保留旧基地址指针
  movl %esp, %ebp # 将基地址设为栈指针
  subl $4, %esp # 为本地存储保留空间
  movl 8(%ebp), %ebx
  movl 12(%ebp), %ecx

  movl %ebx, -4(%ebp)   # 存储当前结果

power_loop_start:
 cmpl $1, %ecx
 je end_power
 movl -4(%ebp), %eax
 imull %ebx, %eax
 movl %eax, -4(%ebp)

 decl %ecx
 jmp power_loop_start

end_power:
 movl -4(%ebp), %eax
 movl %ebp, %esp
 popl %ebp
 ret

