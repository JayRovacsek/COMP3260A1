# this is kind of just a quick hack together
import sys
import transDecrypt
if __name__ == "__main__":
    if len(sys.argv) is 1:
        reps = int(input("Enter the number of keys you want to check: "))
    else:
        reps = int(sys.argv[1]) # should only ever use 1 arg
    i = 1
    while(i <= reps):
        print("\nKey {}".format(i))
        print(transDecrypt.decrypt(i,'hteinemgmcaaiheawnasihpcreahcmniuesetdecnoyrtnapddcyretpercsteessmgasomeerrcepsileyeinmwagsafmaaliorfyletdealecrtemocaheinarlctoramohcnseiocpirmisgvanraeytifoiffdrenmtedoltseehngieamauswescmodemcairlladnyawaslsaootpddeyhtbmeltiiraadnyogenrvemtlanesvcirsefnaomueorbnftoiasnotsmafosumylyanbizemrgnabfeyroadneudignresodncowlwdrrahgetreamnmlitraimydleohtwheemrcthanegamisihvetreinosomtocsmmnyloidcsusestehdamhnichesaganidoneotiterbycuaeesliladerpycotoigltswresaeltebdocyretplraaegubmnrefemossgseahttahabdeenecnpehierotndehahcmnidceeyrtoipwnsamaedosspbieyblopihslrcpotyrgpehasrairmnaeejrswiejkzrryoykcadniehrkynyzaslgikrmofichrepubeuarerosncrtcitunonddaceytproimtenohsewdereildevefdrorplomnatbodiranitnafardcntehenielltgineceagndeihtogurthisshuoccerdonmaedelrtuwassaagiiifnactiantdteholaidelaweffrrotehtxecitafnunelecfluortidsabetdeaubayttipaalcsssmseneitstahtehtneotfdehuoreepnawawrsahatsndeeybwyotaesebracsoeutfeedhrcpitynofegomrnicahprse'))
        i+=1
