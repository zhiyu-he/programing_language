as xx.s -o xx.o
ld xx.o -o xx

./xx


as --32 -o powers.o powers.s
ld -m elf_i386 -dynamic-linker /lib/ld-linux.so.2  -o powers -L/lib -lc powers.o

