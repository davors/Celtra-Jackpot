function FuncDrawSurface(x,y,z,graphTitle,graphXlabel,graphYlabel)


tri = delaunay(x,y);
size(tri);
trisurf(tri, x, y, z);
lighting phong
shading interp
colorbar EastOutside
%daspect([1 1 1]);
%set(gca,'ydir','reverse');
view(2);

title(graphTitle,'FontSize',12);
xlabel(graphXlabel,'FontSize',12)
ylabel(graphYlabel,'FontSize',12)

hold on
if(size(x,1) <= 100)
    plot3(x,y,z,'xk','MarkerSize',3);
elseif(size(x,1) <= 1000)
    plot3(x,y,z,'.k','MarkerSize',2);
end
% ca = daspect;
% ca(1:2) = 1;
% daspect(ca);
xlim([min(x) max(x)]);
ylim([min(y) max(y)]);
hold off
grid on;

%print -dpdf figure_color2D.pdf
pause(0.01);

end