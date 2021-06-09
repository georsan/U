function [P]=my_visual_bisection_function_Sandoval_Jorge(f,a,b,iter)

while sign(f(a))*sign(f(b))>0
 a=rand(1)*20-10;
 b=rand(1)*20-10;
end
 disp('Se encontraron los intervalos: ');
 int = [a b];
 disp(int)


 c=(a+b)/2;
 ni=0;

 while (abs(f(c))>=iter)
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
 root=c;
 disp('la raiz es:')
 disp(root)
 disp('El numero de iteraciones es:')
 disp(ni)
 
 fplot(f,[-11,11])
 hold on
 
 plot(root,f(root),'*')
 grid on;
end
