from math import log
def vpp(P,s,f): return P*s/(P*s+(1-P)*f)
for name,P,c,m,f in [("pairs",.10,.1,.2,.05),("un modele",.02,.6,.2,.05),("partage precis",.02,.6,.2,.005),("indep",.02,.1,.1,.005)]:
    s=(1-c)*(1-m); v=vpp(P,s,f)
    print(name,round(s,4),round(v*100,2),round(1/v,2),"esc VPP",round((1-s*v)*100,2),"esc1",round((1-s)*100,2),"R VPP",round(P*(1-s*v)*100,3),"R1",round(P*(1-s)*100,3))
for N in (4,12):
    for q in (0,.03):
        a=1-(1-q)*.94**N; b=1-(1-q)*(1-.0036)**N
        print(N,q,round(a*100,2),round(b*100,2), round(q/b*100,1) if q else None, "indep",round((1-.94**N)*100,2),round((1-(1-.0036)**N)*100,2))
print("12 vs 4 ratio", (1-.94**12)/(1-.94**4))
print("vpp depistage",vpp(.01,.9,.05), 2/13)
print("severity idee",1-(.88**5+.03**5)/.91, "rare",1-(.22**5+.2**5+.16**5+.14**5+.1**5)/.82, "conn",1-(.02**5+.01**5)/.03)
print("alerte",1-.97**4,1-.18**4,1-.09**4)
print("pw",1-(1-.001)*(1-.08),1-(1-1e-5)*(1-1/6), 1/26,1/10001)
print("surprises",-log(.05),-log(.001),-log(.95),-log(.999),-log(.2),-log(.02),-log(.8),-log(.98),.8/.98)
print("odds",5/29,5/9,5/73,25/29)
print("0.294 inverse",17/5)
# risk shared model vs P
for P in (.06,.07,.08,.1):
    s=.32; v=vpp(P,s,.05); print(P, round(P*(1-s*v)*100,2))
print("VPP at 2% with f=5% controleur indep", vpp(.02,.81,.05))
print("D.3 4.1% vs", 1/26)
print("dix x 0.01 etc", .1*.01,.01*.9)
