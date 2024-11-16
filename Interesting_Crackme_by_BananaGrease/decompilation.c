// This is the decompilation of the "Interesting Crackme" challenge by BananaGrease
//
// This is not meant to be a operation accurate decompilation, the only thing I care about
// recreating is the high-level actions of the application, for decompilation practice and 
// allowing people following along to experiment. The source code can be found in the 
// comments of the challenge, by the author himself.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printWelcome() {
  printf("---------- Welcome To My First CrackMe Challenge! ---------- \n\n");
}

void clearScreen() {
#ifdef _WIN32
    system("cls");
#else 
  system("clear");
#endif
}


char* generatePassword(char *username) {
  static char password[16];
  size_t len = strlen(username);

  memset(password, ' ', sizeof(password));

  for (int i = 0; i < len; i++) {
    password[i] = username[i] + i;  
  }

  for (int i = len; i < sizeof(password); i++) {
    password[i] = ' ' + (i % 16);  
  }

  password[sizeof(password) - 1] = '\0';

  return password;
}

int main(int argc, char *argv[]) {
  char username[16];
  char password[16];
  clearScreen();
  printWelcome();
  printf("Please Enter Your Username: ");
  scanf("%15s", username);  
  clearScreen();

  printWelcome();
  printf("Please Enter Your Licence Key: ");
  scanf("%15s", password);  
  clearScreen();

  char* generatedPassword = generatePassword(username);
  if (strcmp(password, generatedPassword) == 0) {
    printWelcome();
    printf("Authentication Success!\n");
  } else {
    printWelcome();
    printf("Authentication Failure!\n");
  }

  return 0;
}
