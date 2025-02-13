#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h> 

int processInput(char *input_string) {
    char *advanced_index;
    int result;
    char current_index;
    
    result = 0x1505; 
    advanced_index = input_string;

    while (1) {
        current_index = *advanced_index;
        advanced_index = advanced_index + 1;
        if (current_index == 0) break; 
        result = result * 0x21 + (int)current_index; 
    }
    return result;
}

void testInputSizes() {
    char input[256];
    int result;
    int target_value = -773328759;
    int closest_diff = INT_MAX;    
    char closest_input[256];      

    char characters[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    for (int len = 7; len <= 10; len++) {
        for (int i = 0; i < 1000000; i++) { 
            for (int j = 0; j < len; j++) {
                input[j] = characters[rand() % strlen(characters)];
            }
            input[len] = '\0'; 

            result = processInput(input);

            int diff = abs(result - target_value);

            if (diff < closest_diff) {
                closest_diff = diff;
                strcpy(closest_input, input);  
            }

            if (result == target_value) {
                printf("Found matching input: %s\n", input);
                printf("Result: %d (Target Value Matched)\n", result);
                return; 
            }
        }
    }

    printf("No matching input found.\n");
    printf("Closest input: %s\n", closest_input);
    printf("Closest result: %d\n", processInput(closest_input));
    printf("Difference from target: %d\n", closest_diff);
}

int main() {
    srand(time(NULL));

    testInputSizes();

    return 0;
}
