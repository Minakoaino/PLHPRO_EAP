# ενσωμάτωση βιβλιοθηκών
from datetime import date 
from random import choice
from string import digits
import time

# εκχώριση τυχαίου αλφαριθμητικού 11 ψηφίων
n = 11
amka_len = "".join(choice(digits) for i in range(n))
# μεταβλητή που αποτελεί το μήκος του αριθμητικού
amka = len(amka_len)
# μεταβλητή που αποτελεί τα 2 τελευταία νούμερα του τρέχοντος έτους
current_year = int(time.strftime("%y"))

# όσο η συνθήκη παραμένει αληθής
while True:
    amka_check = input('Παρακαλώ δώστε αριθμό ΑΜΚΑ: ')
        
    if amka == len(amka_check) and amka_check.isdigit() == True:
        # έλεγχος ότι το μήκος του αλφαριθμητικού αντιστοιχεί σε ΑΜΚΑ (11 ψηφία)
        print("Ο ΑΜΚΑ βρέθηκε και αποτελείται από:",len(amka_check),"ψηφία.") 
        # υπολογισμός και εμφάνιση της ηλικίας του χρήστη
        print("Ο χρήστης είναι",current_year - int(amka_check[4:6]) + 100 if current_year < int(amka_check[4:6]) else current_year - int(amka_check[4:6]),"χρονών")
        ## Προσδιορισμός φύλου με βάση αν το δεύτερο μέρος του ΑΜΚΑ είναι άρτιος ή περιττός
        print("γυναίκα" if int(amka_check[6:10]) % 2 == 0 else "άντρας")
        
    elif amka_check.isdigit() == False: 
        print("Δεν δώσατε αριθμό. Ο ΑΜΚΑ πρέπει να αποτελείται αποκλειστικά από αριθμούς! ")
        continue
    
    elif amka != len(amka_check) and amka_check.isdigit() == True:
         print("Παρακαλώ δώστε έγκυρο αριθμό ΑΜΚΑ:")
         continue
     
    # ## Ερώτηση στον χρήστη αν θέλει να επαναλάβει τη διαδικασία ή θέλει να τερματίσει το  πρόγραμμα
    run_again = input("Θέλετε να ελέγξετε άλλο ΑΜΚΑ, (Ν)αι/(Ο)χι;").upper()
   
    # το πρόγραμμα διακόπτεται όταν ο χρήστης δώσει ο
    if run_again == "Ο":
        # διακοπή εντολής βρόχου ακόμη κι αν η προϋπόθεση του βρόχου δεν έχει γίνει False   
        print("Τέλος προγράμματος")
        break        
    elif run_again =="Ν":
        continue
    else:
        print(input("Δεν δώσατε έγκυρη απάντηση. Πατήστε enter για να ξαναδοκιμάσετε"))