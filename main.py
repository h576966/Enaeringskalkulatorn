import streamlit as st
from datetime import date


col1, col2 = st.columns(2)    
   
with col1:
    

    with st.form("Ernæringsstatus", clear_on_submit=False):
        
        sex = st.selectbox(
            "Kjønn:",
            ('Kvinne', 'Mann')
        )

        age = st.number_input(
            label="Alder:",
            min_value=0,
            step=1,
        )
        
        height = st.number_input(
            label="Høgde(cm):",
            min_value=0,
            step=1,
        )

        weight = st.number_input(
            label="Vekt:",
            min_value=0.0,
            step=0.1,
        )

        prevWeight = st.number_input(
            label="Tidlegare vekt:",
            min_value=0.0,
            step=0.1,
        )

        prevDate = st.date_input(
            label="Dato forrige vekt:",
            value=date.today(),
        )
        
        activityLvl = st.selectbox(
            "Daglig aktivitet:",
            ("Sengeliggende(1.2)",
             "Stillesittende arbeid(1.35)",
             "Lite fysisk aktivitet(1.55)",
             "Stående arbeid(1.75)",
             "Hardt fysisk arbeid(2)"),
            
        )
        
        activity = st.checkbox(
            label="Betydelig grad av fysisk aktivitet(+.3)",
            value=False,
        )
        
        submitted = st.form_submit_button() 
             
 
with col2:
    kcalNeed =str(round(30 * weight))
    st.write("Enæringsbehov:", kcalNeed, " kcal/d")
    
    
    if (sex == "Mann"):
        sexMod = 5
    elif(sex=="Kvinne"):
        sexMod = -161
    
    RMR = ((10 * weight)+ (6.25 * height) + (sexMod))-(5*age)
    RMR2W = str(round(RMR))
    

    
    if(activityLvl=="Sengeliggende(1.2)"):
        PAL = 1.2
    elif(activityLvl=="Stillesittende arbeid(1.35)"):
        PAL = 1.35
    elif(activityLvl=="Lite fysisk aktivitet(1.55)"):
         PAL = 1.55
    elif(activityLvl=="Stående arbeid(1.75)"):
        PAL = 1.75
    elif(activityLvl=="Hardt fysisk arbeid(2)"):
        PAL = 2
    
    if(activity):
        PAL+=.3
    
    #st.write("PAL")
    #st.write(PAL)
    
    Mifflin = str(round(RMR * PAL))
    st.write("Mifflins formel:", Mifflin, " kcal/d,", " RMR(", RMR2W,")")
    
    waterReq = str(round((.03 * weight) ,2))
    st.write("Væskebehov:", waterReq)
    
    
    
    h = (height/100)
    BMI =  str(round(weight/ (h*h), 2))
    st.write("KMI:", BMI)
    
    
    dateToday = date.today()
    dateLast = prevDate
    
    diff = (dateToday - dateLast).days

    #st.write(diff)
    
    if diff <= 61:
        months2 = True
    elif diff <=91:
        months3 = True
    elif diff <=181:
        months6 = True
    
    if (submitted) & (int(prevWeight) !=0):    
        weightChange =round(((weight/prevWeight) - 1 )*100)
        change = str(weightChange)
        KMI = float(BMI)
        if weightChange > -5:
            st.write("Vekt forendring: ", change)
        elif (weightChange <= -15) & (diff <= 181):
            st.write("Vekt forendring: ", change, " Alvorlig undereræring")
        elif (KMI <= 16) | ((KMI <=18.5) & (age >=70)):
            st.write("Vekt forendring: ", change, " Alvorlig undereræring")
        elif (KMI<= 18.5) & (weightChange <= -5) & (diff <= 91 ):
            st.write("Vekt forendring: ", change, " Alvorlig undereræring")
        elif (KMI<= 20) & (age >= 70) & (weightChange <= -5) & (diff <= 91 ):
            st.write("Vekt forendring: ", change, " Alvorlig undereræring")
        elif  ((weightChange<=-10) & (diff<=91)) | ((weightChange<=-5) & (diff<=61)):
            st.write("Vekt forendring: ", change, " Moderat undereræring")
        elif  (KMI<=-18.5) | ((KMI<=20) & (age>=70)):
            st.write("Vekt forendring: ", change, " Moderat undereræring")
        elif  (weightChange <= -5) & (KMI<=20.5) & (diff<=181):
            st.write("Vekt forendring: ", change, " Moderat undereræring")
        elif  (age>65) & (KMI<=22) & (weightChange <= -5) & (diff<=181):
            st.write("Vekt forendring: ", change, " Moderat undereræring")
            
   