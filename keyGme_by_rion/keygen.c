#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define KEY_LENGTH 16

int32_t isValidAlpha(char arg1) {
    if ((int32_t)arg1 >= 0x41 && (int32_t)arg1 <= 0x5a)
        return 1;
    return 0;

}



int32_t isValidNum(char arg1) {
    if ((int32_t)arg1 >= 0x30 && (int32_t)arg1 <= 0x39)
        return 1;
    return 0;
}



int32_t isValid(const char* string) {
    size_t length = strlen(string);
    int32_t check = 0;

    for (int32_t i = 0; i < length - 1; i++) {
        if (!isValidAlpha(string[i]) && !isValidNum(string[i])) {
            puts("Found invalid character!");
            exit(3);  
        }

        check = (int64_t)((check + (int32_t)string[i]) >> 1) % 0xf00 + 0xa;
    }

    return check == (int32_t)string[length - 1];

}



void bruteForce() {

    char serialKey[KEY_LENGTH + 1]; 
    const char charset[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"; 
    int totalCharsetLength = strlen(charset);

    while (1) {
        for (int i = 0; i < KEY_LENGTH; i++) {
            serialKey[i] = charset[rand() % totalCharsetLength];
        }

        serialKey[KEY_LENGTH] = '\0'; 

        if (isValid(serialKey)) {
            printf("Found a valid serial key: %s\n", serialKey);
            return; 
        }
    }

}



int main() {
    bruteForce();
    return 0;

}
