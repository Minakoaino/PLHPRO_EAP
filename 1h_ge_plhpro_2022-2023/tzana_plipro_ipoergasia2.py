# ενσωμάτωση βιβλιοθηκών
import time

# συμβολοσειρά για τις επιλογές του υπολογιστή
choices = 'ΨΧΧΠΨΧΨΠΠΠΨΠΨΧΠΨΠΧΨΧΠ'
x = 0
# Χρησιμοποιούμε την εντολή βρόχου while προκειμένου το παιχνίδι να συνεχίζεται όσο η συνθήκη παραμένει αληθής  
while True:

    # επιλογές χρήστη 
    player_choices = ["Ψ", "Χ", "Π"]
    # αμυντικός προγραμματισμός ώστε να βεβαιωθούμε ότι η επιλογή του χρήστη είναι έγκυρη 
    # το πρόγραμμα συνεχίζει να ζητάει απο το χρήστη έγκυρη επιλογή ενώ όταν βάλει σωστή επιλογή το παιχνίδι ξεκινάει
    # το πρόγραμμα δέχεται τις επιλογές ακόμα και αν ο χρήστης βάλει μικρά γράμματα αφού μετατρέπουμε το input σε uppercase
    player = None
    while player not in player_choices:
        print("Παρακαλώ δώσε Π, Ψ η Χ: ")
        player = input("Διάλεξε Πέτρα (Π) Ψαλίδι (Ψ) η Χαρτί (Χ): ").upper()
        
        # Υπολογιστης
        # Ο υπολογιστής διαλέγει κάθε φορά το επόμενο στοιχείο της συμβολοσειράς. 
        # Αν τελειώσουν οι επιλογές ξεκινάει από την αρχή    
        computer =  choices[x]
        if x == len(choices) -1:
            x=0
        else:
          x = x +1 
    
    # όταν χρήστης και υπολογιστής έχουν ίδια επιλογή οδηγεί σε ισοπαλία 
    if player == computer:
        print("Ο υπλογιστής διάλεξε: ",computer)
        print("Διάλεξες: ",player)
        print("Ισοπαλία!")

    # Η πέτρα κερδίζει το ψαλίδι
    elif player == "Π":
        if computer == "Χ":
            print("Ο υπλογιστής διάλεξε: ", computer)
            print("Διάλεξες: ", player)
            print("Έχασες!")
        if computer == "Ψ":
            print("Ο υπλογιστής διάλεξε: ", computer)
            print("Διάλεξες: ", player)
            print("Κέρδισες")
    
    # Το ψαλίδι κερδίζει το χαρτί
    elif player == "Ψ":
        if computer == "Π":
            print("Ο υπλογιστής διάλεξε: ", computer)
            print("Διάλεξες: ", player)
            print("You lose!")
        if computer == "Χ":
            print("Ο υπλογιστής διάλεξε: ", computer)
            print("Διάλεξες: ", player)
            print("Κέρδισες!")
    
    # Το χαρτί κερδίζει τη πέτρα
    elif player == "Χ":
        if computer == "Ψ":
            print("Ο υπλογιστής διάλεξε: ", computer)
            print("Διάλεξες: ", player)
            print("Έχασες!")
        if computer == "Π":
            print("Ο υπλογιστής διάλεξε: ", computer)
            print("player: ", player)
            print("Κέρδισες!")

    # Ερώτηση στο χρήστη αν θέλει να ξαναπαίξει
    play_again = input("Πληκτρολόγησε ναι για να ξαναπαίξεις: ").lower()
    
    # τερματισμός παιχνιδιού εισάγοντας κενή συμβολοσειρά
    # το παιχνίδι τερματίζει μετά από 2 δευτερόλεπτα αν η απάντηση του χρήστη <> ναι 
    # διακοπή εντολής βρόχου ακόμη κι αν η προϋπόθεση του βρόχου δεν έχει γίνει False  
    
    if play_again == "" or play_again == " ":
        time.sleep(2)
        # διακοπή εντολής βρόχου ακόμη κι αν η προϋπόθεση του βρόχου δεν έχει γίνει False
        break
    elif play_again !="ναι":
        print(input("Δεν έδωσες έγκυρη απάντηση. Πάτησε enter για να ξαναδοκιμάσεις."))
        
print("Τέλος!")
# **************************************************************
