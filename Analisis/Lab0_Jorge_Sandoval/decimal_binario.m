function [binario]=decimal_binario(number)
if number<0
number=number*-1;
end
parteE=floor(number);
parteD=rem(number,1);
j=1;
entero=floor(parteE/2);
sobra=rem(parteE,2);
binario(j)=num2str(sobra);

while entero>=1
    j=j+1;
    parteE=entero;
    entero=floor(parteE/2);
    sobra=rem(parteE,2);
    binario(j)=num2str(sobra);
    
end
j=j+1;
binario=fliplr(binario);
binario(j)=num2str('.');

if parteD==0
    binario(j+1)=num2str(0);
    decimal=1;
else
    decimal=0;
end
while decimal~=1
    j=j+1;   
    decimal=parteD*2;
    parted=rem(decimal,1);
    binario(j)=num2str(floor(decimal));
    parteD=parted;
end
end