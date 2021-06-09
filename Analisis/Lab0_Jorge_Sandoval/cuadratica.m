function[x1,x2]=cuadratica(a,b,c)
if b>0
   x1=(-2*c)/(b+sqrt(b^2-4*a*c));
   x2=(-b-sqrt(b^2-4*a*c))/(2*a);
else
   x1=(-b+sqrt(b^2-4*a*c))/(2*a);
   x2=(-2*c)/(b-sqrt(b^2-4*a*c));
end
end

