
programa fibonacci; 
var
	int n, fib1, fib2, i;

principal()
{
	escribe("Introduce numero mayor que 1: ");
	lee(n); 

	si (n > 1) entonces
	{
		fib1 = 1;
		fib2 = 1;
		escribe(fib1);

		desde i = 0 hasta n hacer
		{
			escribe(fib2);
			fib2 = fib1 + fib2;
			fib1 = fib2 - fib1;
		}
	}	
	sino
	{
		escribe("numero menor a 1");
	}
	
}