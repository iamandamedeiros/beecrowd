#include <stdio.h>
#define TAM 12

int main() {
    int i;
    int j;
    int colunaVerde = 11;
    char t;
    double m[TAM][TAM];
    double resultado = 0;
    
    scanf("%c",&t);
    
    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            
            scanf("%lf", &m[i][j]);
            
            if (j > colunaVerde) {
                resultado += m[i][j];
            }
        }
        if (i >= 6) colunaVerde++;
        if (i < 5) colunaVerde--;
    }
    if (t=='M') resultado /= 30.0;
    printf("%.1lf\n", resultado);

    return 0;
}