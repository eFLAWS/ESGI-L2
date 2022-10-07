/* main des exo*/

#include "stdlib.h"
#include "stdio.h"

/*
répète un nombre selon 1 11 111 .... 
*/
int againAndMore()
{
    int boucle = 0;
    while (boucle == 0)
    {
        int nb, i, value, sum = 0;
        printf("Quel nombre voulez-vous repeter ? ");
        scanf("%d", &value);
        printf("\nTaper le nombre de passages : ");
        scanf("%d", &nb);
        for (i = 0; i < nb; i++)
        {
            sum = sum * 10 + value;
            printf("\n%d", sum);
        } 
        
        printf("\nVoulez recommencer ? (0: oui 1: non)\n");
        scanf("%d", &boucle);
    }

    return 0;
}

int main(int argc, char** argv)
{
    int exo;
    printf("quel exo ?(1: againAndMore)\n");
    scanf("%d", &exo);

    switch (exo)
    {
        case 1:
            againAndMore();
            break;
        default:
            break;
    }
    
    
    return EXIT_SUCCESS;
}