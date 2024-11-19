//Command used to compile: gcc -O0 -g -o, then objdump -d
//Decompilation is incredibly close to the original code, check_password is 
//mostly the same and main method has some bigger differences in the assembly representation.



00000000000011c9 <check_password>:
    11c9:       f3 0f 1e fa             endbr64 
    11cd:       55                      push   %rbp
    11ce:       48 89 e5                mov    %rsp,%rbp
    11d1:       48 83 ec 30             sub    $0x30,%rsp
    11d5:       48 89 7d d8             mov    %rdi,-0x28(%rbp)
    11d9:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
    11e0:       00 00 
    11e2:       48 89 45 f8             mov    %rax,-0x8(%rbp)
    11e6:       31 c0                   xor    %eax,%eax
    11e8:       c6 45 eb 42             movb   $0x42,-0x15(%rbp)
    11ec:       c6 45 ec 65             movb   $0x65,-0x14(%rbp)
    11f0:       c6 45 ed 5f             movb   $0x5f,-0x13(%rbp)
    11f4:       c6 45 ee 57             movb   $0x57,-0x12(%rbp)
    11f8:       c6 45 ef 68             movb   $0x68,-0x11(%rbp)
    11fc:       c6 45 f0 69             movb   $0x69,-0x10(%rbp)
    1200:       c6 45 f1 74             movb   $0x74,-0xf(%rbp)
    1204:       c6 45 f2 65             movb   $0x65,-0xe(%rbp)
    1208:       c6 45 f3 5f             movb   $0x5f,-0xd(%rbp)
    120c:       c6 45 f4 48             movb   $0x48,-0xc(%rbp)
    1210:       c6 45 f5 61             movb   $0x61,-0xb(%rbp)
    1214:       c6 45 f6 74             movb   $0x74,-0xa(%rbp)
    1218:       c6 45 f7 00             movb   $0x0,-0x9(%rbp)
    121c:       48 8d 55 eb             lea    -0x15(%rbp),%rdx
    1220:       48 8b 45 d8             mov    -0x28(%rbp),%rax
    1224:       48 89 d6                mov    %rdx,%rsi
    1227:       48 89 c7                mov    %rax,%rdi
    122a:       e8 91 fe ff ff          call   10c0 <strcmp@plt>
    122f:       89 45 e4                mov    %eax,-0x1c(%rbp)
    1232:       8b 45 e4                mov    -0x1c(%rbp),%eax
    1235:       48 8b 55 f8             mov    -0x8(%rbp),%rdx
    1239:       64 48 2b 14 25 28 00    sub    %fs:0x28,%rdx
    1240:       00 00 
    1242:       74 05                   je     1249 <check_password+0x80>
    1244:       e8 57 fe ff ff          call   10a0 <__stack_chk_fail@plt>
    1249:       c9                      leave  
    124a:       c3                      ret    

000000000000124b <main>:
    124b:       f3 0f 1e fa             endbr64 
    124f:       55                      push   %rbp
    1250:       48 89 e5                mov    %rsp,%rbp
    1253:       48 83 ec 40             sub    $0x40,%rsp
    1257:       89 7d cc                mov    %edi,-0x34(%rbp)
    125a:       48 89 75 c0             mov    %rsi,-0x40(%rbp)
    125e:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
    1265:       00 00 
    1267:       48 89 45 f8             mov    %rax,-0x8(%rbp)
    126b:       31 c0                   xor    %eax,%eax
    126d:       48 8d 05 90 0d 00 00    lea    0xd90(%rip),%rax        # 2004 <_IO_stdin_used+0x4>
    1274:       48 89 c7                mov    %rax,%rdi
    1277:       b8 00 00 00 00          mov    $0x0,%eax
    127c:       e8 2f fe ff ff          call   10b0 <printf@plt>
    1281:       48 8d 45 e0             lea    -0x20(%rbp),%rax
    1285:       48 89 c6                mov    %rax,%rsi
    1288:       48 8d 05 8a 0d 00 00    lea    0xd8a(%rip),%rax        # 2019 <_IO_stdin_used+0x19>
    128f:       48 89 c7                mov    %rax,%rdi
    1292:       b8 00 00 00 00          mov    $0x0,%eax
    1297:       e8 34 fe ff ff          call   10d0 <__isoc99_scanf@plt>
    129c:       48 8d 45 e0             lea    -0x20(%rbp),%rax
    12a0:       48 89 c7                mov    %rax,%rdi
    12a3:       e8 21 ff ff ff          call   11c9 <check_password>
    12a8:       89 45 dc                mov    %eax,-0x24(%rbp)
    12ab:       83 7d dc 00             cmpl   $0x0,-0x24(%rbp)
    12af:       74 11                   je     12c2 <main+0x77>
    12b1:       48 8d 05 66 0d 00 00    lea    0xd66(%rip),%rax        # 201e <_IO_stdin_used+0x1e>
    12b8:       48 89 c7                mov    %rax,%rdi
    12bb:       e8 d0 fd ff ff          call   1090 <puts@plt>
    12c0:       eb 0f                   jmp    12d1 <main+0x86>
    12c2:       48 8d 05 63 0d 00 00    lea    0xd63(%rip),%rax        # 202c <_IO_stdin_used+0x2c>
    12c9:       48 89 c7                mov    %rax,%rdi
    12cc:       e8 bf fd ff ff          call   1090 <puts@plt>
    12d1:       b8 00 00 00 00          mov    $0x0,%eax
    12d6:       48 8b 55 f8             mov    -0x8(%rbp),%rdx
    12da:       64 48 2b 14 25 28 00    sub    %fs:0x28,%rdx
    12e1:       00 00 
    12e3:       74 05                   je     12ea <main+0x9f>
    12e5:       e8 b6 fd ff ff          call   10a0 <__stack_chk_fail@plt>
    12ea:       c9                      leave  
    12eb:       c3                      ret    

Disassembly of section .fini:

00000000000012ec <_fini>:
    12ec:       f3 0f 1e fa             endbr64 
    12f0:       48 83 ec 08             sub    $0x8,%rsp
    12f4:       48 83 c4 08             add    $0x8,%rsp
    12f8:       c3                      ret    
