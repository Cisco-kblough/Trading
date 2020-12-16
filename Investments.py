i=1
stop=60
init_prin=85000
min1=.015
min2=.02
min3=.025
yearly_add=20000
run_prin1=init_prin
run_prin2=init_prin
run_prin3=init_prin
while i<=stop:
    if i%12==0:
        run_prin1=run_prin1+yearly_add
        run_prin2=run_prin2+yearly_add
        run_prin3=run_prin3+yearly_add
    monthly1=run_prin1*min1
    monthly2=run_prin2*min2
    monthly3=run_prin3*min3
    run_prin1=monthly1 + run_prin1
    run_prin2=monthly2 + run_prin2
    run_prin3=monthly3 + run_prin3
    print(i, round(monthly1, 2), round(monthly2, 2), round(monthly3, 2), round(run_prin1, 2), round(run_prin2, 2), round(run_prin3, 2))
    i=i+1
    
