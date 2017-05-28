#include<stdio.h>

main(){
	
	int caso,visitas,i,j,k,cont=0;
	scanf("%d",&caso);

	for(i=1; i<=caso;i++){
		scanf("%d",&visitas);
		
		int Ai[visitas];
	
		for(j=0;j<visitas;j++){
			scanf("%d",&Ai[j]);
			printf("%d",Ai[j]);
			
			for(k=0;k<=j;k++){
				if(k==0){
					cont++;
					printf("%d\n",cont);
					system("pause");
				} else if(Ai[j]!=Ai[k]){
					cont++;
					printf("%d\n",cont);
				}
			}
		}
		printf("Caso %d: %d",i,cont);
	}
	
	return 0;
}
