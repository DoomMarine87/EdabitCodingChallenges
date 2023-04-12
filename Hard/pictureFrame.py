"""Create a function that takes the width, height and character and returns a picture frame as a 2D list.
Examples

get_frame(4, 5, "#") ➞ [
  ["####"],
  ["#  #"],
  ["#  #"],
  ["#  #"],
  ["####"]
]
# Frame is 4 characters wide and 5 characters tall.


get_frame(10, 3, "*") ➞ [
  ["**********"],
  ["*        *"],
  ["**********"]
]
# Frame is 10 characters and wide and 3 characters tall.


get_frame(2, 5, "0") ➞ "invalid"
# Frame's width is not more than 2.

Notes

    Remember the gap.
    Return "invalid" if width or height is 2 or less (can't put anything inside)."""

def get_frame(w, h, ch):
    return[[ch*w]]+[[ch+" "*(w-2)+ch]]*(h-2)+[[ch*w]] if w>2 and h>2 else "invalid"
    

"""print(get_frame(4, 5, "#"))
print(get_frame(10, 3, "*"))
print(get_frame(2, 5, "0"))"""

print(get_frame(1, 6, "["))#, "invalid")
print(get_frame(5, 4, "z"))#, [["zzzzz"], ["z   z"], ["z   z"], ["zzzzz"]])
print(get_frame(3, 4, "A"))#, [["AAA"], ["A A"], ["A A"], ["AAA"]])
print(get_frame(10, 2, "`"))#, "invalid")
print(get_frame(10, 4, "l"))#, [["llllllllll"], ["l        l"], ["l        l"], ["llllllllll"]])
print(get_frame(5, 9, "Z"))#, [["ZZZZZ"], ["Z   Z"], ["Z   Z"], ["Z   Z"], ["Z   Z"], ["Z   Z"], ["Z   Z"], ["Z   Z"], ["ZZZZZ"]])
print(get_frame(4, 6, "J"))#, [["JJJJ"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["JJJJ"]])
print(get_frame(3, 4, "R"))#, [["RRR"], ["R R"], ["R R"], ["RRR"]])
print(get_frame(3, 6, "Q"))#, [["QQQ"], ["Q Q"], ["Q Q"], ["Q Q"], ["Q Q"], ["QQQ"]])
print(get_frame(3, 3, "^"))#, [["^^^"], ["^ ^"], ["^^^"]])
print(get_frame(5, 2, "F"))#, "invalid")
print(get_frame(3, 8, "J"))#, [["JJJ"], ["J J"], ["J J"], ["J J"], ["J J"], ["J J"], ["J J"], ["JJJ"]])
print(get_frame(7, 10, "`"))#, [["```````"], ["`     `"], ["`     `"], ["`     `"], ["`     `"], ["`     `"], ["`     `"], ["`     `"], ["`     `"], ["```````"]])
print(get_frame(6, 6, "v"))#, [["vvvvvv"], ["v    v"], ["v    v"], ["v    v"], ["v    v"], ["vvvvvv"]])
print(get_frame(7, 2, "?"))#, "invalid")
print(get_frame(3, 10, ":"))#, [[":::"], [": :"], [": :"], [": :"], [": :"], [": :"], [": :"], [": :"], [": :"], [":::"]])
print(get_frame(6, 7, "N"))#, [["NNNNNN"], ["N    N"], ["N    N"], ["N    N"], ["N    N"], ["N    N"], ["NNNNNN"]])
print(get_frame(7, 5, "h"))#, [["hhhhhhh"], ["h     h"], ["h     h"], ["h     h"], ["hhhhhhh"]])
print(get_frame(7, 5, "!"))#, [["!!!!!!!"], ["!     !"], ["!     !"], ["!     !"], ["!!!!!!!"]])
print(get_frame(2, 3, "F"))#, "invalid")
print(get_frame(1, 2, "E"))#, "invalid")
print(get_frame(6, 3, "j"))#, [["jjjjjj"], ["j    j"], ["jjjjjj"]])
print(get_frame(4, 7, "J"))#, [["JJJJ"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["JJJJ"]])
print(get_frame(8, 3, "`"))#, [["````````"], ["`      `"], ["````````"]])
print(get_frame(6, 8, "V"))#, [["VVVVVV"], ["V    V"], ["V    V"], ["V    V"], ["V    V"], ["V    V"], ["V    V"], ["VVVVVV"]])
print(get_frame(6, 2, "+"))#, "invalid")
print(get_frame(4, 1, "l"))#, "invalid")
print(get_frame(4, 8, "L"))#, [["LLLL"], ["L  L"], ["L  L"], ["L  L"], ["L  L"], ["L  L"], ["L  L"], ["LLLL"]])
print(get_frame(10, 7, "C"))#, [["CCCCCCCCCC"], ["C        C"], ["C        C"], ["C        C"], ["C        C"], ["C        C"], ["CCCCCCCCCC"]])
print(get_frame(4, 6, "T"))#, [["TTTT"], ["T  T"], ["T  T"], ["T  T"], ["T  T"], ["TTTT"]])
print(get_frame(9, 1, "t"))#, "invalid")
print(get_frame(9, 7, "&"))#, [["&&&&&&&&&"], ["&       &"], ["&       &"], ["&       &"], ["&       &"], ["&       &"], ["&&&&&&&&&"]])
print(get_frame(3, 1, "("))#, "invalid")
print(get_frame(10, 8, "<"))#, [["<<<<<<<<<<"], ["<        <"], ["<        <"], ["<        <"], ["<        <"], ["<        <"], ["<        <"], ["<<<<<<<<<<"]])
print(get_frame(8, 6, "O"))#, [["OOOOOOOO"], ["O      O"], ["O      O"], ["O      O"], ["O      O"], ["OOOOOOOO"]])
print(get_frame(2, 2, "T"))#, "invalid")
print(get_frame(4, 10, "J"))#, [["JJJJ"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["J  J"], ["JJJJ"]])
print(get_frame(7, 2, "4"))#, "invalid")
print(get_frame(7, 4, "~"))#, [["~~~~~~~"], ["~     ~"], ["~     ~"], ["~~~~~~~"]])
print(get_frame(8, 3, "="))#, [["========"], ["=      ="], ["========"]])
print(get_frame(3, 8, "<"))#, [["<<<"], ["< <"], ["< <"], ["< <"], ["< <"], ["< <"], ["< <"], ["<<<"]])
print(get_frame(7, 1, "4"))#, "invalid")
print(get_frame(7, 3, "o"))#, [["ooooooo"], ["o     o"], ["ooooooo"]])
print(get_frame(8, 2, "p"))#, "invalid")
print(get_frame(10, 9, "&"))#, [["&&&&&&&&&&"], ["&        &"], ["&        &"], ["&        &"], ["&        &"], ["&        &"], ["&        &"], ["&        &"], ["&&&&&&&&&&"]])
print(get_frame(8, 6, "-"))#, [["--------"], ["-      -"], ["-      -"], ["-      -"], ["-      -"], ["--------"]])
print(get_frame(5, 1, "n"))#, "invalid")
print(get_frame(1, 6, "r"))#, "invalid")"""

"""get_frame=lambda w,h,c:'invalid'if w<3or h<3else[[c*w]]+[[c+' '*(w-2)+c]]*(h-2)+[[c*w]]"""

