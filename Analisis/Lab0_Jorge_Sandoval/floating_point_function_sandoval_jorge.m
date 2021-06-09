function P=floating_point_function_sandoval_jorge(n)
if n<0
    signo=num2str(1);
else
 
   signo=num2str(0);
end
suma=-1;
j=0;
binario=decimal_binario(n);
for i=2:length(binario)
    j=j+1;
    suma=suma+1;
    if binario(i)=='.'
    exponente=suma;
    j=j-1;
    else
        matissa(j)=binario(i);
    end
end
bias=2^(7-1)-1;
exp=exponente+bias;
expB=dec2bin(exp);


k=length(matissa);
valor=1;
manti(1)=num2str(0);
for i=1:8
if valor<=k
manti(i)=matissa(i);
else
    manti(i)=num2str(0);
end
valor=valor+1;
end
P=[signo expB manti];

end
    

