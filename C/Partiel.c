/*
 Objectif: Partiel de C
 Date:  04/03/22
 Auteur: Paul BULLIARD
 Classe: 2A4MCSI
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Annonce des variables

int main(int size, int srand, int *bDate, int temp, void calendrier, int datePopulaire, int cMois, int dateMax);

//Création du tableau avec les dâtes de naissance

int main()
{
    int size;
    int j, i;
    int temp;
    int sum = 0;


    printf("Entrer le nombre de jours dans l'année ( 366): ");
    scanf("%d", &size);


    int cMois[size];
    int *bDate = malloc(sizeof(int) * size);

// Affichage du tableau avec les valeurs aléatoires 

    for (i = 0; i < size; i++)
    {
        srand(time(NULL));
        bDate[i] = (rand() % 366 + 1);
        printf("\n La case %d a une valeur de %d \n", bDate[i])

        int main(void)
    }

// Nombre d'étudiants ayant la même dâte de naissance (toute case du tableau ayant une valeur supérieure ou égale à 2)

    int n, m, size, count = 0;

     for( n = 0; n < size; n++)
    {
        scanf("%d", &arr[n]);
    }
    for(n = 0; n < size; n++)
    {
        for(m = n + 1; m < size; j++)
        {
            if(arr[n] == arr[m])
            {
                count++;
                break;
            }
        }
    }

    printf("\n Le nombre de personnes ayant la même dâte d'anniversaire est de %d", count);

    return 0;

    int dateMax = datePopulaire(cMois, n);

    printf("\n La date de naissance la plus populaire est : %d", dateMax; 

    return 0;
}

// Tableau des mois avec le nombre de personnes nées par moi

/* 
static void main(String[] args) {
    mois = new String[13];
    mois[ 0 ] = null;
    mois[ 1 ] = "Janvier";
    mois[ 2 ] = "Février";
    mois[ 3 ] = "Mars";
    mois[ 4 ] = "Avril";
    mois[ 5 ] = "Mai";
    mois[ 6 ] = "Juin";
    mois[ 7 ] = "Juillet";
    mois[ 8 ] = "Août";
    mois[ 9 ] = "Septembre";
    mois[ 10 ] = "Octobre";
    mois[ 11 ] = "Novembre";
    mois[ 12 ] = "Décembre";

int jourMois[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
*/

int main(){
    void calendrier
            int cMois[366] = ;
            int *janvier = cMois;
            int *fervier = cMois + 31;
            int *mars = cMois + 60;
            int *avril = cMois + 91;
            int *mai = cMois + 121;
            int *juin = cMois + 152;
            int *juillet = cMois + 182;
            int *aout = cMois + 213;
            int *septembre = cMois + 244;
            int *octobre = cMois + 274;
            int *novembre = cMois + 305;
            int *decembre = cMois + 336;

    for (int i = 0; i < 366; i++)
        {     
        printf("%d ", calendrier[i]);
        }

// Calcul pour chaque mois

    for(i=0; i<size; i++)
        {
            scanf("%d", &janvier[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(janvier[i] == janvier[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en janvier est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &fevrier[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(fevrier[i] == fevrier[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en février est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &mars[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(mars[i] == mars[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en mars est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &avril[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(avril[i] == avril[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en avril est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &mai[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(mai[i] == mai[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en mai est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &juin[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(juin[i] == juin[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en juin est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &juillet[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(juillet[i] == juillet[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en juillet est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &aout[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(aout[i] == aout[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en août est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &septembre[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(septembre[i] == septembre[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en septembre est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &octobre[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(octobre[i] == otobre[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en octobre est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &novembre[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(novembre[i] == novembre[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en novembre est de %d", count[i]);
    for(i=0; i<size; i++)
        {
            scanf("%d", &decembre[i]);
        }
        for(i=0; i<size; i++)
        {
            for(j=i+1; j<size; j++)
            {
                if(decembre[i] == decembre[j])
                {
                    count++;
                    break;
                }
            }
        }
        printf("\n Le nombre d'étudiants nés en décembre est de %d", count[i]);
}


// Recherche de la date de naissance la plus populaire (Valeur du tableau la plus grande)

int datePopulaire(int cMois[], int n) 
{
    int i, j, dateMax, count;
     int maxCount = 0;
    for(i = 0; i< n; i++)
    {
        count = 1;
        for(j = i+1; j < n; j++)
        {
            if(cMois[j] == cMois[i])
            {
                count++;
                if(count > maxCount)
                {
                    dateMax= cMois[j];
                }
            }
        }
    }
    return dateMax

    printf("\n La date de naissance la plus populaire est le %d", dateMax[0]);

    return 0;
}