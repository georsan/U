function my_visual_secant_function_Sandoval_Jorge(fun,p0,p1,iter)
for n=1:iter
    pk = p1 -(fun(p1)*(p1-p0))/(fun(p1)-fun(p0));
    p0=p1;
    p1=pk;
   
end
  m = (fun(p1)-fun(p0))/(p1-p0);
    y = @(x) m*(x-p1)+fun(p1);
    y1 = @(x) 0*x;
    figure,
    fplot(fun);
    hold on
    fplot(y1,'--r');
    hold on;
    fplot(y);
    ylabel('f(x)');
    xlim([-10 10]);
    plot(p0,fun(p0),'*');
    plot(p1,fun(p1),'*');
    title('ITERACIONES');
    legend('f(x)','x--axis','sec');  
end