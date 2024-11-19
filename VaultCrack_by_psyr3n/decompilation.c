// Decompilation of VaultCrack
// Tried to keep it as close as possible to the given assembly.
// check_password is about 80% the same and the main method less.
// Regardless, they are practically the same and this can be used as a reference
// or guide for beginners.
// 
// Have a great day :)
// github.com/johnnnathan






//Using snake case because of the ghidra output
#include <stdio.h>
#include <string.h>
int check_password(char* input){

  char target_password[13];
  target_password[0] = 0x42; // 'B'
  target_password[1] = 0x65; // 'e'
  target_password[2] = 0x5F; // '_'
  target_password[3] = 0x57; // 'W'
  target_password[4] = 0x68; // 'h'
  target_password[5] = 0x69; // 'i'
  target_password[6] = 0x74; // 't'
  target_password[7] = 0x65; // 'e'
  target_password[8] = 0x5F; // '_'
  target_password[9] = 0x48; // 'H'
  target_password[10] = 0x61; // 'a'
  target_password[11] = 0x74; // 't'
  target_password[12] = 0x00; // Null terminator '\0'
  int flag = strcmp(input, target_password);
  return flag;

}


int main(int argc, char *argv[])

{
  int flag;
  char password [23];
  printf("Enter the password: ");
  //The scanf in the disassembly shows "%50s" but that doesn't make sense since
  //password is shown to be 23 long, decided to keep the 23 length value
  scanf("%22s" , password);

  flag = check_password(password);


  if (flag){
    printf("Wrong Input !\n");
  }
  else{
    printf("Welcome !\n");
  }
  return 0;
}
