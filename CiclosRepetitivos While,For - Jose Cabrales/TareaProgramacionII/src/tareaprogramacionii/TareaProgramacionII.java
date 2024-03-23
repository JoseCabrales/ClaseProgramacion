package TareaProgramacionII;
import java.util.Scanner;


public class TareaProgramacionII {
    public static void main(String[] args) {
         int i,x,a;
     
         Scanner teclado = new Scanner(System.in);
    
    
        
        
    a=5;
    x=0;
    while(a>x){
        x+=1;
        System.out.println("""
                   Elija una Opcion : 1. Personas
                   2. Vehiculos
                   3. Universidades
                   4. Notas
                   5. Salir""");
        i = teclado.nextInt();

        if(i == 1){
        System.out.println("Seleccionaste la opcion Personas");
         }
        
        if(i == 2){
        System.out.println("Seleccionaste la opcion Vehiculos");
        }
        
        if(i == 3){
        System.out.println("Seleccionaste la opcion Universidades");
        }
        
        if(i == 4){
        System.out.println("Seleccionaste la opcion Notas");
        }
        
        if(i==5){
        System.out.println("Saliendo del programa");
        
        }
        
        
         
                
                
 
     }
   }
}
        

        


    
        
        
         
        
        
        
         