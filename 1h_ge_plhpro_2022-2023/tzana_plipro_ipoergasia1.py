import time
# όσο η συνθήκη παραμένει αληθής ζήτα από το χρήστη input
while True:
    word = input(str("Δώσε λέξη: ")).upper()
    # αν ο χρήστης πληκτρολογήσει κενή συμβολοσειρά τότε το πρόγραμμα τερματίζει
    if word == " " or word == "":
      print("δεν είναι λέξη")
      time.sleep(1) 
      break
    # αν η αναποδη λέξη είναι ίδια με το input του χρήστη
    elif word == word[::-1]:
        print("Παλίνδρομη") 
        continue   
    else:
        print("όχι παλίνδρομη")
