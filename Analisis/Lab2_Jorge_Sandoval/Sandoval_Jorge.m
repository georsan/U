function [raiz]=Sandoval_Jorge(f,a,b)
while sign(f(a))*sign(f(b))>0
 a=rand(1)*20-10;
 b=rand(1)*20-10;
end
 disp('Se encontraron los intervalos: ');
 int = [a b];
 disp(int)

 ni=0;
 e=1e-10;
 nt = ((log(abs(b-a)))-log(abs(e))/log(2))-1;
 c=(a+b)/2;

 while (abs(f(c))>=e)
 c = (a+b)/2;
 fc = f(c);
 ni=ni+1;
 if fc == 0
 break
 end
 if sign(f(a))*sign(f(c))<0
 b=c;
 else
 a=c;
 end
 end
 raiz=c;
 disp('la raiz es:')
 disp(raiz)
 disp('El numero de iteraciones es:')
 disp(ni)
 disp('El numero de iteraciones teórico es:')
 disp(nt)


 xd=[0.135335 0.018315 0.002478 0.0003354 0.00004539];
 Nt= [8.6396 15.2834 21.9273 28.5712 35.2150];
 dx=[15 21 27 35 41];
 plot(xd,Nt,'--r')
 xlabel('Epsilon')
 hold on
 plot (xd, dx,':b')
 ylabel('iteraciones teórico (--), iteraciones practica(…)')
end