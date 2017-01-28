#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int blunder(int un, int startn) {
     if(((un * startn + (un/startn))  % startn) == 0) {
               return startn;
     }
     return blunder(un, startn+1);
}


int main()
{
     printf(">>");
     FILE *file;
     char *fileName;
     scanf("%s", &fileName);
     printf("\n");
     file = fopen(&fileName, "w+");
     int userNumber = 5434435434;
     int data[10000];
     int usedNumbers[sizeof(data)/sizeof(int*)];
     int startingNumber = 0;

     for(int x = 0; x != sizeof(data) / sizeof(int*); x++) {
               startingNumber++;
               data[x] = blunder(userNumber, startingNumber) - startingNumber;
               printf("Attempt Number %d >> %d\n", x+1, data[x]+1);
               char dataToWrite[100];
               sprintf(dataToWrite, "Attempt Number %d >> %d\n", x+1, data[x]+1);
               fputs(&dataToWrite, file);
     }

     fclose(file);
     printf("%d Calculations Performed And Wrote To File.", sizeof(data)/sizeof(int*));

    return 0;
}
