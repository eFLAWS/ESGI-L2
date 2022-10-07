COURS

/* Cours loupé à rattraper */

/*
 Objectif: afficher la suite 9, 99, 999 etc ..
 Date:  22/10/21
 Auteur: Frédéric Sananes
*/
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
   int nb;
   int i;
   int value = 9;
   int sum = 0;
   printf("\nTaper le nombre de passages : ");
   scanf("%d", &nb);
   for(i = 0; i < nb; ++i) {
       sum = sum * 10 + value;
       printf("\n%d ", sum);
   }
    return EXIT_SUCCESS;
}

/* Second period */

int arr [10] = {1,2,3,5,7,11,13,17,19,23};
int arra