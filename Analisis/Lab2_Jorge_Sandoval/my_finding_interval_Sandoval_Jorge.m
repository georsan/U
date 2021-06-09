function [a,b]=my_finding_interval_Sandoval_Jorge(f,a,b)

while sign(f(a))*sign(f(b))>0
 a=rand(1)*20-10;
 b=rand(1)*20-10;
 end
 disp('Se encontraron los intervalos: ');
 int = [a b];
 disp(int)
end