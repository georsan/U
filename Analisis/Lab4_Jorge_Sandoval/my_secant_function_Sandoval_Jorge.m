function my_secant_function_Sandoval_Jorge(fun,p0,p1,iter)

for i=1:iter
    pk=p1-(fun(p1)*(p1-p0))/(fun(p1)-fun(p0));
    p0=p1;
    p1=pk;    
end
disp("La raiz es "+pk);
end