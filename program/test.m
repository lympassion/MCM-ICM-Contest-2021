x=1:1:5;%x轴上的数据，第一个值代表数据开始，第二个值代表间隔，第三个值代表终止
a=[203.024,113.857,256.259,244.888,293.376]; %a数据y值
b=[334.4,143.2,297.4,487.2,596.2]; %b数据y值
%  plot(x,a,'--db',x,b,'-or'); %线性，颜色，标记
plot(x,a,'--db', 'LineWidth',5)
hold on
plot(x,b,'-or', 'LineWidth',3)
hold off
axis([0,6,0,700])  %确定x轴与y轴框图大小
set(gca,'XTick',[0:1:6]) %x轴范围1-6，间隔1
set(gca,'YTick',[0:100:700]) %y轴范围0-700，间隔100
legend('Neo4j','MongoDB');   %右上角标注
xlabel('深度')  %x轴坐标描述
ylabel('时间（ms）') %y轴坐标描述
