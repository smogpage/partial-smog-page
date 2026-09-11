options = odeset('OutputFcn', [], 'AbsTol', 1e-10, 'RelTol', 1e-3);
[t, y] = ode45(@(t, y) glu3(t, y, 0.25, 1, 1, 1, 1, 1, 1, 2.5), [0, 60], [0, 0, 0, 0, 0.5, 0.5], options);

plot(t, y(:, 1));
hold on;
plot(t, y(:, 2), 'r');
plot(t, y(:, 3), 'g');
plot(t, y(:, 4), 'm');
plot(t, y(:, 5), 'k');
plot(t, y(:, 6), 'x-');
title('Upper glycolysis model');
ylabel('concentration');
xlabel('time');
legend('Glu', 'G6P', 'F6P', 'F16P2', 'ATP', 'ADP');
