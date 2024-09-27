telefonkatalog = [] # ["fornavn", "etternavn", "telefonnummer"]

def printMeny():
    print("---------------------Telefonkatalog------------------")
    print("| 1. Legg til ny person                             |")
    print("| 2. Søk opp person eller telefonnummer             |")
    print("| 3. Vis alle personer                              |")
    print("| 4. Endre person                                   |")
    print("| 5. Slett person                                   |")
    print("| 6. Avslutt                                        |")
    print("-----------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif valgtTall == "3":
        visAllePersoner()
    elif valgtTall == "6":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()
    elif valgtTall == "5":
        slettPerson()
    elif valgtTall == "4":
        endrePerson()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-4: ")
        utfoerMenyvalg(nyttForsoek)

def registrerPerson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")

    nyRegistrering = [fornavn, etternavn, telefonnummer]
    telefonkatalog.append(nyRegistrering)

    print("{0} {1} er regitrert med telefonnummer {2}"
          .format(fornavn, etternavn, telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

def visAllePersoner():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
    else:
        print("************************************************"
              "************************************************")
        
        for personer in telefonkatalog:
            print("* Fornavn: {:15s} Etternavn: {:15s} Telefonnummer:{:8s}"
                    .format(personer[0], personer[1], personer[2]))
        print("************************************************"
              "************************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()

def sokPerson():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        printMeny()
    else:
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnPerson("fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnPerson("etternavn:", navn)
        elif sokefelt == "3":
            tlfnummer = input("Telefonnummer: ")
            finnPerson("telefonnummer", tlfnummer)
        elif sokefelt == "4":
            printMeny()
        else:
            print("Ugyldig valg. Velg et tall mellom 1-4: ")
            sokPerson()

def finnPerson(typeSok, sokeTekst):
    svar = []
    for personer in telefonkatalog:
        if typeSok == "fornavn":
            if personer[0] == sokeTekst:
                svar.append(personer)
        elif typeSok == "etternavn":
                svar.append(personer)
        elif typeSok == "telefonnummer":
                svar.append(personer)

    if not svar:
        print("finner ingen personer")
    else:
        for personer in svar:
            print("{0} {1} har telefonnummer {2}"
                  .format(personer[0], personer[1], personer[2]))
        

def slettPerson():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
    else:       
        navn = input("Skriv inn fornavn eller etternavn på personen du vil slette: ")
        funnet = False
        for person in telefonkatalog:
            if navn in person:  # Sjekker om fornavn eller etternavn matcher
                telefonkatalog.remove(person)
                print(f"{person[0]} {person[1]} er slettet fra katalogen.")
                funnet = True
                break
        if not funnet:
            print("Ingen treff i katalogen.")
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

def endrePerson():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
    else:
        navn = input("Skriv inn fornavn eller etternavn på personen du vil endre: ")
        funnet = False
        for person in telefonkatalog:
            if navn in person:  # Sjekker om fornavn eller etternavn matcher
                print(f"Fant {person[0]} {person[1]} med telefonnummer {person[2]}.")
                nytt_fornavn = input(f"Nytt fornavn (trykk enter for å beholde '{person[0]}'): ")
                nytt_etternavn = input(f"Nytt etternavn (trykk enter for å beholde '{person[1]}'): ")
                nytt_telefonnummer = input(f"Nytt telefonnummer (trykk enter for å beholde '{person[2]}'): ")
                
                # Oppdaterer kun dersom brukeren skriver inn noe nytt
                if nytt_fornavn:
                    person[0] = nytt_fornavn
                if nytt_etternavn:
                    person[1] = nytt_etternavn
                if nytt_telefonnummer:
                    person[2] = nytt_telefonnummer
                
                print(f"Profilen er oppdatert: {person[0]} {person[1]} - {person[2]}")
                funnet = True
                break
        if not funnet:
            print("Ingen treff i katalogen.")
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()


printMeny()