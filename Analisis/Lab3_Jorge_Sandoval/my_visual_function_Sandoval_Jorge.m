function my_visual_function_Sandoval_Jorge(fun,p0,iter)
syms x;
der = matlabFunction(diff(fun,x));

for i=1:iter
    root=p0-(fun(p0)/der(p0));
    p0=root;
    scatter(p0,fun(p0));
        hold on 
        grid on
end
fplot(fun, [-20 20]);
fplot(@(x)0, [-20 20])

end