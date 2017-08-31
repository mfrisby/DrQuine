#include <stdio.h>
/*
	Shiny
*/
#define TOTO
#define TATA
#define FT() int main(void){FILE *file = fopen("Grace_kid.c", "w");if(file){char *s = "#include <stdio.h>%c/*%c%cShiny%c*/%c#define TOTO%c#define TATA%c#define FT() int main(void){FILE *file = fopen(%cGrace_kid.c%c, %cw%c);if(file){char *s = %c%s%c;fprintf(file, s, 10, 10, 9, 10, 10, 10, 10, 34, 34, 34, 34, 34, s, 34, 10);fclose(file);}return(0);}%cFT();";fprintf(file, s, 10, 10, 9, 10, 10, 10, 10, 34, 34, 34, 34, 34, s, 34, 10);fclose(file);}return(0);}
FT();