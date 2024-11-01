//Decompilation of the main method of the crackmes challenge 
// I am coding on linux so can not call the IsDebuggerPresent from the windows.h library, feel free to add it yourself.

#include <stddef.h>
#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[])
{
  char password[9];
  char xorPassword[9];
  char input[9];


  password[0] = 'Y';
  password[1] = 'o';
  password[2] = 'u';
  password[3] = 'r';
  password[4] = 'P';
  password[5] = 'a';
  password[6] = 's';
  password[7] = 's';
  password[8] = '\0';

  for (int i = 0; i < 8; i++){
    xorPassword[i] = password[i] ^ 10;
  }
  xorPassword[8] = '\0';
  //IsDebuggerPresent call would be here
  printf("Give your password:");

  fgets(input, sizeof(input), stdin);
  size_t length = strcspn(input, "\n");
  input[length] = '\0';
  for (int i = 0; i < 8; i++){
    input[i] = input[i] ^ 10;
  }
  int result = memcmp(xorPassword, input, length);
  if (result == 0){
    printf("Success");
  }else {
    printf("Failure");
  }

  return 0;
}

