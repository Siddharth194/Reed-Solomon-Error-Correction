def Thues(ri,qi,si,ti,r_asterisk,t_asterisk):
    i=0

    #Extracting the required ri[j] such that ri[j] is the greatest value of all the elements having an index greater than that of r*.
    while(True):
        if(ri[i]<r_asterisk):
            break
        i=i+1

    return ri[i],qi[i],si[i],ti[i]
