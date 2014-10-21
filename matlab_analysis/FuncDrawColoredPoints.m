function FuncDrawColoredPoints(x,y,z,drawErrorBar,confidenceX,confidenceY,graphTitle,graphXlabel,graphYlabel)

%prepare color map
maxz = max(z);
minz = min(z);
colour_range = jet(length(z)+1);
cmap = zeros(length(z),3);
for i = 1:length(z)
    color_index = round((length(z)*(z(i,1)-minz)/(maxz-minz)))+1;
    cmap(i,:) = colour_range(color_index,:);
end

%draw graph
if(drawErrorBar)
    scatter(x, y, 100, cmap, 'filled')
    hold on
    for i = 1:length(x)
        tmp = errorbar(x(i),y(i),confidenceY(i));
        set(tmp,'Color',cmap(i,:));
        tmp = herrorbar(x(i),y(i),confidenceX(i));
        set(tmp,'Color',cmap(i,:));
    end
    scatter(x, y, 100, cmap, 'filled')  %%repeated call to put points in front of confidence lines
else
    scatter(x, y, 50, cmap, 'filled')
end
hold off

grid on;

lighting phong
shading interp
colorbar EastOutside
caxis([min(z), max(z)])

title(graphTitle,'FontSize',12);
xlabel(graphXlabel,'FontSize',12)
ylabel(graphYlabel,'FontSize',12)

%print -dpdf figure_color2D.pdf


hold off

pause(0.01);

end