#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/*
	Shiny
*/
int len_int(n){if (n < 10 && n>= 0)return 1;if (n < 0){return (0);}int ret = 0;while(n > 0){ret++;n = n / 10;}return ret;}
int main(void){
int i = 5;
if (i<=0){return(0);}if (__FILE__ != "Sully.c"){i-=1;}int n = ((len_int(i))+9);char nb[n];snprintf(nb, n, "Sully_%d.c", i);FILE *file = fopen(nb, "w");char *s = "#include <stdio.h>%c#include <string.h>%c#include <stdlib.h>%c/*%c%cShiny%c*/%cint len_int(n){if (n < 10 && n>= 0)return 1;if (n < 0){return (0);}int ret = 0;while(n > 0){ret++;n = n / 10;}return ret;}%cint main(void){%cint i = %d;%cif (i<=0){return(0);}if (__FILE__ != %cSully.c%c){i-=1;}int n = ((len_int(i))+9);char nb[n];snprintf(nb, n, %cSully_%cd.c%c, i);FILE *file = fopen(nb, %cw%c);char *s = %c%s%c;if (file){fprintf(file, s, 10, 10, 10, 10, 9, 10, 10, 10, 10, i, 10, 34, 34, 34, 37, 34, 34, 34, 34, s, 34, 34, 37, 37, 37, 34);fclose(file);char cmd[100];sprintf(cmd, %cgcc -Wall -Wextra -Werror %cs -o Sully_%cd; ./Sully_%cd%c, nb, i, i);system(cmd);}return (0);}";if (file){fprintf(file, s, 10, 10, 10, 10, 9, 10, 10, 10, 10, i, 10, 34, 34, 34, 37, 34, 34, 34, 34, s, 34, 34, 37, 37, 37, 34);fclose(file);char cmd[100];sprintf(cmd, "gcc -Wall -Wextra -Werror %s -o Sully_%d; ./Sully_%d", nb, i, i);system(cmd);}return (0);}