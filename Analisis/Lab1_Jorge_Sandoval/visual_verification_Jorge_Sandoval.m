function visual_verification_Jorge_Sandoval(fun,a,b)    
fplot(fun, [a b]);
    hold on
    fplot(@(x)x, [a b]);
    fplot(@(x)a, [a b], '--');
    fplot(@(x)b, [a b], '--');
    legend('f(x)','y = x', 'a', 'b')
    xlabel('x');
    ylabel('y');
    hold off
    grid on
end