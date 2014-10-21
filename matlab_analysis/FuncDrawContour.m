function FuncDrawContour(x,y,z,graphTitle,graphXlabel,graphYlabel)

gridStep = max(size(x,1)/10,100);

xlin=linspace(min(x),max(x),gridStep);
ylin=linspace(min(y),max(y),gridStep);
[X,Y]=meshgrid(xlin,ylin);
Z=griddata(x,y,z,X,Y,'cubic');
%
mesh(X,Y,Z); % interpolated
axis tight; hold on
surf(X,Y,Z)
if(size(x,1) <= 100)
    plot3(x,y,z,'xk','MarkerSize',3);
elseif(size(x,1) <= 1000)
    plot3(x,y,z,'.k','MarkerSize',2);
end

lighting phong
shading interp
colorbar EastOutside
%daspect([1 1 100]);
%set(gca,'ydir','reverse');
view(2);

title(graphTitle,'FontSize',12);
xlabel(graphXlabel,'FontSize',12)
ylabel(graphYlabel,'FontSize',12)
grid on;
hold off

%print -dpdf figure_color2D.pdf
pause(0.01);

end