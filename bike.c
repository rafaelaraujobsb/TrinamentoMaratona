#include<stdio.h>

main(){
	
	int caso,turistas,assentos, lugares,n=1;
	
	scanf("%d",&caso);

	do{
		scanf("%d %d",&turistas,&assentos);
		assentos = assentos - 1;
		
		lugares = turistas % assentos;
		
		if(lugares == 0){
			lugares = turistas/assentos;
		} else {
			lugares = turistas/assentos+1;
		}
		
		printf("Caso %d: %d\n",n,lugares);
		n++;
	}while(n<=caso);
	
	return 0;
}
