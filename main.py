from pyStandardGalacticAlphabet import SGA

sga_ = SGA()

from_en_to_sga = sga_.encode("Hello, world!")
print("From EN to SGA: ", from_en_to_sga)

from_sga_to_en = sga_.decode("Hᒷꖎꖎ𝙹, ∴𝙹∷ꖎ↸!")
print("From SGA to EN: ", from_sga_to_en)