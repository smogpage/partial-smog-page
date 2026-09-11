function dydt = glu3(t, y, k1, k2, k3, nk3, k4, k5, k6, k7)

% For indexing
glu = 1;
g6p = 2;
f6p = 3;
f16p2 = 4;
atp = 5;
adp = 6;

% Rate equations
v1 = k1;
v2 = k2 * y(glu) * y(atp);
v3 = k3 * y(g6p) - nk3 * y(f6p);
v4 = k4 * y(f6p) * y(atp);
v5 = k5 * y(f16p2);
v6 = k6 * y(f16p2);
v7 = k7 * y(adp);

% ODE equations
dydt(glu) = v1 - v2;
dydt(g6p) = v2 - v3;
dydt(f6p) = v3 - v4 + v5;
dydt(f16p2) = v4 - v5 - v6;
dydt(atp) = -v2 - v4 + v7;
dydt(adp) = v2 + v4 - v7;

dydt = dydt';
end